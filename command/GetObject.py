#=====================================================================
# GetObject.py
#   Description:
#       Downloads the specified object from the bucket. If no destination
#       is specified, the object will be written to the ~/Downloads folder
#       using the specified file name.
#=====================================================================

import os.path

def toLocation(blackpearl, bucket, key, destination, logbook):
    logbook.INFO("Downloading file [" + key + "] from bucket [" + bucket + "]...")

    try:
        if(destination == None or destination == ""):
            destination = "~/Downloads/" + key
            destination = os.path.expanduser(destination)
            logbook.INFO("No destination file specified. Saving object to " + destination);

        blackpearl.getObject(bucket, key, destination, logbook)

        return "File saved to " + destination
    except Exception as e:
        raise e


