#====================================================================
# ReadOnlyBucket.py
#   Description:
#       This command controls all the tasks associated with making a
#       bucket read-only. This task is accomplished by modifying the
#       existing bucket ACLs so all users only have the ability to 
#       restore data from the bucket and view active jobs.
#====================================================================

def testCode(bucket, blackpearl, logbook):
    try:
        logbook.INFO("Testing the MakeBucketReadOnly command...")
        permissions = ["LIST", "READ", "JOB"]

        for perm in permissions:
            blackpearl.putBucketAclForUser(bucket, "seans", perm, logbook)
    except Exception as e:
        return e.__str__()
