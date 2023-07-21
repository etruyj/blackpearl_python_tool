#====================================================================
#   StageObjects.py
#       Description:
#           These commands are used to stage objects from tape to
#           disk in order to streamline the restore process.
#====================================================================

from ds3 import ds3

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
