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

def deleteBucketAcl(bucket_id, acl, blackpearl, logbook):
    try:
        logbook.INFO("Sending delete ACL [" + acl["Id"] + "] on bucket " + bucket_id)

        response = blackpearl.delete_bucket_acl_spectra_s3(ds3.DeleteBucketAclSpectraS3Request(acl["Id"]))

    except Exception as e:
        logbook.ERROR(e.__str__())

        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform delete-bucket-acls on bucket [" + bucket + "]")
        else:
            raise Exception("Failed to delete ACL for bucket [" + bucket + "].")

def getBucketAcls(bucket, blackpearl, logbook):
    try:
        logbook.INFO("Fetchings ACLs for bucket [" + bucket + "]")

        response = blackpearl.get_bucket_acls_spectra_s3(ds3.GetBucketAclsSpectraS3Request(bucket))

        logbook.INFO("Found (" + str(len(response.result["BucketAclList"])) + ") ACLs.")

        return response.result["BucketAclList"]
    except Exception as e:
        logbook.ERROR(e.__str__())

        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform get-bucket-acls on bucket [" + bucket + "]")
        else:
            raise Exception("Failed to fetch ACLs for bucket [" + bucket + "].")
        

def putBucketAclForGroup(bucket_id, group_id, permission, blackpearl, logbook):
    try:
        logbook.WARN("Putting bucket ACL " + permission + " for group [" + group_id + "] on bucket " + bucket_id)

        blackpearl.put_bucket_acl_for_group_spectra_s3(ds3.PutBucketAclForGroupSpectraS3Request(bucket_id, group_id, permission))
    except Exception as e:
        logbook.ERROR(e.__str__())

        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform put-bucket-acls on bucket [" + bucket + "]")
        else:
            raise Exception("Failed to put ACL for bucket [" + bucket + "].")

def putBucketAclForUser(bucket_id, user_id, permission, blackpearl, logbook):
    try:
        logbook.WARN("Putting bucket ACL " + permission + " for user [" + user_id + "] on bucket " + bucket_id)

        blackpearl.put_bucket_acl_for_user_spectra_s3(ds3.PutBucketAclForUserSpectraS3Request(bucket_id, permission, user_id))
    except Exception as e:
        logbook.ERROR(e.__str__())

        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform put-bucket-acls on bucket [" + bucket + "]")
        else:
            raise Exception("Failed to put ACL for bucket [" + bucket + "].")
