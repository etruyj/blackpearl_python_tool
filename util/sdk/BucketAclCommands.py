#====================================================================
# BucketAclCommands.py
#   Description:
#       This code is for exploring adding BucketAclCommands to the 
#       python tool. 
#   
#   Functions:
#       - deleteBucketAcls
#       - getBucketAcls
#       - putBucketAclForGroup
#       - putBucketAclForUser
#====================================================================

from ds3 import ds3

def putBucketAclForUser(bucket_id, user_id, permission, blackpearl, logbook):
    try:
        logbook.WARN("Putting bucket ACL for user [" + user_id + "] on bucket " + bucket_id)

        blackpearl.put_bucket_acl_for_user_spectra_s3(ds3.PutBucketAclForUserSpectraS3Request(bucket_id, permission, user_id))
    except Exception as e:
        logbook.ERROR(e.__str__())
        raise e
