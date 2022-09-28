#====================================================================
# SDKCommands.py
#       Description:
#           The basic SDK commands that are used for the script's
#           commands.
#====================================================================

from ds3 import ds3
from util.Logger import Logger

def createBucket(blackpearl, name, data_policy, owner, logbook):
    try:
        logbook.INFO("Creating bucket [" + name + "]...")
        logbook.DEBUG("blackpearl.put_bucket_spectra_s3()...")

        # ds3.PutBucketSpectraS3Request(bucket_name, data_policy_id, id=?, owner)
        #   not sure what the id field is. Can you specifiy the bucket id when creating the bucket?
        createBucketResponse = blackpearl.put_bucket_spectra_s3(ds3.PutBucketSpectraS3Request(name, data_policy, None, owner))

        return createBucketResponse
    except Exception as e:
        print(e)
        logbook.ERROR("Failed to create bucket [" + name + "]")

def createDataPolicy(blackpearl, name, force_puts, min_spanning, blobbing, checksum_type, blob_size, get_priority, put_priority, verify_after_write, verify_priority, end_to_end_crc, versions_to_keep, rebuild_priority, versioning, logbook):
    try:
        logbook.INFO("Creating data policy [" + name + "]...")
        logbook.DEBUG("blackpearl.put_data_policy_spectra_s3()...")
        
        createPolicyResponse = blackpearl.put_data_policy_spectra_s3(ds3.PutDataPolicySpectraS3Request(name, force_puts, min_spanning, blobbing, checksum_type, blob_size, get_priority, put_priority, verify_after_write, verify_priority, end_to_end_crc, versions_to_keep, rebuild_priority, versioning))

        return createPolicyResponse
    except Exception as e:
        print(e)
        logbook.ERROR("Failed to create data policy [" + name + "]")

def getBuckets(blackpearl, logbook):
    try:
        logbook.INFO("Fetching bucket names.")
        logbook.DEBUG("blackpear.get_buckets_spectra_s3()")
        
        getBucketsResponse = blackpearl.get_buckets_spectra_s3(ds3.GetBucketsSpectraS3Request())

        logbook.INFO("Found (" + str(len(getBucketsResponse.result['BucketList'])) + ") buckets.")
        
        return getBucketsResponse.result['BucketList']

    except Exception as e:
        print(e)
        logbook.ERROR("Failed to retrieve buckets")

def getBucketInfo(blackpearl, name, logbook):
    try:
        logbook.INFO("Fetching details on bucket [" + name + "]")
        logbook.DEBUG("blackpearl.get_bucket_spectra_s3(" + name + ")")
        getBucketResponse = blackpearl.get_bucket_spectra_s3(ds3.GetBucketSpectraS3Request(name))

        print(vars(getBucketResponse))
    except Exception as e:
        print(e)
        logbook.ERROR("Failed to retrieve info.")

def getBucketNames(blackpearl, logbook):
    try:
        logbook.INFO("Fetching bucket names.")
        logbook.DEBUG("blackpear.get_service()")
        
        getServiceResponse = blackpearl.get_service(ds3.GetServiceRequest())
        
        logbook.INFO("Found " + str(len(getServiceResponse.result['BucketList'])) + " buckets.")

        return getServiceResponse.result['BucketList']

    except Exception as e:
        print(e)
        logbook.ERROR("Failed to retrieve buckets")

def getDataPolicies(blackpearl, logbook):
    try:
        logbook.INFO("Fetching data policies...")
        logbook.DEBUG("Calling blackpearl.get_data_policies_spectra_s3()...")

        getDataPolicies = blackpearl.get_data_policies_spectra_s3(ds3.GetDataPoliciesSpectraS3Request())

        logbook.INFO("Found (" + str(len(getDataPolicies.result['DataPolicyList'])) + ") data policies.")

        return getDataPolicies.result['DataPolicyList']
    except Exception as e:
        print(e)
        logbook.ERROR("Failed to retrieve data policies.")

def getStorageDomains(blackpearl, logbook):
    try:
        logbook.INFO("Fetching storage domains...")
        logbook.DEBUG("Calling blackpearl.get_storage_domains_spectra_s3()...")

        getStorageDomains = blackpearl.get_storage_domains_spectra_s3(ds3.GetStorageDomainsSpectraS3Request())

        #print(vars(getStorageDomains))
        return getStorageDomains.result['StorageDomainList']
    except Exception as e:
        print(e)
        logbook.ERROR("Failed to retrieve storage domains.")

def getUsers(blackpearl, logbook):
    try:
        logbook.INFO("Fetching user list...")
        logbook.DEBUG("blackpearl.get_users_spectra_s3()")

        getUsersResponse = blackpearl.get_users_spectra_s3(ds3.GetUsersSpectraS3Request())

        logbook.INFO("Found (" + str(len(getUsersResponse.result['UserList'])) + ") users.")

        return getUsersResponse.result['UserList']
    except Exception as e:
        print(e)
        logbook.ERROR("Failed to retrieve user list")
