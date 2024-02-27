#====================================================================
# TapeReport.py
#       Description:
#           Creates a summary report of tapes that can be output to
#           the shell or saved to a file.
#       
#       Provided info:
#           barcode:
#           state:
#           bucket:
#           partition:
#           storage_domain
#           used_space
#
#
#       group_by:
#           none | default:     list of tapes by barcode
#           bucket:             count of tapes by bucket
#           storage_domain:     count of tapes by storage domain
#           state:              
#           tape_type:          count of tapes by tape type
#           tape_partition:     count of tapes by tape partition
#
#       filter_by:
#           none | default:     all tapes are listed
#           blank | scratch:    all scratch tapes
#           bucket:             tapes belonging to a specific bucket
#           in-use | with-data: all tapes with data.
#           storage_domain:     all tapes in storage domain
#           tape_type:          all tapes of type
#           tape_partition:     all tapes in tape partition
#
#       Release notes:
#           Group by and filter by functionality will be phased in.
#           Initial development will be limited.
#====================================================================

import command.ListBuckets as ListBuckets
import command.ListStorageDomainMembers as ListStorageDomainMembers
import command.ListStorageDomains as ListStorageDomains
import command.ListTapePartitions as ListTapePartitions
import command.ListTapes as ListTapes
import util.map.MapBuckets as MapBuckets
import util.map.MapStorageDomains as MapStorageDomains
import util.map.MapTapePartitions as MapTapePartitions

from structures.BucketGroupTapes import BucketGroupTapes
from structures.TapeSummary import TapeSummary
from structures.sdk.Tape import Tape

def createReport(group_by, filter_by, blackpearl, logbook):
    logbook.INFO("Creating tape report...")
    output = []

    # Fetch Required Information
    try:
        tape_list = ListTapes.createList(blackpearl, logbook)
        bucket_list = ListBuckets.createList(blackpearl, logbook)
        par_list = ListTapePartitions.createList(blackpearl, logbook)
        domain_list = ListStorageDomains.createList(blackpearl, logbook)
        member_list = ListStorageDomainMembers.createList(blackpearl, logbook)

        # Error handling.
        # If the bucket list is not actually a list, don't continue to process.
        # The first failure for not enough privileges is list users in the 
        # ListBuckets call.
        if(not isinstance(bucket_list, list)):
            # Pass the error message over to the output.
            output = bucket_list
        else:
            logbook.INFO("Mapping ids to names...")
            bucket_map = MapBuckets.createIDNameMap(bucket_list)
            par_map = MapTapePartitions.createIDNameMap(par_list)
            member_domain_map = MapStorageDomains.createMemberNameMap(domain_list, member_list)

            # Parse Filter By
            params = None
            if(filter_by != None):
                params = filter_by.split(":")

            if(len(params) == 2):
                logbook.INFO("Filtering results by " + str(params[0]) + ":" + str(params[1]))
            else:
                params = None

            # Build List
            if(tape_list != None):
                match group_by:
                    case "bucket":
                        output = listGroupBucket(tape_list, bucket_map, params, logbook)
                    case "storage_domain":
                        output = listGroupStorageDomain(tape_list, bucket_map, params, logbook)
                    case _:
                        logbook.WARN("group-by [" + group_by + "] not supported. Outputing list of all tapes.")
                        output = listAllTapes(tape_list, bucket_map, par_map, member_domain_map, params, logbook)

            else:
                print("No tapes returned from report.")
                logbook.ERROR("No tapes returned from report.")

        return output
    except Exception as e:
        logbook.ERROR(e.__str__())
        return e.__str__()

def filterTape(tape, filter_by):
    #============================================
    # Filters the tape results by the filter by
    # parameters.
    # filter_by[0]: the field to parse.
    # filter_by[1]: the value to parse for
    #
    # if not match is found, null/None value is
    # returned.
    #============================================
    if(filter_by != None):
        match filter_by[0]:
            case "barcode":
                filter_by[1] = str(filter_by[1]).upper()
                if(filter_by[1] in tape.getBarcode()):
                    return tape
            case "state":
                filter_by[1] = filter_by[1].upper()
                if(tape.getState()==filter_by[1]):
                    return tape
            case "status":
                if(filter_by[1] == "blank" or filter_by[1] == "scratch"):
                    if(tape.getStorageDomainMemberId() == None):
                        return tape
                if(filter_by[1] == "in-use" or filter_by[1] == "has-data"):
                    if(tape.getStorageDomainMemberId() != None):
                        return tape
    else:
        # No filter specified.
        # don't filter. Return tape.
        return tape

