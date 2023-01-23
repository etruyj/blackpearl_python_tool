#====================================================================
#   MapBuckets.py
#       Description: 
#           Create a dictionary of [String, String] to determine
#           bucket name from id and bucket id from name
#====================================================================

from structures.BucketSummary import BucketSummary

def createIDNameMap(bucket_list):
    bucket_map = {}

    if(bucket_list != None):
        for bucket in bucket_list:
            bucket_map[bucket.getId()] = bucket.getName()

    return bucket_map

def createNameIDMap(bucket_list):
    bucket_map = {}

    if(bucket_list != None):
        for bucket in bucket_list:
            bucket_map[bucket.getName()] = bucket.getId()

    return bucket_map

