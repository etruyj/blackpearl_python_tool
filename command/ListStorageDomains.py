# ListStorageDomains.py

from structures.StorageDomainSummary import StorageDomainSummary
from structures.sdk.StorageDomain import StorageDomain

def createList(blackpearl, logbook):
    logbook.INFO("Creating list of storage domains...")
    logbook.DEBUG("Calling blackpearl.getStorageDomains()...")

    output = []
    domain_list = blackpearl.getStorageDomains(logbook)

    for domain in domain_list:
        dom = StorageDomain()
        dom.setEjectFullThreshold(domain['AutoEjectMediaFullThreshold'])
        dom.setEjectCron(domain['AutoEjectUponCron'])
        dom.setEjectOnCancelled(domain['AutoEjectUponJobCancellation'])
        dom.setEjectOnCompleted(domain['AutoEjectUponJobCompletion'])
        dom.setEjectOnFull(domain['AutoEjectUponMediaFull'])
        dom.setId(domain['Id'])
        dom.setLtfsFileNaming(domain['LtfsFileNaming'])
        dom.setMaxTapeFragmentationPercent(domain['MaxTapeFragmentationPercent'])
        dom.setAutoVerificationFrequency(domain['MaximumAutoVerificationFrequencyInDays'])
        dom.setMediaEjectionAllowed(domain['MediaEjectionAllowed'])
        dom.setName(domain['Name'])
        dom.setSecureMediaAllocation(domain['SecureMediaAllocation'])
        dom.setVerifyPriorToAutoEject(domain['VerifyPriorToAutoEject'])
        dom.setWriteOptimization(domain['WriteOptimization'])

        output.append(dom)

    return output

def createSummaryList(blackpearl, logbook):
    logbook.INFO("Creating list of storage domains...")
    logbook.DEBUG("Calling blackpearl.getStorageDomains()...")

    output = []
    domain_list = blackpearl.getStorageDomains(logbook)

    for domain in domain_list:
        print(domain)
        summary = StorageDomainSummary()
        summary.name = domain['Name']
        summary.uuid = domain['Id']

        output.append(summary)

    return output

