#====================================================================
# ListTapes.py
#   Description:
#       Provides a list of tapes in the blackpearl.
#====================================================================

import command.ListBuckets as ListBuckets
import command.ListTapePartitions as ListTapePartitions
import util.map.MapBuckets as MapBuckets
import util.map.MapTapePartitions as MapTapePartitions

from structures.raw.Tape import Tape

def allTapes(blackpearl, logbook):
    logbook.INFO("Creating list of tapes...")
    logbook.DEBUG("Calling blackpearl.getAllTapes()")
    output = []

    tape_list = blackpearl.getTapesAll(logbook)

    # Getting buckets to map names to Id
    logbook.INFO("Mapping bucket IDs to names...")
    bucket_list = ListBuckets.createList(blackpearl, logbook)
    bucket_map = MapBuckets.createIDNameMap(bucket_list)

    logbook.INFO("Mapping tape partition IDs to names...")
    par_list = ListTapePartitions.all(blackpearl, logbook)
    par_map = MapTapePartitions.createIDNameMap(par_list)

    logbook.INFO("Mapping storage domain IDs to names...")

    if(tape_list == None):
        eprint("Unable to retreive tape list")
        logbook.ERROR("Unable to retrieve tape list")
    else:
        for tape in tape_list:
            tape_info = Tape()
            
            print(tape)

            tape_info.setAssignedToStorageDomain(tape['AssignedToStorageDomain'])
            tape_info.setAvailableCapacity(tape['AvailableRawCapacity'])
            tape_info.setBarcode(tape['BarCode'])
            
            tape_info.setBucketId(tape['BucketId'])

            tape_info.setBucketName("")
            if(bucket_map != None):
                if(tape['BucketId'] != None):
                    if(tape['BucketId'] in bucket_map):
                        tape_info.setBucketName(bucket_map[tape['BucketId']])
                    else:
                        logbook.WARN("Unabled to find bucket name for ID [" + tape['BucketId'] + "].")
                else:
                    logbook.WARN("Tape [" + tape['BarCode'] + "] is not assigned to a bucket.")
            else:
                logbook.WARN("No buckets found.")

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
            
            if(par_map != None):
                if(tape['PartitionId'] != None):
                    if(tape['PartitionId'] in par_map):
                        tape_info.setPartitionName(tape['PartitionId'])
                    else:
                        logbook.WARN("Unable to find tape partition [" + tape['PartitionId'] + "].")
                        tape_info.setPartitionName("")
                else:
                    logbook.WARN("Tape [" + tape['BarCode'] + "] is not assigned to a partition.")
                    tape_info.setPartitionName("")
            else:
                logbook.WARN("No partitions found.")
                tape_info.setPartitionName("")

            tape_info.setPreviousState(tape['PreviousState'])
            tape_info.setSerialNumber(tape['SerialNumber'])
            tape_info.setState(tape['State'])
            tape_info.setStorageDomainId(tape['StorageDomainMemberId'])

            # Set Storage Domain Name

            tape_info.setTakeOwnershipPending(tape['TakeOwnershipPending'])
            tape_info.setTotalRawCapacity(tape['TotalRawCapacity'])
            tape_info.setType(tape['Type'])
            tape_info.setVerifyPending(tape['VerifyPending'])
            tape_info.setWriteProtected(tape['WriteProtected'])

            output.append(tape_info)

    return output
