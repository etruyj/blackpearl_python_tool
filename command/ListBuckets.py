#====================================================================
#   ListBuckets.py
#       Description:
#           Provides a list of buckets
#====================================================================

import command.ListDataPolicies as ListDataPolicies
import command.ListUsers as ListUsers
import util.Logger as Logger
import util.map.MapDataPolicies as MapDataPolicies
import util.map.MapUsers as MapUsers

from structures.BucketSummary import BucketSummary

def createList(blackpearl, logbook):
    logbook.INFO("Creating list of buckets...")
    logbook.DEBUG("Calling blackpearl.getBuckets()")
    output = []
    
    bucket_list = blackpearl.getBuckets(logbook)

    logbook.DEBUG("Calling ListUsers.createList()")
    user_list = ListUsers.createList(blackpearl, logbook);

    logbook.DEBUG("Calling MapUsers.createIDNameMap()")
    user_map = MapUsers.createIDNameMap(user_list)
   
    logbook.DEBUG("Calling ListDataPolicies.createList()")
    policy_list = ListDataPolicies.createList(blackpearl, logbook)

    logbook.DEBUG("Calling MapDataPolicies.createIDNameMap()")
    policy_map = MapDataPolicies.createIDNameMap(policy_list)

    if(bucket_list == None):
        eprint("Unable to retrieve bucket list")
        logbook.ERROR("Unable to retrieve bucket list")
    else:
        for bucket in bucket_list:
            summary = BucketSummary()
            summary.name = bucket['Name']

            if(user_map[bucket['UserId']] == None):
                logbook.WARN("Unable to find user with id [" + bucket['UserId'] + "]")
                summary.owner = bucket['UserId']
            else:
                summary.owner = user_map[bucket['UserId']]

            if(policy_map[bucket['DataPolicyId']] == None):
                logbook.WARN("Unabled to find data policy with id [" + bucke['DataPolicyId'] + "]")
                summary.data_policy = bucket['DataPolicyId']
            else:
                summary.data_policy = policy_map[bucket['DataPolicyId']]

            summary.size = bucket['LogicalUsedCapacity']

            output.append(summary)

    return output
