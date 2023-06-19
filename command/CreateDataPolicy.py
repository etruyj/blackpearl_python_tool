# CreateDataPolicy.py
#   Allows the creation of data policies via the command line
#   Due to the number of configuration options, these must be specified by a JSON
#   file. This functions to verify all the required parameters are specificed.

from util.Logger import Logger
from util.BPConnector import BPConnector

def fillMissingFieldsThenVerify(blackpearl, policy, logbook):
    if('name' in policy.keys()):
        name = policy['name']
    else:
        name = None
    
    if('always_accept_replicated_puts' in policy.keys()):
        force_puts = policy['always_accept_replicated_puts']
    else:
        force_puts = None

    if('minimize_spanning' in policy.keys()):
        min_spanning = policy['minimize_spanning']
    else:
        min_spanning = None

    if('blobbing_enabled' in policy.keys()):
        blobbing = policy['blobbing_enabled']
    else:
        blobbing = None

    if('checksum_type' in policy.keys()):
        checksum_type = policy['checksum_type']
    else:
        checksum_type = None

    if('default_blob_size' in policy.keys()):
        blob_size = policy['default_blob_size']
    else:
        blob_size = None

    if('default_get_priority' in policy.keys()):
        get_priority = convertPriorityToEnum(policy['default_get_priority'])
    else:
        get_priority = None

    if('default_put_priority' in policy.keys()):
        put_priority = convertPriorityToEnum(policy['default_put_priority'])
    else:
        put_priority = None

    if('verify_after_write' in policy.keys()):
        verify_after_write = policy['verify_after_write']
    else:
        verify_after_write = False

    if('default_verify_priority' in policy.keys()):
        verify_priority = convertPriorityToEnum(policy['default_verify_priority'])
    else:
        verify_priority = None

    if('require_end_to_end_crc' in policy.keys()):
        end_to_end_crc = policy['require_end_to_end_crc']
    else:
        end_to_end_crc = None

    if('versions_to_keep' in policy.keys()):
        versions_to_keep = policy['versions_to_keep']
    else:
        versions_to_keep = 1000

    if('rebuild_priority' in policy.keys()):
        rebuild_priority = convertPriorityToEnum(policy['rebuild_priority'])
    else:
        rebuild_priority = "LOW"

    if('versioning' in policy.keys()):
        versioning = policy['versioning']
    else:
        versioning = None

    return verifyThenCreate(blackpearl, name, force_puts, min_spanning, blobbing, checksum_type, blob_size, get_priority, put_priority, verify_after_write, verify_priority, end_to_end_crc, versions_to_keep, rebuild_priority, versioning, logbook)
    

def convertPriorityToEnum(priority):
    match priority:
        case "critical" | "Critical" | "CRITICAL":
            return "CRITICAL"
        case "urgent" | "Urgent" | "URGENT":
            return "URGENT"
        case "high" | "High" | "HIGH":
            return "HIGH"
        case "normal" | "Normal" | "NORMAL":
            return "NORMAL"
        case "low" | "Low" | "LOW":
            return "LOW"
        case "background" | "Background" | "BACKGROUND":
            return "BACKGROUND"

def verifyThenCreate(blackpearl, name, force_puts, min_spanning, blobbing, checksum_type, blob_size, get_priority, put_priority, verify_after_write, verify_priority, end_to_end_crc, versions_to_keep, rebuild_priority, versioning, logbook):
    # Verify required fields exists
    if(name == None):
        logbook.ERROR("Data policy is missing required field: name")
        print("Data policy is missing required field: name")
    elif(force_puts == None):    
        logbook.ERROR("Data policy [" + name + "] is missing required field: always_force_put_jobs")
        print("Data policy [" + name + "] is missing required field: always_force_put_jobs")
    elif(min_spanning == None):
        logbook.ERROR("Data policy [" + name + "] is missing required field: always_minimize_spanning_across_media")
        print("Data policy [" + name + "] is missing required field: always_minimize_spanning_across_media")
    elif(blobbing == None):
        logbook.ERROR("Data policy [" + name + "] is missing required field: blobbing_enabled")
        print("Data policy [" + name + "] is missing required field: blobbing_enabled")
    elif(checksum_type == None):
        logbook.ERROR("Data policy [" + name + "] is missing required field: checksum_type")
        print("Data policy [" + name + "] is missing required field: checksum_type")
#    elif(blob_size == None):
#        logbook.ERROR("Data policy [" + name + "] is missing required field: default_blob_size")
#        print("Data policy [" + name + "] is missing required field: default_blob_size")
    elif(get_priority == None):
        logbook.ERROR("Data policy [" + name + "] is missing required field: default_get_job_priority")
        print("Data policy [" + name + "] is missing required field: default_get_job_priority")
    elif(put_priority == None):
        logbook.ERROR("Data policy [" + name + "] is missing required field: default_put_job_priority")
        print("Data policy [" + name + "] is missing required field: default_put_job_priority")
    elif(verify_after_write == None):
        logbook.ERROR("Data policy [" + name + "] is missing required field: default_verify_after_write")
        print("Data policy [" + name + "] is missing required field: default_verify_after_write")
    elif(verify_priority == None):
        logbook.ERROR("Data policy [" + name + "] is missing required field: default_verify_job_priority")
        print("Data policy [" + name + "] is missing required field: default_verify_job_priority")
    elif(end_to_end_crc == None):
        logbook.ERROR("Data policy [" + name + "] is missing required field: end_to_end_crc_required")
        print("Data policy [" + name + "] is missing required field: end_to_end_crc_required")
    elif(versions_to_keep == None):
        logbook.ERROR("Data policy [" + name + "] is missing required field: versions_to_keep")
        print("Data policy [" + name + "] is missing required field: versions_to_keep")
    elif(rebuild_priority == None):
        logbook.ERROR("Data policy [" + name + "] is missing required field: rebuild_priority")
        print("Data policy [" + name + "] is missing required field: rebuild_priority")
    elif(versioning == None):
        logbook.ERROR("Data policy [" + name + "] is missing required field: versioning")
        print("Data policy [" + name + "] is missing required field: versioning")
    else:
        logbook.INFO("All required data policy fields are present. Creating data policy...")
        logbook.DEBUG("Calling blackpearl.createDataPolicy()...")
        return blackpearl.createDataPolicy(name, force_puts, min_spanning, blobbing, checksum_type, blob_size, get_priority, put_priority, verify_after_write, verify_priority, end_to_end_crc, versions_to_keep, rebuild_priority, versioning, logbook)
