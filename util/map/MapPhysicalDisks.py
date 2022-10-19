# MapPhysicalDisks.py
#   Creates a dictionary of different data disks based on type and then size.
#   Primary Keys
#       - hdd
#       - ssd
#       - nvme

def createTypeDiskMap(data_disks):
    # Keys [ hdd, ssd, nvme ]
    disk_map = {}
    disk_map['hdd'] = {}
    disk_map['ssd'] = {}
    disk_map['nvme'] = {}

    for disk in data_disks:
        if(disk['speed'] != None):
            # See if the key exists and if not, create it
            # then add the list to the map.
            if(disk['size'] in disk_map['hdd']):
                disk_map['hdd'][disk['size']].append(disk)
            else:
                group = []
                group.append(disk)
                disk_map['hdd'][disk['size']] = group
        else:
            if(disk['size'] in disk_map['nvme']):
                disk_map['nvme'][disk['size']].append(disk)
            else:
                group = []
                group.append(disk)
                disk_map['nvme'][disk['size']] = group

    return disk_map

def groupAvailableDisksByType(disk_list):
    disk_map = {}
    disk_map['hdd'] = []
    disk_map['ssd'] = []
    disk_map['nvme'] = []

    for disk in disk_list:
        if('pool_status' in disk.keys() and disk['pool_status'] == "available"):
            if(disk['speed'] != None):
                disk_map['hdd'].append(disk)
            else:
                # Not sure how to split this out into SDD and NVMe yet.
                # So everything is NVMe.
                disk_map['nvme'].append(disk)

    return disk_map
