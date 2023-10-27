#====================================================================
# ReadOnlyBucket.py
#   Description:
#       This command controls all the tasks associated with making a
#       bucket read-only. This task is accomplished by modifying the
#       existing bucket ACLs so all users only have the ability to 
#       restore data from the bucket and view active jobs.
#====================================================================


#================================================
# POC Workflow
# Resets all users to have the same 3 permissions with the exception
# of the bucket owner.
#================================================

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

# This command removes all permissions from the listed group.
# The intent is to be used in conjunction with the setGroupAsReadOnly()
# and setUserAsReadOnly() calls in order to set specific permissions 
# for all agents.
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

# This command adds LIST, READ, and JOB privs to a group.
# It does not remove any permissions. That must be done in a different
# Function. Not used in the production script as this overwrites the
# original configuration giving all users the same 3 abilities regardless
# of the admins original intention.
def setGroupAsReadOnly(bucket, group, blackpearl, logbook):
    try:
        logbook.INFO("Setting group [" + group + "] to read_only on bucket " + bucket + "...")
        permissions = ["LIST", "READ", "JOB"]

        for perm in permissions:
            blackpearl.putBucketAclForGroup(bucket, group, perm, logbook)
    except Exception as e:
        raise e

# This command adds LIST, READ, and JOB privs to a user.
# It does not remove any permissions. That must be done in a different
# Function. Not used in the production script as this overwrites the
# original configuration giving all users the same 3 abilities regardless
# of the admins original intention.
def setUserAsReadOnly(bucket, user, blackpearl, logbook):
    try:
        logbook.INFO("Setting user [" + user + "] to read_only on bucket " + bucket + "...")
        permissions = ["LIST", "READ", "JOB"]

        for perm in permissions:
            blackpearl.putBucketAclForUser(bucket, user, perm, logbook)
    except Exception as e:
        raise e

#================================================
# Distribution Attempt
#================================================

def deleteAcl(acl, blackpearl, logbook):
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


def makeBucketReadOnly(bucket, blackpearl, logbook):
    try:
        logbook.INFO("Marking bucket [" + bucket + "] as read-only.")
        permissions = ["LIST", "READ", "JOB"]
        permission_string = "["

        for perm in permissions:
            permission_string = permission_string + perm + ","

        permission_string = permission_string[:-1] + "]"

        logbook.INFO("Removing all but the following permissions: " + permission_string)


        # 1.) Get all ACLs on the bucket.
        logbook.DEBUG("getExistingAcls(" + bucket + ")")
        acls = getExistingAcls(bucket, blackpearl, logbook)
        
        # 2.) Delete all ACLs off bucket.
        #       Store user and group Ids to re-put read-only permissions.
        logbook.DEBUG("Sorting ACLs by user or group.")
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
                if(acl["Permission"] not in permissions):
                    logbook.DEBUG(actor + "'s ACL permission " + acl["Permission"] + " is not listed in allowed permissions.")
                    logbook.DEBUG("Calling deleteAcl()")
                    deleteAcl(acl, blackpearl, logbook)


    except Exception as e:
        raise e
