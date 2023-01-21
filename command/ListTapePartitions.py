#====================================================================
# ListTapeParititons.py
#       Description:
#           Provides a list of Tape Partitions
#====================================================================

from structures.sdk.TapePartition import TapePartition

def createList(blackpearl, logbook):
    logbook.INFO("Retrieving list of tape partitions")
    logbook.DEBUG("Calling blackpearl.getTapePartitions()")
    output = []

    par_list = blackpearl.getTapePartitions(logbook)
    
    if(par_list != None):
        for par in par_list:
            partition = TapePartition()

            partition.setAutoCompaction(par['AutoCompactionEnabled'])
            partition.setAutoQuiesce(par['AutoQuiesceEnabled'])
            partition.setDriveIdleTimeout(par['DriveIdleTimeoutInMinutes'])
            partition.setDriveType(par['DriveType'])
            partition.setErrorMessage(par['ErrorMessage'])
            partition.setPartitionId(par['Id'])
            partition.setImportExportConfig(par['ImportExportConfiguration'])
            partition.setLibraryId(par['LibraryId'])
            partition.setMinReadReserve(par['MinimumReadReservedDrives'])
            partition.setMinWriteReserve(par['MinimumWriteReservedDrives'])
            partition.setName(par['Name'])
            partition.setQuiesced(par['Quiesced'])
            partition.setSerialNumber(par['SerialNumber'])
            partition.setState(par['State'])

            output.append(partition)
           
        return output
    else:
        logbook.WARN("No tape partitions found.")
