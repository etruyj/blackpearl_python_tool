#====================================================================
# ConvertTable.py
#       Description:
#           Converts the output to a table format.
#====================================================================

from structures.BucketGroupTapes import BucketGroupTapes
from structures.BucketSummary import BucketSummary
from structures.TapeSummary import TapeSummary
from structures.UserSummary import UserSummary

import util.convert.StorageUnits as StorageUnits

def toOutput(output):
    toPrint = []
    tables = []

    if(output != None):
        if(type(output) is dict):
            tables = loadDict(output)
        elif(len(output) >= 1):
            if(isinstance(output[0], BucketGroupTapes)):
                tables = loadBucketGroupSummary(output)
            if(isinstance(output[0], BucketSummary)):
                tables = loadBucketSummary(output)
            if(isinstance(output[0], TapeSummary)):
                tables = loadTapeSummary(output)
            if(isinstance(output[0], UserSummary)):
                print("add code")

    if(tables != None):
        toPrint = buildTable(tables)

    return toPrint

#================================================
# Functions
#================================================

def buildTable(table):
    toPrint = []
    row = ""

    if(len(table) >= 1):
        # Determine the number of rows
        # Initial set-up
        column_count = len(table[0])
        column_size = []

        for i in range(0, column_count):
            column_size.append(0)

        # Determine the max column size
        for y in range(0, len(table)):
            for x in range(0, column_count):
                if(len(str(table[y][x])) > column_size[x]):
                    column_size[x] = len(str(table[y][x]))
        
        for i in range(0, len(table)):
            toPrint.append(buildRowSeparator(column_size))
            toPrint.append(buildRow(table[i], column_size))

        toPrint.append(buildRowSeparator(column_size))

        return toPrint

        
def buildRowSeparator(column_size):
    row = ""
    for i in range(0, len(column_size)):
        row += "+"
        for d in range(0, column_size[i] + 2):
            row += "-"

    row += "+"

    return row

def buildRow(fields, column_size):
    row = "|"

    for i in range(0, len(column_size)):
        row += " " + str(fields[i])
        
        # Add spaces to fill in box
        for n in range(len(str(fields[i])), column_size[i] + 1):
            row += " "

        row += "|"

    return row

def loadBucketGroupSummary(output):
    table = []
    row = []

    # Load Table Headers
    row.append("bucket name")
    row.append("tape count")
    row.append("available allocated")
    row.append("used")
    row.append("total allocated")
    table.append(row)

    # Load Values
    for bucket in output:
        row = []
        row.append(bucket.getBucketName())
        row.append(bucket.getTapeCount())
        row.append(StorageUnits.bytesToHumanReadable(int(bucket.getAvailableCapacity())))
        row.append(StorageUnits.bytesToHumanReadable(int(bucket.getUsedCapacity())))
        row.append(StorageUnits.bytesToHumanReadable(int(bucket.getTotalCapacity())))
        table.append(row)
    
    return table


def loadBucketSummary(output):
    table = []
    row = []

    # Load Table Headers
    row.append("name")
    row.append("data policy")
    row.append("owner")
    row.append("size")
    table.append(row)

    # Load Values
    for bucket in output:
        row = []
        row.append(bucket.getName())
        row.append(bucket.getDataPolicy())
        row.append(bucket.getOwner())
        row.append(StorageUnits.bytesToHumanReadable(int(bucket.getSize())))
        table.append(row)

    return table


def loadDict(output):
    table = []
    headers = []

    for key in output.keys():
        headers.append(key)

    for i in range(0, len(headers)):
        row = []
        row.append(headers[i])
        row.append(output[headers[i]])
        table.append(row)

    return table

def loadTapeSummary(output):
    table = []

    # Build Table Headers
    row = []
    row.append("barcode")
    row.append("bucket")
    row.append("tape partition")
    row.append("storage domain")
    row.append("state")
    row.append("tape type")
    row.append("available capacity")
    row.append("used capacity")
    row.append("total capacity")
    table.append(row)

    # Fill values
    for tape in output:
        row = []
        row.append(tape.getBarcode())
        row.append(tape.getBucket())
        row.append(tape.getTapePartition())
        row.append(tape.getStorageDomain())
        row.append(tape.getState())
        row.append(tape.getTapeType())
        row.append(StorageUnits.bytesToHumanReadable(int(tape.getAvailableCapacity())))
        row.append(StorageUnits.bytesToHumanReadable(int(tape.getUsedCapacity())))
        row.append(StorageUnits.bytesToHumanReadable(int(tape.getTotalCapacity())))

        table.append(row)

    return table