def findBucketName(bucket, bucket_map, logbook):
    # Override the bucket id with the bucket name
    # if it is present in the map. Otherwise return
    # the bucket ID to the output.
    if(bucket_map != None):
        if(bucket != None):
            if(bucket in bucket_map):
                bucket = bucket_map[bucket]
            else:
                logbook.WARN("Bucket ID [" + bucket + "] not found in bucket list.")

    return bucket

def findStorageDomainName(sdm, member_domain_map, logbook):
    # Overrid the storage domain member id with the storage domain
    # name if it is present in the map. Otherwise return the
    # storage domain member id.
    if(member_domain_map != None):
        if(sdm != None):
            if(sdm in member_domain_map):
                sdm = member_domain_map[sdm]
            else:
                logbook.WARN("Storage Domain Member ID [" + sdm + "] not associated with a storage domain.")
    return sdm

def findTapePartitionName(par_id, par_map, logbook):
    # Override the tape partition id with the tape partition
    # name if it is present in the map. Otherwise return the
    # tape partition id.
    if(par_map != None):
        if(par_id != None):
            if(par_id in par_map):
                par_id = par_map[par_id]
            else:
                logbook.WARN("Tape partition ID [" + par_id + "] not found in partition list.")

    return par_id

def listAllTapes(tape_list, bucket_map, par_map, member_domain_map, filter_by, logbook):
    logbook.INFO("Creating list of all tapes.")
    tsm_list = []

    for tape in tape_list:
        # If filter was specified, filter tape.
        if(filter_by != None):
            tape = filterTape(tape, filter_by)

        # If tape wasn't filtered out, add to list.
        if(tape != None):
            tsm = TapeSummary()

            tsm.setBarcode(tape.getBarcode())
            tsm.setBucket(findBucketName(tape.getBucketId(), bucket_map, logbook))
            tsm.setState(tape.getState())
            tsm.setStorageDomain(findStorageDomainName(tape.getStorageDomainMemberId(), member_domain_map, logbook))
            tsm.setTapeCapacity(tape.getTotalCapacity(), tape.getAvailableCapacity())
            tsm.setTapeType(tape.getTapeType())
            tsm.setTapePartition(findTapePartitionName(tape.getPartitionId(), par_map, logbook))

            tsm_list.append(tsm)

    return tsm_list

def listGroupBucket(tape_list, bucket_map, filter_by, logbook):
    logbook.INFO("Creating list grouped by bucket...");
    tape_map = {}

    # Error handle to make sure there is a list of tapes.
    if(tape_list != None):
        for tape in tape_list:
            if(filter_by != None):
                tape = filterTape(tape, filter_by)

            if(tape != None):
                #Blank tapes
                if(tape.getStorageDomainMemberId() == None):
                    if("scratch" not in tape_map):
                        bgt = BucketGroupTapes()
                        bgt.setBucketName("scratch")
                        bgt.addTapeCapacity(tape.getTotalCapacity(), tape.getAvailableCapacity())
                        bgt.addTape()
                        tape_map["scratch"] = bgt
                    else:
                        bgt = tape_map["scratch"]
                        bgt.addTapeCapacity(tape.getTotalCapacity(), tape.getAvailableCapacity())
                        bgt.addTape()
                        tape_map["scratch"] = bgt

                # Non-bucket isolated tapes
                elif(tape.getBucketId() == None):
                    if("non-isolated" not in tape_map):
                        bgt = BucketGroupTapes()
                        bgt.setBucketName("non-isolated")
                        bgt.addTapeCapacity(tape.getTotalCapacity(), tape.getAvailableCapacity())
                        bgt.addTape()
                        tape_map["non-isolated"] = bgt
                    else:
                        bgt = tape_map["non-isolated"]
                        bgt.addTapeCapacity(tape.getTotalCapacity(), tape.getAvailableCapacity())
                        bgt.addTape()
                        tape_map["non-isolated"] = bgt

                # Bucket isolated tapes
                elif(tape.getBucketId() != None):
                    if(tape.getBucketId() not in tape_map):
                        bgt = BucketGroupTapes()
                        bgt.setBucketName(tape.getBucketId())
                        bgt.addTapeCapacity(tape.getTotalCapacity(), tape.getAvailableCapacity())
                        bgt.addTape()
                        tape_map[tape.getBucketId()] = bgt
                    else:
                        bgt = tape_map[tape.getBucketId()]
                        bgt.addTapeCapacity(tape.getTotalCapacity(), tape.getAvailableCapacity())
                        bgt.addTape()
                        tape_map[tape.getBucketId()] = bgt

                # Default - Failed to parse
                else:
                    logbook.WARN("Unabled to parse tape [" + tape.getBarcode() + "].")

    # Convert Bucket ID to Bucket Name
    # and switch from dictionary to a list.    
    bucket_list = []
    for key in tape_map.keys():
        bgt = tape_map[key]

        # Find bucket name if not a scratch or non-isolated.
        if(key != "scatch" and key != "non-isolated"):
            bgt.setBucketName(findBucketName(bgt.getBucketName(), bucket_map, logbook))

        # Add bgt to list.
        bucket_list.append(bgt)

    return bucket_list

