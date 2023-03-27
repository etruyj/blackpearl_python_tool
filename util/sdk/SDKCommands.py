#====================================================================
# SDKCommands.py
#       Description:
#           The basic SDK commands that are used for the script's
#           commands.
#====================================================================

from ds3 import ds3
from util.Logger import Logger

def createBucket(blackpearl, name, data_policy, owner, logbook):
    try:
        logbook.INFO("Creating bucket [" + name + "]...")
        logbook.DEBUG("blackpearl.put_bucket_spectra_s3()...")

        # ds3.PutBucketSpectraS3Request(bucket_name, data_policy_id, id=?, owner)
        #   not sure what the id field is. Can you specifiy the bucket id when creating the bucket?
        createBucketResponse = blackpearl.put_bucket_spectra_s3(ds3.PutBucketSpectraS3Request(name, data_policy, None, owner))

        return createBucketResponse
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform put-bucket")
        else:
            raise Exception("Failed to create bucket [" + name + "].")

def createDataPersistenceRule(blackpearl, data_policy_id, isolation, storage_domain_id, storage_type, minimum_days, logbook):
    try:
        logbook.INFO("Adding data persistence rule [domain: " + storage_domain_id + " to data_policy_id [" + data_policy_id + "]")
        logbook.DEBUG("blackpearl.put_data_persistence_rule_spectra_s3(" + data_policy_id + ", " + isolation + ", " + storage_domain_id + ", " + storage_type + ", " + str(minimum_days) + ")...")

        createPersistenceRule = blackpearl.put_data_persistence_rule_spectra_s3(ds3.PutDataPersistenceRuleSpectraS3Request(data_policy_id, isolation, storage_domain_id, storage_type, minimum_days))

        return createDataPersistenceRule
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform put-data-persistence-rule")
        else:
            raise Exception("Failed to add data persistene rule to data policy.")

def createDataPolicy(blackpearl, name, force_puts, min_spanning, blobbing, checksum_type, blob_size, get_priority, put_priority, verify_after_write, verify_priority, end_to_end_crc, versions_to_keep, rebuild_priority, versioning, logbook):
    try:
        logbook.INFO("Creating data policy [" + name + "]...")
        logbook.DEBUG("blackpearl.put_data_policy_spectra_s3()...")
        
        createPolicyResponse = blackpearl.put_data_policy_spectra_s3(ds3.PutDataPolicySpectraS3Request(name, force_puts, min_spanning, blobbing, checksum_type, blob_size, get_priority, put_priority, verify_after_write, verify_priority, end_to_end_crc, versions_to_keep, rebuild_priority, versioning))

        return createPolicyResponse.result
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform put-data-policy")
        else:
            raise Exception("Failed to create data policy [" + name + "].")

def createDiskPartition(blackpearl, name, partition_type, logbook):
    try:
        logbook.INFO("Creating disk partition [" + name + "]...");
        logbook.DEBUG("blackpearl.put_pool_partition_spectra_s3()...");

        if(partition_type == "nearline" or partition_type == "online"):
            createDiskPartitionResponse = blackpearl.put_pool_partition_spectra_s3(ds3.PutPoolPartitionSpectraS3Request(name, partition_type))

            return createDiskPartitionResponse
        else:
            logbook.ERROR("Invalid partition type [" + partition_type + "] specified.")

    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform put-disk-partition")
        else:
            raise Exception("Failed to create disk partition [" + name + "].")

def createStorageDomain(blackpearl, name, auto_eject_threshold, auto_eject_cron, auto_eject_cancellation, auto_eject_on_completion, auto_eject_on_full, ltfs_file_naming, verification_frequency_days, auto_compaction_threshold, media_ejection_allowed, secure_media_allocation, verify_prior_to_eject, write_optimization, logbook):
    try:
        logbook.INFO("Creating storage domain [" + name + "]...")
        logbook.DEBUG("blackpearl.put_storage_domain_spectra_s3()...")
        
        createStorageDomain = blackpearl.put_storage_domain_spectra_s3(ds3.PutStorageDomainSpectraS3Request(name, auto_eject_threshold, auto_eject_cron, auto_eject_cancellation, auto_eject_on_completion, auto_eject_on_full, ltfs_file_naming, verification_frequency_days, auto_compaction_threshold, media_ejection_allowed, secure_media_allocation, verify_prior_to_eject, write_optimization))

        return createStorageDomain.result
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform put-storage-domain")
        else:
            raise Exception("Unable to create storage domain [" + name + "].")

