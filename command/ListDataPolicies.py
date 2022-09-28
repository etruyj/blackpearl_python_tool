# ListDataPolicies.py
#       Description:
#           Creates a summary list of all data policies.

from structures.DataPolicySummary import DataPolicySummary
from util.Logger import Logger

def createList(blackpearl, logbook):
    logbook.INFO("Creating list of Data Policies...")
    logbook.DEBUG("Calling blackpearl.getDataPolicies()...")
    
    output = []

    policy_list = blackpearl.getDataPolicies(logbook)

    for policy in policy_list:
        summary = DataPolicySummary()
        summary.name = policy['Name']
        summary.uuid = policy['Id']

        output.append(summary)

    return output


