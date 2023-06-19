#====================================================================
#   MapDiskPartitions.py
#       Description:
#           Creates a dictionary of [String, String] to determine
#           disk partition name from id and disk partition id from name.
#====================================================================

def createIDNameMap(partitions):
    par_map = {}

    if(partitions != None):
        for partition in partitions:
            par_map[partition['Id']] = partition['Name']

    return par_map

def createNameIDMap(partitions):
    par_map = {}
    
    if(partitions != None):
        for partition in partitions:
            par_map[partition['Name']] = partition['Id']

    return par_map

