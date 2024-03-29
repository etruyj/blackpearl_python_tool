#====================================================================
#   DeleteObjects.py
#       Description:
#           Issues the commands to the BlackPearl to delete objects
#           in a specified list from the specified bucket.
#====================================================================

import command.PutObject as PutObject
import util.io.File as File
from util.Logger import Logger

import os.path
from datetime import datetime

def createAuditLog(user, bucket):
    date = datetime.now()
    log_path = "../log/audit-nacre-delete-" + date.strftime("%Y-%m-%d_%H-%M-%S") + ".log"
    audit_log = Logger(log_path, "1 GiB", 1, 1)
    audit_log.INFO("User [" + user + "] issued delete-objects command against bucket " + bucket)
    return audit_log

def deleteObjectBatch(blackpearl, bucket, object_list, logbook, audit_log):
    try:
        result = blackpearl.deleteObjects(bucket, object_list, logbook)
    
        # Print failed.
        for error in result["ErrorList"]:
            print(error["Code"] + ": " + error["Key"]) 
        # Store Success
        for success in result["DeletedList"]:
            audit_log.WARN("Batch deleted object: " + success["Key"])

    except Exception as e:
        raise e

def deleteSingleObject(blackpearl, bucket, to_delete, logbook):
    try:
        blackpearl.deleteObject(bucket, to_delete, logbook)
        return True
    except Exception as e:
        if("does not exist" in e.__str__()):
            return False
        else:
            raise e

def fromFile(blackpearl, bucket, file, logbook, user, buffer=1000, ignore_audit_log=False):
    print("WARNING: You are issuing a command to delete multiple objects from the bucket " + bucket + ". These objects cannot be recovered.")
    decision = input("Please type DELETE ALL to delete all objects without prompting or VERIFY to verify each object name before deleting: ")

    if(decision == "VERIFY" or decision == "DELETE ALL"):
        try:
            audit_log = createAuditLog(user, bucket)

            while os.path.isfile(file):
                object_list = File.partialParse(file, buffer)
            
                processDeletes(blackpearl, decision, bucket, object_list, logbook, audit_log)

            if(not ignore_audit_log):
                saveAuditLog(blackpearl, bucket, logbook, audit_log)
        except Exception as e:
            logbook.ERROR(e.__str__())
            return e.__str__()
    else:
        return "Invalid input selected. No objects have been deleted."

def processDeletes(blackpearl, decision, bucket, object_list, logbook, audit_log):
    logbook.INFO("Processing deletes for (" + str(len(object_list)) + ") objects from bucket [" + bucket + "].")
    
    if(decision == "VERIFY"):
        for to_delete in object_list:
            choice = input("Type DELETE to delete " + to_delete + " from bucket " + bucket + ": ")

            if(choice == "DELETE"):
                success = deleteSingleObject(blackpearl, bucket, to_delete, logbook)

                if(success):
                    audit_log.WARN("Deleted object: " + to_delete)
    elif(decision == "DELETE ALL"):
        print("Deleting batch of " + str(len(object_list)) + " objects from bucket [" + bucket + "].")
        deleteObjectBatch(blackpearl, bucket, object_list, logbook, audit_log)

def saveAuditLog(blackpearl, bucket, logbook, audit_log):
    logbook.INFO("Saving audit log to bucket [" + bucket + "]")
    
    log_key = audit_log.getLogPath().split("/")
    log_key = log_key[len(log_key)-1]

    PutObject.toBlackPearlAndRename(blackpearl, bucket, log_key, audit_log.getLogPath(), logbook)

