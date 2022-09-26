#====================================================================
# SDKCommands.py
#       Description:
#           The basic SDK commands that are used for the script's
#           commands.
#====================================================================

from ds3 import ds3
from util.Logger import Logger

def getBuckets(blackpearl, logbook):
    try:
        logbook.INFO("Fetching bucket names.")
        logbook.DEBUG("blackpear.get_buckets_spectra_s3()")
        
        getBucketsResponse = blackpearl.get_buckets_spectra_s3(ds3.GetBucketsSpectraS3Request())

        logbook.INFO("Found " + str(len(getBucketsResponse.result['BucketList'])) + " buckets.")
        
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

def getUsers(blackpearl, logbook):
    try:
        logbook.INFO("Fetching user list...")
        logbook.DEBUG("blackpearl.get_users_spectra_s3()")

        getUsersResponse = blackpearl.get_users_spectra_s3(ds3.GetUsersSpectraS3Request())

        return getUsersResponse.result['UserList']
    except Exception as e:
        print(e)
        logbook.ERROR("Failed to retrieve user list")
