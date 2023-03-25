#====================================================================
# ListCompletedJobs.py
#   Description:
#       Provides a list of completed jobs.
#====================================================================

from structures.sdk.Job import Job

def createList(blackpearl, logbook):
    logbook.INFO("Creating list of completed jobs...")
    logbook.DEBUG("Calling blackpearl.getCompletedJobs()...")

    output = []
    
    try:
        job_list = blackpearl.getCompletedJobs(logbook)

        if(job_list == None):
            logbook.ERROR("Null value returned for job list.")
            raise Exception("Unable to retrieve job list.")
        else:
            for job in job_list:
                job_info = Job()

                job_info.setBucketId(job['BucketId'])
                job_info.setCachedSize(job['CachedSizeInBytes'])
                job_info.setChunkProcessingOrder(job['ChunkClientProcessingOrderGuarantee'])
                job_info.setCompletedSize(job['CompletedSizeInBytes'])
                job_info.setCreatedAt(job['CreatedAt'])
                job_info.setDateCompleted(job['DateCompleted'])
                job_info.setErrorMessage(job['ErrorMessage'])
                job_info.setId(job['Id'])
                job_info.setNaked(job['Naked'])
                job_info.setName(job['Name'])
                job_info.setOriginalSize(job['OriginalSizeInBytes'])
                job_info.setPriority(job['Priority'])
                job_info.setRechunked(job['Rechunked'])
                job_info.setRequestType(job['RequestType'])
                job_info.setTruncated(job['Truncated'])
                job_info.setUserId(job['UserId'])

                output.append(job_info)

            return output

    except Exception as e:
        logbook.ERROR(e.__str__())
        print(e)
