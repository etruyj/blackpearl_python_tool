# ListStorageDomains.py

from structures.StorageDomainSummary import StorageDomainSummary

def createList(blackpearl, logbook):
    logbook.INFO("Creating list of storage domains...")
    logbook.DEBUG("Calling blackpearl.getStorageDomains()...")

    output = []
    domain_list = blackpearl.getStorageDomains(logbook)

    for domain in domain_list:
        summary = StorageDomainSummary()
        summary.name = domain['Name']
        summary.uuid = domain['Id']

        output.append(summary)

    return output

