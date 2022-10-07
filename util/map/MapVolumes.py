#====================================================================
#   MapVolumes.py
#       Description:
#           Creates a dictionary of [String, String] to determine
#           volume name from id and volume id from name.
#====================================================================

def createIDNameMap(volumes):
    vol_map = {}

    if(volumes != None):
        for volume in volumes:
            vol_map[volume['id']] = volume['name']

    return vol_map

def createNameIDMap(volumes):
    vol_map = {}
    
    if(volumes != None):
        for volume in volumes:
            vol_map[volume['name']] = volume['id']

    return vol_map

