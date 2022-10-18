from structures.BucketSummary import BucketSummary
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
        for line in output:
            if(isinstance(line, BucketSummary)):
                printBucket(line)
            if(isinstance(line, UserSummary)):
                printUser(line)

def printBucket(line):
    print(line.name + " " + line.data_policy + " " + line.owner + " " + str(line.size))

def printUser(user):
    print(user.name + " " + user.uuid)
