#====================================================================
#   MapStorageDomains.py
#       Description:
#           Creates a dictionary of [String, String] to determine
#           domain name from id and domain id from name.
#====================================================================

from structures.StorageDomainSummary import StorageDomainSummary

def createIDNameMap(domain_list):
    domain_map = {}

    if(domain_list != None):
        for domain in domain_list:
            domain_map[domain.getId()] = domain.getName()

    return domain_map

def createNameIDMap(domain_list):
    domain_map = {}
    
    if(domain_list != None):
        for domain in domain_list:
            domain_map[domain.getName()] = domain.getId()

    return domain_map

def createMemberNameMap(domain_list, member_list):
    # create a map of storage domain member id to storage domain name
    member_name_map = {}

    domain_map = createIDNameMap(domain_list)

    if(domain_map != None and member_list != None):
        for member in member_list:
            if(member.getDomainId() in domain_map):
                member_name_map[member.getMemberId()] = domain_map[member.getDomainId()]
            else:
                member_name_map[member.getMemberId()] = member.getDomainId()

    return member_name_map

