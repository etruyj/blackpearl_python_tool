# CreateVolume
#   Handles all the volume creation commands.

import util.convert.StorageUnits as StorageUnits

def fillFieldsThenVerify(blackpearl, volume_info, pool, logbook):

    if('access_time' in volume_info.keys()):
        access_time = volume_info['access_time'];
    else:
        access_time = False
    
    if('case_sensitive' in volume_info.keys()):
        case_insensitive = volume_info['case_sensitive']
    else:
        case_insensitive = True
    
    if('compression' in volume_info.keys()):
        compression = volume_info['compression']
    else:
        compression = False
    
    if('deduplication' in volume_info.keys()):
        deduplication = volume_info['deduplication']
    else:
        deduplication = False
    
    if('name' in volume_info.keys()):
        name = volume_info['name']
    else:
        name = "none"
    
    # Not sure of the filters required here.
    # Not seeing any of these in my outputs and 
    # NFI isn't supported in this stage of the script.
    nfi_repeat_schedule_daily = 1
    nfi_repeat_schedule_hour = 1
    nfi_repeat_schedule_minute = 0
    nfi_repeat_schedule_unit = "daily"
    nfi_repeat_schedule_weekly = False

    if('nfi_volume_policy_bucket_id' in volume_info.keys()):
        nfi_volume_policy_bucket_id = volume_info['nfi_volume_policy_bucket_id']
    else:
        nfi_volume_policy_bucket_id = ""

    if('nfi_volume_policy_cron_string' in volume_info.keys()):
        nfi_volume_policy_cron_string = nfi_volume_policy_cron_string
    else:
        nfi_volume_policy_cron_string = "0 3 */1 * *"
    
    if('nfi_volume_policy_enabled' in volume_info.keys()):
        nfi_volume_policy_enabled = volume_info['nfi_volume_policy_enabled']
    
        #Set to false because the code doesn't suppor this yet.
        if(nfi_volume_policy_enabled):
            logbook.WARN("NFI is not supported in this version of code. Disabling NFI for volume [" + name + "].")
            print("WARNING: NFI is not supported in this version of code. Disabling NFI for volume [" + name + "].")
            print("Please configure NFI manually from the BlackPearl UI.")
            nfi_volume_policy_enabled = False

    else:
        nfi_volume_policy_enabled = False

    if('nfi_volume_policy_nfi_system_id' in volume_info.keys()):
        nfi_volume_policy_nfi_system_id = volume_info['nfi_volume_policy_nfi_system_id']
    else:
        nfi_volume_policy_nfi_system_id = "1"
    
    if('nfi_volume_policy' in volume_info.keys()):
        nfi_volume_policy = volume_info['nfi_volume_info']
    else:
        nfi_volume_policy = "copy and keep"
    
    if(pool != None):
        pool_id = pool
    else:
        pool_id = "none"
    
    #max size bytes
    if('quota' in volume_info.keys()):
        StorageUnits.bytesToHumanReadable(volume_info['quota']) # Testing
        quota = StorageUnits.humanReadableToBytes(volume_info['quota'])

        # Check for error handling.
        # 0 is an invalid input
        if(quota <= 0):
            quota == ""
    else:
        quota = ""

    #min size bytes
    if('reservation' in volume_info.keys()):
        StorageUnits.bytesToHumanReadable(volume_info['reservation']) # Testing
        reservation = StorageUnits.humanReadableToBytes(volume_info['reservation'])
        
        # Check for error handling.
        # 0 is an invalid input
        if(reservation <= 0):
            reservation == ""
    else:
        reservation = ""
    
    if('read_only' in volume_info.keys()):
        read_only = volume_info['read_only']
    else:
        read_only = False
    
    if('size' in volume_info.keys()):
        size = volume_info['size']
    else:
        size = None
    
    # Not sure what key corresponds to this.
    snapshot_change_threshold = "80"

    if('type' in volume_info.keys()):
        vol_type = volume_info['type']
    else:
        vol_type = "data"

    verifyThenCreate(blackpearl, access_time, case_insensitive, compression, deduplication, name, nfi_repeat_schedule_daily, nfi_repeat_schedule_hour, nfi_repeat_schedule_minute, nfi_repeat_schedule_unit, nfi_repeat_schedule_weekly, nfi_volume_policy_bucket_id, nfi_volume_policy_cron_string, nfi_volume_policy_enabled, nfi_volume_policy_nfi_system_id, nfi_volume_policy, pool_id, quota, reservation, read_only, size, snapshot_change_threshold, vol_type, logbook)

def verifyThenCreate(blackpearl, access_time, case_insensitive, compression, deduplication, name, nfi_repeat_schedule_daily, nfi_repeat_schedule_hour, nfi_repeat_schedule_minute, nfi_repeat_schedule_unit, nfi_repeat_schedule_weekly, nfi_volume_policy_bucket_id, nfi_volume_policy_cron_string, nfi_volume_policy_enabled, nfi_volume_policy_nfi_system_id, nfi_volume_policy, pool_id, quota, reservation, read_only, size, snapshot_change_threshold, vol_type, logbook):

    if(name == "none"):
        logbook.ERROR("Volume name is not specified. Skipping volume creation.")
    elif(pool_id == "none"):
        logbook.ERROR("Pool ID is required for creating volume [" + name + "].")
    else:
        blackpearl.createVolume(access_time, case_insensitive, compression, deduplication, name, nfi_repeat_schedule_daily, nfi_repeat_schedule_hour, nfi_repeat_schedule_minute, nfi_repeat_schedule_unit, nfi_repeat_schedule_weekly, nfi_volume_policy_bucket_id, nfi_volume_policy_cron_string, nfi_volume_policy_enabled, nfi_volume_policy_nfi_system_id, nfi_volume_policy, pool_id, quota, reservation, read_only, size, snapshot_change_threshold, vol_type, logbook)

