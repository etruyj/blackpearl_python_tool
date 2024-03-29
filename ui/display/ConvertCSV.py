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
from structures.ObjectSummary import ObjectSummary
from structures.TapeSummary import TapeSummary
from structures.UserSummary import UserSummary
from structures.sdk.Ds3Object import Ds3Object

import util.convert.StorageUnits as StorageUnits

def toOutput(output, include_headers):
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
            if(isinstance(output[0], ObjectSummary)):
                toPrint = convertObjectSummary(output)
            if(isinstance(output[0], Ds3Object)):
                toPrint = convertDs3Object(output)
            if(isinstance(output[0], TapeSummary)):
                toPrint = convertTapeSummary(output)
            if(isinstance(output[0], UserSummary)):
                toPrint = convertUserSummary(output)

        # Delete headers if not included.
        if(not include_headers):
            toPrint.pop(0)

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

def convertDs3Object(output):
    toPrint = []
    row = ""

    # column headers
    row = "object_name,size,owner,last_modified,version_id,is_latest,storage_class,etag"
    toPrint.append(row)

    for obj in output:
        row = obj.getKey() + "," + StorageUnits.bytesToHumanReadable(int(obj.getSize())) + "," + obj.getOwnerDisplayName() + "," + obj.getLastModified() + "," + obj.getVersionId() + "," + obj.getIsLatest() + "," + obj.getStorageClass() + "," + obj.getEtag()

        toPrint.append(row)

    return toPrint

def convertObjectSummary(output):
    toPrint = []
    headers = "name"
    row = ""

    for obj in output:
        row = obj.getName() 

        if(obj.getId() != None):
            headers = headers + ",id"
            row = row + "," + obj.getId()
        if(obj.getBucketName() != None):
            headers = headers + ",bucket_name"
            row = row + "," + obj.getBucketName()
        if(obj.getSize() != None):
            headers = headers + ",size"
            row = row + "," + obj.getSize()
        if(obj.getInCache() != None):
            headers = headers + ",in_cache"
            
            if(obj.getInCache()):
                row = row + ",y"
            else:
                row = row + ",n"
        if(obj.getOwner() != None):
            headers = headers + ",owner"
            row = row + "," + obj.getOwner()
        if(obj.getCreationDate() != None):
            headers = headers + ",creation_date"
            row = row + "," + obj.getCreationDate()
        if(obj.getTapes() != None):
            headers = headers + ",barcode"
            row = row + ","

            for i in range(0, obj.getTapeCount()):
                row = row + obj.getTape(i) + " "

            row = row[:-1] # strip last space from line.
        if(obj.getEtag() != None):
            headers = headers + ",etag"
            row = row + "," + obj.getEtag()

        if(len(toPrint) == 0):
            toPrint.append(headers)
        
        toPrint.append(row)
        headers = ""

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


