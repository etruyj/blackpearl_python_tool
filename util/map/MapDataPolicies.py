#====================================================================
#   MapDataPolicies.py
#       Description:
#           Creates a dictionary of [String, String] to determine
#           policy name from id and policy id from name.
#====================================================================

from structures.DataPolicySummary import DataPolicySummary

def createIDNameMap(policy_list):
    policy_map = {}

    if(policy_list != None):
        for policy in policy_list:
            policy_map[policy.uuid] = policy.name

    return policy_map

def createNameIDMap(policy_list):
    policy_map = {}
    
    if(policy_list != None):
        for policy in policy_list:
            policy_map[policy.name] = policy.uuid

    return policy_map

