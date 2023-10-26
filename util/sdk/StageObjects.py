#====================================================================
#   StageObjects.py
#       Description:
#           These commands are used to stage objects from tape to
#           disk in order to streamline the restore process.
#====================================================================

from ds3 import ds3

def fromList(bucket, object_list, blackpearl, log):
    try:
        stage_list = []

        # Build the object list
        for obj in object_list:
            log.DEBUG("Staging object " + bucket + "/" + obj)
            stage_object = ds3.Ds3GetObject(obj)
            log.DEBUG("ds3.Ds3GetObject.name: [" + str(stage_object.name) + "]")
            stage_list.append(stage_object)

        log.INFO("Issuing stage command for (" + str(len(stage_list)) + ") objects in bucket " + bucket)
        log.DEBUG("blackpearl.stage_objects_job_spectra_s3()")

        response = blackpearl.stage_objects_job_spectra_s3(ds3.StageObjectsJobSpectraS3Request(bucket, stage_list))

    except Exception as e:
        log.ERROR(e.__str__())

        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform stage-objects for bucket " + bucket)
        elif("codec can't encode character" in e.__str__()):
            raise Exception("Access Denied: Attempted to connect to wrong interface.")
        elif("Could not find requested blobs" in e.__str__()):
            obj = e.__str__().split("blobs for: ")[1] # Parse for failed objects
            raise Exception("Failed to stage object(s): " + obj)
        elif("MediaOnliningRequired" in e.__str__()):
            tapes = e.__str__().split("Online: ")[1] # Parse for required tapes
            raise Exception("Failed to stage objects: Media onlining required. Please insert tape(s) " + tapes)
        else:
            raise Exception("Failed to stage objects.")

def singleObject(bucket, object_name, blackpearl, log):
    log.INFO("Issuing staging command for " + bucket + "/" + object_name)
    log.DEBUG("blackpearl.stage_objects_job_spectra_s3()")

    try:
        object_list = []
        stage_object = ds3.Ds3GetObject(object_name)
        object_list.append(stage_object)
        response = blackpearl.stage_objects_job_spectra_s3(ds3.StageObjectsJobSpectraS3Request(bucket, object_list))

        print(response.result)
    except Exception as e:
        print(e)
