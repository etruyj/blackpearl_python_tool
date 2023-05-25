#====================================================================
#   MapTapePartitions.py
#       Description:
#           Creates a dictionary of [String, String] to map tape
#           partition names to ids and vice versa.
#====================================================================

from structures.sdk.TapePartition import TapePartition

def createIDNameMap(par_list):
    par_map = {}

    if(par_list != None):
        for par in par_list:
            par_map[par.getPartitionId()] = par.getName()
    else:
        print("No par list")

    return par_map

def createNameIDMap(par_list):
    par_map = {}

    if(par_list != None):
        for par in par_list:
            par_map[par.getName()] = par.getPartitionId()

    return par_map

