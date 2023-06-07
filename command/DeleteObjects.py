#====================================================================
#   DeleteObjects.py
#       Description:
#           Issues the commands to the BlackPearl to delete objects
#           in a specified list from the specified bucket.
#====================================================================

import util.io.File as File
import os.path

def fromFile(blackpearl, bucket, file, logbook, buffer=1000):
    logbook.INFO("Deleting first " + str(buffer) + " objects specified in " + file + " from " + bucket)

    try:
        while os.path.isfile(file):
            objects = File.partialParse(file, buffer)

            for to_delete in objects:
                print("delete: " + to_delete)

    except Exception as e:
        logbook.ERROR(e.__str__())
        return e.__str__()
