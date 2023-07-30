#====================================================================
#   StageObject.py
#       Description:
#           This command stages an object from tape to cache.
#====================================================================

import util.io.File as File

def fromList(bucket, file_name, blackpearl, logbook):
    logbook.INFO("Staging objects listed in " + file_name)

    try:
        object_list = File.load(file_name)
        logbook.INFO("List contains (" + str(len(object_list)) + ") objects.")
        blackpearl.stageObject(bucket, object_list, logbook)

        return "Staging (" + str(len(object_list)) + ") objects command sent."
    except Exception as e:
        logbook.ERROR(e.__str__())
        return e.__str__()


def singleObject(bucket, object_name, blackpearl, logbook):
    logbook.INFO("Staging object " + bucket + "/" + object_name)

    try:
        blackpearl.stageObject(bucket, object_name, logbook)
    except Exception as e:
        print(e)
        return e.__str__()
