# Create Pool

from structures.NasPool import NasPool

def assignDisks(disk_list, drive_count, stripes, parity, logbook):
    logbook.INFO("Finding disks for pool...")

    drives_assigned = 0
    drives_per_stripe = drive_count / stripes
    drives_in_stripe = 0
    stripe = 0

    pool = NasPool(parity, stripes) # pools initialize with a single stripe.
    
    for disk in disk_list:
        if(stripe < stripes and disk['pool_status'] != None):
            if(disk['pool_status'] == "available"):
                print(disk['physical_path'] + " " + disk['pool_status'])

                pool.addDiskToStripe(stripe, disk['physical_path'], disk['size'], "data")
                drives_in_stripe += 1
                drives_assigned += 1

                disk['pool_status'] = "pending"
                if(drives_in_stripe == drives_per_stripe):
                    print("next stripe")
                    # Next Stripe
                    drives_in_stripe = 0
                    stripe += 1
                    pool.addStripeToTopology("data")

    if(drives_assigned == drive_count):
        # Drives assigned successfully.
        pool.calcSizes()
        return pool
    else:
        # Unabled to assign drives to pool
        logbook.WARN("Unabled to assign drives to pool. Cancelling pool creation.")
        print("WARNING: Unabled to assign drives to pool. Cancelling pool creation.")
        return None

def buildPool(blackpearl, pool, disk_list, logbook):
    
    if('name' not in pool.keys()):
        logbook.WARN("No name specified for pool. Skipping pool creation.")
    else:
        logbook.INFO("Creating pool [" + pool['name'] + "]...")
        
        if('power_saving_mode' not in pool.keys()):
            logbook.WARN("Power saving mode not set for pool [" + pool['name'] + "]. Setting to disabled.")
            print("WARNING: Power saving mode not set for pool [" + pool['name'] + "]. Setting to disabled.")
            pool['power_saving_mode'] = "disabled"

        pool = assignDisks(disk_list, pool['drive_count'], pool['stripes'], pool['protection_level'], logbook)

        if(pool != None):
            pool.setName(pool['name'])
            pool.setPowerMode(pool['power_saving_mode'])

            logbook.DEBUG("Calling blackpearl.createPool()...")
            return blackpearl.createPool(pool, logbook)
