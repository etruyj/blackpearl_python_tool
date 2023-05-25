#====================================================================
#   MapPools.py
#       Description:
#           Creates a dictionary of [String, String] to determine
#           pool name from id and pool id from name.
#====================================================================

def createIDNameMap(pools):
    pool_map = {}

    if(pools != None):
        for pool in pools:
            pool_map[pool['id']] = pool['name']

    return pool_map

def createNameIDMap(pools):
    pool_map = {}
    
    if(pools != None):
        for pool in pools:
            pool_map[pool['name']] = pool['id']

    return pool_map

