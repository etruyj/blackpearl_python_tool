#====================================================================
#   StageObject.py
#       Description:
#           This command stages an object from tape to cache.
#====================================================================

def singleObject(bucket, object_name, blackpearl, logbook):
    logbook.INFO("Staging object " + bucket + "/" + object_name)

    try:
        blackpearl.stageObject(bucket, object_name, logbook)
    except Exception as e:
        print(e)
        return e.__str__()