def createStorageDomainPoolMember(blackpearl, pool_id, storage_domain_id, write_optimization, logbook):
    try:
        logbook.INFO("Adding pool partition to storage domain...")
        logbook.DEBUG("blackpearl.put_pool_storage_domain_member_spectra_s3_request()...")

        createPoolMember = blackpearl.put_pool_storage_domain_member_spectra_s3(ds3.PutPoolStorageDomainMemberSpectraS3Request(pool_id, storage_domain_id, write_optimization))

        return createPoolMember
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform put-storage-domain-member")
        else:
            raise Exception("Unable to add pool partition [" + pool_id + "] to storage domain.")

def createStorageDomainTapeMember(blackpearl, storage_domain_id, tape_par_id, tape_type, auto_compaction_threshold, write_preference, logbook):
    try:
        logbook.INFO("Adding tape partition to storage domain...")
        logbook.DEBUG("blackpearl.put_tape_storage_domain_member_spectra_s3()...")

        createTapeMember = blackpearl.put_tape_storage_domain_member_spectra_s3(ds3.PutTapeStorageDomainMemberSpectraS3Request(storage_domain_id, tape_par_id, tape_type, auto_compaction_threshold, write_preference))

        return createTapeMember
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform modify-storage-domain")
        else:
            raise Exception("Unabled to add tape partition [" + tape_par_id + "] to storage domain.")


def getBuckets(blackpearl, logbook):
    try:
        logbook.INFO("Fetching bucket names.")
        logbook.DEBUG("blackpear.get_buckets_spectra_s3()")
        
        getBucketsResponse = blackpearl.get_buckets_spectra_s3(ds3.GetBucketsSpectraS3Request())

        logbook.INFO("Found (" + str(len(getBucketsResponse.result['BucketList'])) + ") buckets.")
        
        return getBucketsResponse.result['BucketList']

    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform list-buckets")
        else:
            raise Exception("Unable to retrieve bucket list.")

def getBucketInfo(blackpearl, name, logbook):
    try:
        logbook.INFO("Fetching details on bucket [" + name + "]")
        logbook.DEBUG("blackpearl.get_bucket_spectra_s3(" + name + ")")
        getBucketResponse = blackpearl.get_bucket_spectra_s3(ds3.GetBucketSpectraS3Request(name))

        print(vars(getBucketResponse))
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform get-bucket-info")
        else:
            raise Exception("Unable to retrieve bucket info.")

def getBucketNames(blackpearl, logbook):
    try:
        logbook.INFO("Fetching bucket names.")
        logbook.DEBUG("blackpear.get_service()")
        
        getServiceResponse = blackpearl.get_service(ds3.GetServiceRequest())
        logbook.INFO("BUCKET QUERY") 
        logbook.INFO("Found " + str(len(getServiceResponse.result['BucketList'])) + " buckets.")

        return getServiceResponse.result['BucketList']

    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform list-buckets")
        else:
            raise Exception("Unable to retrieve bucket list.")

def getCompletedJobs(blackpearl, logbook):
    try:
        logbook.INFO("Fetching completed jobs...")
        logbook.DEBUG("Calling blackpearl.get_completed_jobs_spectra_s3()...")

        getCompletedJobs = blackpearl.get_completed_jobs_spectra_s3(ds3.GetCompletedJobsSpectraS3Request())

        logbook.INFO("Found (" + str(len(getCompletedJobs.result['CompletedJobList'])) + ") completed jobs.")

        return getCompletedJobs.result['CompletedJobList']
    except Exception as e:
        print(e)

def getDataPolicies(blackpearl, logbook):
    try:
        logbook.INFO("Fetching data policies...")
        logbook.DEBUG("Calling blackpearl.get_data_policies_spectra_s3()...")

        getDataPolicies = blackpearl.get_data_policies_spectra_s3(ds3.GetDataPoliciesSpectraS3Request())

        logbook.INFO("Found (" + str(len(getDataPolicies.result['DataPolicyList'])) + ") data policies.")

        return getDataPolicies.result['DataPolicyList']
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform list-data-policies")
        else:
            raise Exception("Unable to retrieve data policies.")

