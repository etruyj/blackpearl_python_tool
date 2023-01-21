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

from structures.KeyPair import KeyPair
from structures.TapeSummary import TapeSummary
from structures.sdk.Tape import Tape

def createReport(group_by, filter_by, blackpearl, logbook):
    logbook.INFO("Creating tape report...")
    output = []

    # Fetch Required Information
    tape_list = ListTapes.createList(blackpearl, logbook)
    bucket_list = ListBuckets.createList(blackpearl, logbook)
    par_list = ListTapePartitions.createList(blackpearl, logbook)
    domain_list = ListStorageDomains.createList(blackpearl, logbook)
    member_list = ListStorageDomainMembers.createList(blackpearl, logbook)

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
            case _:
                output = listAllTapes(tape_list, bucket_map, par_map, member_domain_map, params, logbook)

    else:
        print("No tapes returned from report.")
        logbook.ERROR("No tapes returned from report.")

    return output

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
            tsm.setTapeType(tape.getTapeType())
            tsm.setTapePartition(findTapePartitionName(tape.getPartitionId(), par_map, logbook))

            tsm_list.append(tsm)

    return tsm_list

def listGroupBucket(tape_list, bucket_map, filter_by, logbook):
    logbook.INFO("Creating list grouped by bucket...");
    tape_map = {}

    if(tape_list != None):
        # Set the headers
        tape_map["bucket"] = "tape_count"

        for tape in tape_list:
            if(filter_by != None):
                tape = filterTape(tape, filter_by)

            if(tape != None):
                #Blank tapes
                if(tape.getStorageDomainMemberId() == None):
                    if("scratch" not in tape_map):
                        tape_map["scratch"] = 1
                    else:
                        tape_map["scratch"] = tape_map["scratch"] + 1
                # Non-bucket isolated tapes
                elif(tape.getBucketId() == None):
                    if("non-isolated" not in tape_map):
                        tape_map["non-isolated"] = 1
                    else:
                        tape_map["non-isolated"] = tape_map["non-isolated"] + 1
                # Bucket isolated tapes
                elif(tape.getBucketId() != None):
                    if(tape.getBucketId() not in tape_map):
                        tape_map[tape.getBucketId()] = 1
                    else:
                        tape_map[tape.getBucketId()] = tape_map[tape.getBucketId()] + 1
                # Default - Failed to parse
                else:
                    logbook.WARN("Unabled to parse tape [" + tape.getBarcode() + "].")

    # Convert Bucket ID to Bucket Name
    # 1. Get headers
    headers = []
    for key in tape_map.keys():
        headers.append(key)

    # 2. Replace bucket id with bucket_name
    # 3. Delete bucket_id value. There is risk of deleting a
    #   bucket_id if the bucket name isn't found in the list.
    for i in range(0, len(headers)):
        if(not (headers[i] == "scratch" or headers[i] == "non-isolated" or headers[i] == "bucket")):
            tape_map[findBucketName(headers[i], bucket_map, logbook)] = tape_map[headers[i]]
            del tape_map[headers[i]]

    return tape_map
