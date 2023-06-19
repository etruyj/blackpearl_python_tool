#====================================================================
# ListTapes.py
#   Description:
#       Provides a list of tapes in the blackpearl.
#====================================================================

from structures.sdk.Tape import Tape

def createList(blackpearl, logbook):
    logbook.INFO("Creating list of tapes...")
    logbook.DEBUG("Calling blackpearl.getAllTapes()")
    output = []

    tape_list = blackpearl.getTapesAll(logbook)

    if(tape_list == None):
        eprint("Unable to retreive tape list")
        logbook.ERROR("Unable to retrieve tape list")
    else:
        for tape in tape_list:
            tape_info = Tape()
           
            tape_info.setAssignedToStorageDomain(tape['AssignedToStorageDomain'])
            tape_info.setAvailableCapacity(tape['AvailableRawCapacity'])
            tape_info.setBarcode(tape['BarCode'])
            tape_info.setBucketId(tape['BucketId'])
            tape_info.setDescription(tape['DescriptionForIdentification'])
            tape_info.setEjectDate(tape['EjectDate'])
            tape_info.setEjectLabel(tape['EjectLabel'])
            tape_info.setEjectLocation(tape['EjectLocation'])
            tape_info.setEjectPending(tape['EjectPending'])
            tape_info.setFullOfData(tape['FullOfData'])
            tape_info.setId(tape['Id'])
            tape_info.setLastAccessed(tape['LastAccessed'])
            tape_info.setLastCheckpoint(tape['LastCheckpoint'])
            tape_info.setLastModified(tape['LastModified'])
            tape_info.setLastVerified(tape['LastVerified'])
            tape_info.setPartiallyVerifiedEndOfTape(tape['PartiallyVerifiedEndOfTape'])
            tape_info.setPartitionId(tape['PartitionId'])
            tape_info.setPreviousState(tape['PreviousState'])
            tape_info.setSerialNumber(tape['SerialNumber'])
            tape_info.setState(tape['State'])
            tape_info.setStorageDomainId(tape['StorageDomainMemberId'])
            tape_info.setTakeOwnershipPending(tape['TakeOwnershipPending'])
            tape_info.setTotalRawCapacity(tape['TotalRawCapacity'])
            tape_info.setType(tape['Type'])
            tape_info.setVerifyPending(tape['VerifyPending'])
            tape_info.setWriteProtected(tape['WriteProtected'])

            output.append(tape_info)

    return output
