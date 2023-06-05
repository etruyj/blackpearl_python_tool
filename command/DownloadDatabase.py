#====================================================================
# DownloadDatabase.py
#   Description:
#       A script to query the BlackPearl and download a database 
#       backup.
#====================================================================

import command.GetObject as GetObject
import command.ListObjects as ListObjects
import structures.sdk.Ds3Object as Ds3Object

import os.path
from datetime import datetime
from datetime import timezone

def mostRecent(blackpearl, file_prefix, file_name, logbook):
    logbook.INFO("Downloading most recent database backup...")

    try:
        database_bucket = findDatabaseBucket(blackpearl, logbook)
        logbook.DEBUG("Calling ListObjects.createList(" + database_bucket + ")...")
        database_backups = ListObjects.createList(database_bucket, blackpearl, logbook)
        database_file = findDatabaseObject(database_backups, logbook)
        if(database_file != None):
            file_name = prepFileName(file_prefix, file_name, database_file, logbook)
            response = GetObject.toLocation(blackpearl, database_bucket, database_file, file_name, logbook)
        
            return response
        else:
            message = "Unable to file database file"
            logbook.WARN(message)
            return message
    except Exception as e:
        logbook.ERROR(e.__str__())
        return e.__str__()

#================================================
# INTERNAL FUNCTIONS
#================================================

def findDatabaseBucket(blackpearl, logbook):
    try:
        hardware = blackpearl.cases(logbook)
        hostname = None
        serial_number = None

        for system in hardware:
            if system["type"] == "server":
                serial_number = system["serial_number"]
                hostname = system["name"]

        if(serial_number != None):
            return "Spectra-BlackPearl-Backup-" + str(hostname) + "-" + str(serial_number)

    except Exception as e:
        raise e

def findDatabaseObject(database_list, logbook):
    logbook.INFO("Searching for most recent database...")
    
    most_recent_db = None
    most_recent_db_time = None
    test_time = None

    try:
        for database in database_list:
            test_time = datetime.fromisoformat(database.getLastModified()[:-1]).astimezone(timezone.utc)

            if(most_recent_db_time == None):
                most_recent_db = database.getKey()
                most_recent_db_time = test_time
            else:
                # Check if test_time happened after the most recent time
                # if so, the test_time becomes the most recent time and
                # the database object is the most recent database.
                if(test_time > most_recent_db_time):
                    most_recent_db = database.getKey()
                    most_recent_db_time = test_time

        logbook.INFO("The most recent database backup is " + most_recent_db)
        return most_recent_db
    except Exception as e:
        logbook.ERROR(e.__str__())
        raise e.__str__()

def prepFileName(file_prefix, file_path, database_file, logbook):
    # Converts the file path for the database to a file_name.
    if(".tar.xz" in file_path):
        logbook.DEBUG("Full file path specified. Will save database to " + file_path)
    else:
        if(file_path == None or file_path == ""):
            logbook.DEBUG("Setting base path to Downloads directory.")
            file_path = os.path.expanduser("~/Downloads")
        
        # Add the trailing slash if not present.
        if(file_path[-1] != "/" and file_path[-1] != "\\"):
            logbook.DEBUG("Adding terminating slash to path.")
            file_path += "/"

        if(not(file_prefix == None or file_prefix == "")):
            logbook.DEBUG("Added prefix to path.")
            file_path += file_prefix + "-"

        file_path += database_file

        logbook.DEBUG("Will save database to " + file_path)

    return file_path
