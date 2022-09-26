#====================================================================
#   ListBuckets.py
#       Description:
#           Provides a list of buckets
#====================================================================

import util.Logger as Logger

from structures.BucketSummary import BucketSummary

def createList(blackpearl, logbook):
    logbook.DEBUG("Calling blackpearl.getBuckets()");
    output = []
    bucket_list = []
    
    bucket_list = blackpearl.getBuckets(logbook)

   
    if(bucket_list == None):
        eprint("Unable to retrieve bucket list")
        logbook.ERROR("Unable to retrieve bucket list")
    else:
        for bucket in bucket_list:
            summary = BucketSummary()
            summary.name = bucket['Name']
            summary.owner = bucket['UserId']
            summary.data_policy = bucket['DataPolicyId']
            summary.size = bucket['LogicalUsedCapacity']

            output.append(summary)

    return output
