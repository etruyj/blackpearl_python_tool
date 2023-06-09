#====================================================================
# PutObject.py
#   Description:
#       Puts an object to the BlackPearl. The object name can be 
#       specified or the path will be used.
#====================================================================

def toBlackPearl(blackpearl, bucket, path, logbook):
    try:
        logbook.INFO("Saving object " + path + " to bucket " + bucket)
        response = blackpearl.putObject(bucket, path, path, logbook)
        return response
    except Exception as e:
        return e.__str__()

def toBlackPearlAndRename(blackpearl, bucket, key, path, logbook):
    try:
        logbook.INFO("Saving object " + path + " as [" + key + "] to bucket " + bucket)
        response = blackpearl.putObject(bucket, key, path, logbook)
        return response
    except Exception as e:
        return e.__str__()
