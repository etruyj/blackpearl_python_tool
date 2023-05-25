# CreateDiskPartition.py

def verifyThenCreate(blackpearl, disk_par, logbook):
    
    if(disk_par['name'] == None):
        print("ERROR: No disk partition name specified.")
        logbook.ERROR("No disk partition name specified.")
    elif(disk_par['type'] == None):
        print("ERROR: No disk partition name specified.")
        logbook.ERROR("No disk partition name specified.")
    elif(not(disk_par['type'] == "nearline" or disk_par['type'] == "online")):
        print("ERROR: Invalid partition specified. Requires type: 'nearline' or 'online'.")
        logbook.ERROR("Invalid partition type [" + disk_par['type'] + "] specified.")
    else:
        return blackpearl.createDiskPartition(disk_par['name'], disk_par['type'], logbook)
