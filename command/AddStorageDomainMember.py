# AddStorageDomainMember.py

def addAnyMember(blackpearl, storage_domain_id, member, tape_par_map, pool_par_map, logbook):
    if(member['partition'] in tape_par_map.keys()):
        # tape copy
        return addTapeMember(blackpearl, storage_domain_id, tape_par_map[member['partition']], member['tape_type'], member['auto_compaction_threshold'], member['write_optimization'], logbook)
    elif(member['partition'] in pool_par_map.keys()):
        # pool copy
        return addDiskMember(blackpearl, storage_domain_id, pool_par_map[member['partition']], member['write_optimization'], logbook)
    else:
        logbook.WARN("Unabled to find storage domain member [" + member['partition'] + "].")
        print("WARNING: Unabled to find storage domain member [" + member['partition'] + "].")


def addDiskMember(blackpearl, storage_domain_id, member_id, write_optimization, logbook):
    return blackpearl.addDiskPartitionToStorageDomain(member_id, storage_domain_id, write_optimization, logbook)

def addTapeMember(blackpearl, storage_domain_id, member_id, tape_type, compaction_threshold, write_optimization, logbook):
    return blackpearl.addTapePartitionToStorageDomain(storage_domain_id, member_id, tape_type, compaction_threshold, write_optimization, logbook)
