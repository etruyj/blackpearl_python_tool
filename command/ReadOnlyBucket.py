#====================================================================
# ReadOnlyBucket.py
#   Description:
#       This command controls all the tasks associated with making a
#       bucket read-only. This task is accomplished by modifying the
#       existing bucket ACLs so all users only have the ability to 
#       restore data from the bucket and view active jobs.
#====================================================================

def configureAcls(bucket, blackpearl, logbook):
    try:
        logbook.INFO("Changing permissions to make bucket [" + bucket + "] read-only.")
        
        # 1.) Get all ACLs on the bucket.
        acls = getExistingAcls(bucket, blackpearl, logbook)
        
        # 2.) Delete all ACLs off bucket.
        #       Store user and group Ids to re-put read-only permissions.
        user_list = []
        group_list = []

        for acl in acls:
            if(acl["UserId"] != None):
                actor = "User [" + acl["UserId"] + "]"
                if(acl["UserId"] not in user_list):
                    user_list.append(acl["UserId"])
            else:
                actor = "Group [" + acl["GroupId"] + "]"
                if(acl["GroupId"] not in group_list):
                    group_list.append(acl["GroupId"])
            
            if(acl["Permission"] == "OWNER"):
                # Skip - there has to be a bucket owner.
                logbook.INFO(actor + " is the bucket owner. Maintaining ownership.")
            else:
                deleteExistingAcl(acl, blackpearl, logbook)

        # 3.) Put read-only permissions.
        for user in user_list:
            setUserAsReadOnly(bucket, user, blackpearl, logbook)

        for group in group_list:
            setGroupAsReadOnly(bucket, group, blackpearl, logbook)
    except Exception as e:
        logbook.ERROR(e.__str__())
        return e.__str__()

def deleteExistingAcl(acl, blackpearl, logbook):
    try:
        if(acl["UserId"] != None):
            actor = "for user [" + acl["UserId"] + "]"
        else:
            actor = "for group [" + acl["GroupId"] + "]"

        logbook.WARN("Removing permission [" + acl["Permission"] + "] from bucket [" + acl["BucketId"] + "] " + actor)
        
        blackpearl.deleteBucketAcl(acl["BucketId"], acl, logbook)
    except Exception as e:
        raise e

def getExistingAcls(bucket, blackpearl, logbook):
    try:
        logbook.INFO("Pulling list of ACLs for bucket " + bucket)

        acls = blackpearl.getBucketAcls(bucket, logbook)

        return acls
    except Exception as e:
        raise e

def setGroupAsReadOnly(bucket, group, blackpearl, logbook):
    try:
        logbook.INFO("Setting group [" + group + "] to read_only on bucket " + bucket + "...")
        permissions = ["LIST", "READ", "JOB"]

        for perm in permissions:
            blackpearl.putBucketAclForGroup(bucket, group, perm, logbook)
    except Exception as e:
        raise e

def setUserAsReadOnly(bucket, user, blackpearl, logbook):
    try:
        logbook.INFO("Setting user [" + user + "] to read_only on bucket " + bucket + "...")
        permissions = ["LIST", "READ", "JOB"]

        for perm in permissions:
            blackpearl.putBucketAclForUser(bucket, user, perm, logbook)
    except Exception as e:
        raise e
