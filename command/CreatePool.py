# Create Pool

from structures.NasPool import NasPool
import util.map.MapPhysicalDisks as MapPhysicalDisks

def assignDisks(disk_map, drive_count, stripes, parity, logbook):
    logbook.INFO("Finding disks for pool...")

    disk_type = "not specified"
    drives_assigned = 0
    drives_per_stripe = drive_count / stripes
    drives_in_stripe = 0
    stripe = 0

    pool = NasPool(parity, stripes) # pools initialize with a single stripe.
    
    # Determine type of disks to use
    # A disk type can be specified or 
    # if not, it defaults to hdd.
    if(pool.getPreferredDiskType() != "none"):
        pref_type = pool['preferred_disk_type']
        
        if(len(disk_map[pref_type] >= drive_count)):
            logbook.INFO("Enough drives of the specified type [" + pool['prefered_disk_type'] + "] exist to create the pool. Using those disks.")
            disk_type = pref_type

    if(disk_type == "not specified"):
        logbook.INFO("preferred_disk_type not specified for pool. Searching available disks.")
        if(len(disk_map['hdd']) >= drive_count):
            logbook.INFO("Enough hard drives are available (" + str(len(disk_map['hdd'])) + ") to create pool. Setting disk_type to 'hdd'.")
            disk_type = "hdd"
        elif(len(disk_map['ssd']) >= drive_count):
            logbook.INFO("Enough solid state drives are available (" + str(len(disk_map['ssd'])) + ") to create pool. Setting disk_type to 'ssd'.")
            disk_type = "ssd"
        elif(len(disk_map['nvme']) >= drive_count):
            logbook.INFO("Enough NVMe drives are available (" + str(len(disk_map['nvme'])) + ") to create pool. Setting disk_type to 'nvme'.")
            disk_type = "nvme"
        else:
            logbook.WARN("Not enough drives are available to create pool.")
            disk_type = "none"
        
    if(disk_type != "none"):
        for disk in disk_map[disk_type]:
            if(stripe < stripes):
                pool.addDiskToStripe(stripe, disk['id'], disk['size'], "disk")
                drives_in_stripe += 1
                drives_assigned += 1
                
                if(drives_in_stripe == drives_per_stripe):
                    # Next Stripe
                    drives_in_stripe = 0
                    stripe += 1
                    # Check to make sure we don't create a blank
                    # stripe at the end of the list.
                    if(drives_assigned < drive_count):
                        pool.addStripeToTopology(parity)


    if(drives_assigned == drive_count):
        # Drives assigned successfully.
        pool.calcSizes()
        return pool
    else:
        # Unabled to assign drives to pool
        logbook.WARN("Unabled to assign drives to pool. Cancelling pool creation.")
        print("WARNING: Unabled to assign drives to pool. Cancelling pool creation.")
        return None

def buildPool(blackpearl, pool, logbook):
    # Get an updated list of available Data Disks for each pool
    # I haven't figured out an easier way to track this yet.
    logbook.DEBUG("Calling blackpearl.getDataDisks()...")
    disk_list = blackpearl.getDataDisks(logbook)
    logbook.DEBUG("Calling MapPhysicalDisks.groupAvailableDisksByType()...")
    disk_map = MapPhysicalDisks.groupAvailableDisksByType(disk_list)


    if('name' not in pool.keys()):
        logbook.WARN("No name specified for pool. Skipping pool creation.")
    elif('stripes' not in pool.keys()):
        logbook.WARN("Missing required parameter 'stripes' for pool [" + pool['name'] + "]");
    else:
        logbook.INFO("Creating pool [" + pool['name'] + "]...")
        
        if('power_saving_mode' not in pool.keys()):
            logbook.WARN("Power saving mode not set for pool [" + pool['name'] + "]. Setting to disabled.")
            print("WARNING: Power saving mode not set for pool [" + pool['name'] + "]. Setting to disabled.")
            pool['power_saving_mode'] = "disabled"

        pool_settings = assignDisks(disk_map, pool['drive_count'], pool['stripes'], pool['protection_level'], logbook)

        if(pool_settings != None):
            pool_settings.setName(pool['name'])
            pool_settings.setPowerMode(pool['power_saving_mode'])
            pool_settings.setType(pool['type'])

            if('type' in pool.keys()):
                if(pool['type'] == "nas"):
                    logbook.DEBUG("Calling blackpearl.createNASPool()...")
                    
                    return blackpearl.createNASPool(pool_settings, logbook)
                else:
                    logbook.WARN("Unrecognized pool type [" + pool['type'] + "].")
                    print("WARNING: Unrecognized pool type [" + pool['type'] + "].")
            else:
                logbook.WARN("Pool type not set for pool [" + pool['name'] + "]. Unable to create pool.")
                print("WARNING: Pool type not set for pool [" + pool['name'] + "]. Unable to create pool.")
