#====================================================================
# JobReport.py
#   Description:
#       Compiles job information in order to create a report
#====================================================================

import commandListBuckets as ListBuckets
import commandListCompletedJobs as ListCompletedJobs
import util.map.MapBuckets as MapBuckets

from structures.BucketGroupedJob import BucketGroupedJob
from structures.sdk.Job import Job

def createReport(blackpearl, logbook):
    logbook.INFO("Creating job report...")
    output = []

    try:
        job_list = ListCompletedJobs.createList(blackpearl, logbook)
        bucket_list = ListBuckets.createList(blackpearl, logbook)

        logbook.INFO("Mapping ids to names...")


def listGroupBucket(): #job list, bucket_map, filter, logbook
    print("HERE")
