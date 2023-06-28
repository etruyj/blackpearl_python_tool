#====================================================================
# LimitBucketSize.py
#   Description:
#       This command enforces size limits on BlackPearl buckets. The
#       sizes are specified in the configuration file. When this
#       command executes, it checks the bucket against the max size
#       specified in the file. If the size is larger than the
#       sizee specified, it makes all ACLs read-only.
#   
#   Requirements:
#       - user access to the bucket has to be granted via ACLs. The
#           users cannot have global ACL access to all buckets.
#
#   Main Function: test(option,blackpearl,logbook)
#====================================================================

import command.ListBuckets as ListBuckets
import command.ReadOnlyBucket as ReadOnlyBucket
import util.Configuration as Configuration
import util.convert.StorageUnits as StorageUnits

def test(option, blackpearl, logbook):
    try:
        logbook.INFO("Checking bucket size limits.")

        bucket_limits = getBucketLimits(logbook)

        if(bucket_limits == None or len(bucket_limits) < 1):
            message = "Nothing to do. No outstanding bucket size limits to enact."
            logbook.INFO(message)
            return message
        else:
            out_of_policy = outOfPolicyBuckets(bucket_limits, blackpearl, logbook)
            if(len(out_of_policy) > 0):
                enforceLimits(out_of_policy, blackpearl, logbook)
                updateConfig(out_of_policy, bucket_limits, logbook)

    except Exception as e:
        logbook.ERROR(e.__str__())
        return e.__str__()

def enforceLimits(out_of_policy, blackpearl, logbook):
    logbook.INFO("Enforcing bucket policy limits...")

    try:
        for bucket in out_of_policy:
            ReadOnlyBucket.configureAcls(bucket, blackpearl, logbook)
    except Exception as e:
        raise e

def getBucketLimits(logbook):
    try:
        logbook.INFO("Fetching config.")
        config = Configuration.load()
        bucket_limits = None

        for doc in config:
            if('bucket_size_limits' in doc):
                bucket_limits = doc['bucket_size_limits']

        return bucket_limits
    except Exception as e:
        if(e.__str__() == "'NoneType' object is not iterable"):
            logbook.ERROR(e.__str__())
            raise Exception("Configuration file not found.")

def outOfPolicyBuckets(bucket_limits, blackpearl, logbook):
    try:
        logbook.INFO("Checking to see if any buckets are out of policy")
        bucket_list = ListBuckets.createList(blackpearl, logbook)
        out_of_policy = []

        for bucket in bucket_limits:
            if('triggered' not in bucket or bucket['triggered'] == False):
                searching = True
                counter = 0
                limit_in_bytes = StorageUnits.humanReadableToBytes(bucket['limit'])
                
                while(searching and counter < len(bucket_list)):
                    if(bucket['bucket'] == bucket_list[counter].getName()):
                        if(int(bucket_list[counter].getSize()) > limit_in_bytes):
                            out_of_policy.append(bucket['bucket'])
                        searching = False
                    counter += 1

        logbook.INFO("Found (" + str(len(out_of_policy)) + ") out of policy buckets.")
        return out_of_policy
    except Exception as e:
        raise e

def updateConfig(out_of_policy, bucket_limits, logbook):
    try:
        logbook.INFO("Updating config file...")
        for bucket in out_of_policy:
            searching = True
            counter = 0

            while(searching and counter < len(bucket_limits)):
                if(bucket_limits[counter]['bucket'] == bucket):
                    bucket_limits[counter]['triggered'] = True
                    searching = False
                
                counter += 1

        Configuration.update("bucket_size_limits", bucket_limits)

    except Exception as e:
        raise e