def listGroupStorageDomain(tape_list, bucket_map, filter_by, logbook):
    logbook.INFO("Creating list grouped by bucket...");
    tape_map = {}

    # Error handle to make sure there is a list of tapes.
    if(tape_list != None):
        for tape in tape_list:
            if(filter_by != None):
                tape = filterTape(tape, filter_by)

            if(tape != None):
                #Blank tapes
                if(tape.getStorageDomainMemberId() == None):
                    if("scratch" not in tape_map):
                        bgt = BucketGroupTapes()
                        bgt.setBucketName("scratch")
                        bgt.addTapeCapacity(tape.getTotalCapacity(), tape.getAvailableCapacity())
                        bgt.addTape()
                        tape_map["scratch"] = bgt
                    else:
                        bgt = tape_map["scratch"]
                        bgt.addTapeCapacity(tape.getTotalCapacity(), tape.getAvailableCapacity())
                        bgt.addTape()
                        tape_map["scratch"] = bgt

                # Non-bucket isolated tapes
                elif(tape.getBucketId() == None):
                    if("non-isolated" not in tape_map):
                        bgt = BucketGroupTapes()
                        bgt.setBucketName("non-isolated")
                        bgt.addTapeCapacity(tape.getTotalCapacity(), tape.getAvailableCapacity())
                        bgt.addTape()
                        tape_map["non-isolated"] = bgt
                    else:
                        bgt = tape_map["non-isolated"]
                        bgt.addTapeCapacity(tape.getTotalCapacity(), tape.getAvailableCapacity())
                        bgt.addTape()
                        tape_map["non-isolated"] = bgt

                # Bucket isolated tapes
                elif(tape.getBucketId() != None):
                    if(tape.getBucketId() not in tape_map):
                        bgt = BucketGroupTapes()
                        bgt.setBucketName(tape.getBucketId())
                        bgt.addTapeCapacity(tape.getTotalCapacity(), tape.getAvailableCapacity())
                        bgt.addTape()
                        tape_map[tape.getBucketId()] = bgt
                    else:
                        bgt = tape_map[tape.getBucketId()]
                        bgt.addTapeCapacity(tape.getTotalCapacity(), tape.getAvailableCapacity())
                        bgt.addTape()
                        tape_map[tape.getBucketId()] = bgt

                # Default - Failed to parse
                else:
                    logbook.WARN("Unabled to parse tape [" + tape.getBarcode() + "].")

    # Convert Bucket ID to Bucket Name
    # and switch from dictionary to a list.    
    bucket_list = []
    for key in tape_map.keys():
        bgt = tape_map[key]

        # Find bucket name if not a scratch or non-isolated.
        if(key != "scatch" and key != "non-isolated"):
            bgt.setBucketName(findBucketName(bgt.getBucketName(), bucket_map, logbook))

        # Add bgt to list.
        bucket_list.append(bgt)

    return bucket_list
