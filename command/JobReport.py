#====================================================================
# JobReport.py
#   Description:
#       Compiles job information in order to create a report
#====================================================================

import command.ListBuckets as ListBuckets
import command.ListCompletedJobs as ListCompletedJobs
import util.convert.ConvertIds as ConvertIds
import util.map.MapBuckets as MapBuckets

from structures.BucketGroupedJob import BucketGroupedJob
from structures.sdk.Job import Job

from datetime import datetime, timedelta, timezone

def createReport(blackpearl, filter_by, logbook):
    logbook.INFO("Creating job report...")
    output = []

    try:
        job_list = ListCompletedJobs.createList(blackpearl, logbook)
        bucket_list = ListBuckets.createList(blackpearl, logbook)

        # Error hanlding.
        # If the bucket list is not actually a list, don't continue the process.
        if(not isinstance(bucket_list, list)):
            # Pass the error message over to the output.
            output = bucket_list
        else:
            logbook.INFO("Mapping ids to names...")
            bucket_map = MapBuckets.createIDNameMap(bucket_list)
            
            # Filter Params
            params = None
            if(filter_by != None):
                params = filter_by.split(":")

            # Build List
            if(job_list != None):
                output = listGroupBucket(job_list, bucket_map, params, logbook)

        return output

    except Exception as e:
        logbook.ERROR(e.__str__())
        return e.__str__()
        
def filterJob(job, filter_by):
    # Find the oldest reference time by subtracting days or hours off now()
    # must be converted to a timezone aware format hence the now(timezone.utc).astimezone()
    # if oldest time < job_time, job occured before the filter range.
    if(filter_by[0] == "hours"):
        oldest_time = datetime.now(timezone.utc).astimezone() - timedelta(hours=int(filter_by[1]))
    if(filter_by[0] == "days"):
        oldest_time = datetime.now(timezone.utc).astimezone() - timedelta(days=int(filter_by[1]))
   
    job_time = datetime.strptime(job.getDateCompleted(), "%Y-%m-%dT%H:%M:%S.%f%z")

    if(oldest_time == None):
        # Invalid filter
        return job
    elif(oldest_time < job_time):
        # Job occured older than the oldest time.
        return job

def listGroupBucket(job_list, bucket_map, filter_by, logbook): #job list, bucket_map, filter, logbook
    logbook.INFO("Creating list grouped by bucket...")
    grouped_jobs = []
    job_map = {}
    new_buckets = 0

    # Error handling to make sure there is a list of jobs
    if(job_list != None):
        for job in job_list:
            if(filter_by != None and len(filter_by) > 1):
                job = filterJob(job, filter_by)

            if(job != None):
                # Check to see if the bucket has been found already
                # if not create a new
                if(job.getBucketId() not in job_map):
                    bgj = BucketGroupedJob()
                    new_buckets += 1
                    bgj.setBucket(job.getBucketId())
                
                    if(job.getRequestType() == "PUT"):
                        bgj.addJobWrite()
                        bgj.addDataWritten(job.getCompletedSize())
                    elif(job.getRequestType() == "GET"):
                        bgj.addJobRead()
                        bgj.addDataRead(job.getCompletedSize())
                    
                    job_map[job.getBucketId()] = bgj
                else:
                    bgj = job_map[job.getBucketId()]
                   
                    if(job.getRequestType() == "PUT"):
                        bgj.addJobWrite()
                        bgj.addDataWritten(job.getCompletedSize())
                    elif(job.getRequestType() == "GET"):
                        bgj.addJobRead()
                        bgj.addDataRead(job.getCompletedSize())

                    job_map[job.getBucketId()] = bgj

    # Convert map to list
    for key in job_map.keys():
        bgj = job_map[key]
        bgj.setBucket(ConvertIds.findName(bgj.getBucket(), bucket_map, "bucket", logbook))
        grouped_jobs.append(bgj)
   
    return grouped_jobs


