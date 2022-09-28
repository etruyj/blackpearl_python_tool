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
            domain_map[domain.uuid] = domain.name

    return domain_map

def createNameIDMap(domain_list):
    domain_map = {}
    
    if(domain_list != None):
        for domain in domain_list:
            domain_map[domain.name] = domain.uuid

    return domain_map