def getDiskPartitions(blackpearl, logbook):
    try:
        logbook.INFO("Fetching disk partitions...")
        logbook.DEBUG("Calling blackpearl.get_pool_partitions_spectra_s3()...")

        getDiskPartitions = blackpearl.get_pool_partitions_spectra_s3(ds3.GetPoolPartitionsSpectraS3Request())

        return getDiskPartitions.result['PoolPartitionList']
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform list-disk-partitions")
        else:
            raise Exception("Unable to retrieve disk partitions.")

def getPools(blackpearl, logbook):
    try:
        logbook.INFO("Fetching pools...")
        logbook.DEBUG("Calling blackpearl.get_pools_spectra_s3()...")

        getPools = blackpearl.get_pools_spectra_s3(ds3.GetPoolsSpectraS3Request())

        print("utils/sdk/SDKCommands.py: " + vars(getPools))
        return getPools.result
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform list-pools")
        else:
            raise Exception("Unable to retrieve disk pools.")

def getStorageDomainMembers(blackpearl, logbook):
    try:
        logbook.INFO("Fetching storage domain members...")
        logbook.DEBUG("Calling blackpearl.get_storage_domain_members_spectra_s3()")

        getStorageDomainMembers = blackpearl.get_storage_domain_members_spectra_s3(ds3.GetStorageDomainMembersSpectraS3Request())

        logbook.INFO("Found (" + str(len(getStorageDomainMembers.result['StorageDomainMemberList'])) + ") storage domain members.")

        return getStorageDomainMembers.result['StorageDomainMemberList']
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform list-storage-domain-members")
        else:
            raise Exception("Unable to retrieve storage domain members.")

def getStorageDomains(blackpearl, logbook):
    try:
        logbook.INFO("Fetching storage domains...")
        logbook.DEBUG("Calling blackpearl.get_storage_domains_spectra_s3()...")

        getStorageDomains = blackpearl.get_storage_domains_spectra_s3(ds3.GetStorageDomainsSpectraS3Request())

        logbook.INFO("Found (" + str(len(getStorageDomains.result['StorageDomainList'])) + ") storage domains.")

        return getStorageDomains.result['StorageDomainList']
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform list-storage-domains")
        else:
            raise Exception("Unable to retrieve storage domains.")

def getTapePartitions(blackpearl, logbook):
    try:
        logbook.INFO("Fetching tape partition information..")
        logbook.DEBUG("Calling blackpearl.get_tape_partitions_spectra_s3()...")

        getTapePartitions = blackpearl.get_tape_partitions_spectra_s3(ds3.GetTapePartitionsSpectraS3Request())

        logbook.INFO("Found (" + str(len(getTapePartitions.result['TapePartitionList'])) + ") tape partitions.")

        return getTapePartitions.result['TapePartitionList']
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform list-tape-partitions")
        else:
            raise Exception("Unable to retrieve tape partition information")

def getTapesAll(blackpearl, logbook):
    try:
        logbook.INFO("Fetchin all tapes managed by BlackPearl...")
        logbook.DEBUG("blackpearl.get_tapes_spectra_s3()...")

        getTapesResponse = blackpearl.get_tapes_spectra_s3(ds3.GetTapesSpectraS3Request())

        logbook.INFO("Found (" + str(len(getTapesResponse.result['TapeList'])) + ") tapes")

        return getTapesResponse.result['TapeList']
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform list-tapes")
        else:
            raise Exception("Unable to retrieve tape list.")

def getUsers(blackpearl, logbook):
    try:
        logbook.INFO("Fetching user list...")
        logbook.DEBUG("blackpearl.get_users_spectra_s3()")

        getUsersResponse = blackpearl.get_users_spectra_s3(ds3.GetUsersSpectraS3Request())

        logbook.INFO("Found (" + str(len(getUsersResponse.result['UserList'])) + ") users.")

        return getUsersResponse.result['UserList']
    except Exception as e:
        logbook.ERROR(e.__str__())
        
        if("AccessDenied" in e.__str__()):
            raise Exception("Access Denied: User does not have permission to perform list-users")
        else:
            raise Exception("Unable to retrieve user list.")
