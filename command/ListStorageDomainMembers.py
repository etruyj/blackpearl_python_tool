#====================================================================
# ListStorageDomainMembers.py
#   Description:
#       Queries the BlackPearl to generate a list of the storage
#       domain members.
#====================================================================

from structures.sdk.StorageDomainMember import StorageDomainMember

def createList(blackpearl, logbook):
    try:
        logbook.INFO("Creating list of storage domain members...")
        logbook.DEBUG("Calling blackpearl.getStorageDomainMembers()")
        output = []

        member_list = blackpearl.getStorageDomainMembers(logbook)

        if(member_list != None):
            for member in member_list:
                sdm = StorageDomainMember()
                sdm.setCompactionThreshold(member['AutoCompactionThreshold'])
                sdm.setId(member['Id'])
                sdm.setPoolPartitionId(member['PoolPartitionId'])
                sdm.setTapePartitionId(member['TapePartitionId'])
                sdm.setState(member['State'])
                sdm.setStorageDomainId(member['StorageDomainId'])
                sdm.setTapeType(member['TapeType'])
                sdm.setWritePreference(member['WritePreference'])

                output.append(sdm)

        return output
    except Exception as e:
        print(e)
        logbook.ERROR(e)
