from structures.BucketSummary import BucketSummary
from structures.TapeSummary import TapeSummary
from structures.UserSummary import UserSummary

import os

def fileContents(path):
    if(os.path.exists(path)):
        f = open(path)
        print(f.read())
        f.close()

    else:
        print("Error [" + path + "] does not exist.")

def output(output):
    if(output != None):
        if(type(output) is dict):
            printDict(output)
        else:
            for line in output:
                if(isinstance(line, BucketSummary)):
                    printBucket(line)
                if(isinstance(line, TapeSummary)):
                    printTape(line)
                if(isinstance(line, UserSummary)):
                    printUser(line)
            

def printBucket(line):
    print(line.name + " " + line.data_policy + " " + line.owner + " " + str(line.size))

def printDict(output):
    headers = []
    line = ""
    
    # Get headers
    for key in output.keys():
        headers.append(key)


    # Print Headers
    #for i in range(0, len(headers)):
    #    line += line + str(headers[i])

    #    if(i<(len(headers) - 1)):
    #       line += line + ","

    #print(line)
    
    for i in range(0, len(headers)):
           print(headers[i] + "," + str(output[headers[i]]))

def printTape(tape):
    print(tape.getBarcode() + "," + str(tape.getBucket()) + "," + str(tape.getTapePartition()) + "," + str(tape.getStorageDomain()) + "," + str(tape.getState()))

def printUser(user):
    print(user.name + " " + user.uuid)
