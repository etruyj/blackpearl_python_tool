#====================================================================
# ConvertCSV.py
#   Description:
#       Converts script output to a CSV format, including headers.
#       Returns the output as a list for other printing to the shell
#       or to be saved to a file.
#====================================================================

from structures.BucketGroupedJob import BucketGroupedJob
from structures.BucketGroupTapes import BucketGroupTapes
from structures.BucketSummary import BucketSummary
from structures.TapeSummary import TapeSummary
from structures.UserSummary import UserSummary

import util.convert.StorageUnits as StorageUnits

def toOutput(output):
    if(output != None):
        toPrint = []

        # Check for dictionary
        if(type(output) is dict):
            toPrint = convertDict(output)
        # Check to see if the output
        elif(len(output) >= 1):
            if(isinstance(output[0], BucketGroupedJob)):
                toPrint = convertBucketGroupedJob(output)
            if(isinstance(output[0], BucketGroupTapes)):
                toPrint = convertBucketGroupSummary(output)
            if(isinstance(output[0], BucketSummary)):  
                toPrint = convertBucketSummary(output)
            if(isinstance(output[0], TapeSummary)):
                toPrint = convertTapeSummary(output)
            if(isinstance(output[0], UserSummary)):
                toPrint = convertUserSummary(output)

        return toPrint

#================================================
# Converters
#================================================

def convertBucketGroupedJob(output):
    toPrint = []

    # headers
    row = "bucket_name,total_jobs,puts,data_put,gets,data_get"
    toPrint.append(row)

    # Values
    for line in output:
        row = line.getBucket() + ","
        row += str(line.getJobCount()) + ","
        row += str(line.getWriteCount()) + ","
        row += StorageUnits.bytesToHumanReadable(int(line.getDataWrite())) + ","
        row += str(line.getReadCount()) + ","
        row += StorageUnits.bytesToHumanReadable(int(line.getDataRead()))
        toPrint.append(row)

    return toPrint

def convertBucketGroupSummary(output):
    toPrint = []
    
    #headers
    row = "bucket_name,tape_count,available_allocated,used,total_allocated"
    toPrint.append(row)

    #values
    for line in output:
        row = line.getBucketName() + ","
        row += str(line.getTapeCount()) + "," 
        row += StorageUnits.bytesToHumanReadable(int(line.getAvailableCapacity())) + ","
        row += StorageUnits.bytesToHumanReadable(int(line.getUsedCapacity())) + ","
        row += StorageUnits.bytesToHumanReadable(int(line.getTotalCapacity()))
        toPrint.append(row)

    return toPrint

def convertBucketSummary(output):
    toPrint = []
    row = ""

    row = "name,data_policy,owner,size"
    toPrint.append(row)

    for line in output:
        row = line.getName() + "," + line.getDataPolicy() + "," + line.getOwner() + "," + StorageUnits.bytesToHumanReadable(int(line.getSize()))
        toPrint.append(row)

    return toPrint

def convertDict(output):
    headers = []
    toPrint = []

    # Get Headers
    for key in output.keys():
        headers.append(key)

    for i in range(0, len(headers)):
        toPrint.append(str(headers[i]) + "," + str(output[headers[i]]))
        
    return toPrint

def convertTapeSummary(output):
    toPrint = []
    row = ""

    row = "barcode,bucket,tape_partition,storage_domain,state,tape_type,available_capacity,used_capacity,total_capacity"
    toPrint.append(row)

    for line in output:
        row = str(line.getBarcode()) + "," + str(line.getBucket()) + ","
        row += str(line.getTapePartition()) + "," + str(line.getStorageDomain()) + ","
        row += str(line.getState()) + "," + str(line.getTapeType()) + ","
        row += str(StorageUnits.bytesToHumanReadable(int(line.getAvailableCapacity()))) + ","
        row += str(StorageUnits.bytesToHumanReadable(int(line.getUsedCapacity()))) + "," 
        row += str(StorageUnits.bytesToHumanReadable(int(line.getTotalCapacity())))

        toPrint.append(row)

    return toPrint

def convertUserSummary(output):
    toPrint = []
    row = ""

    row = "username,id"
    toPrint.append(row)

    for line in output:
        row = line.getName() + "," + line.getId()
        toPrint.append(row)


