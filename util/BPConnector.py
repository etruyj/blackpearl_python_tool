#===================================================================
# BPConnector.py
#   Description:
#       A wrapper class for the ds3 object returned by the SDK
#===================================================================

from ds3 import ds3
from util.Logger import Logger

import util.sdk.SDKCommands as SDKCommands

class BPConnector:
    def __init__(self, endpoint, access_key, secret_key, logbook):
        if(access_key == "none" and secret_key == "none"):
            logbook.INFO("Creating client with environmental variables")
            
            self.client = ds3.createClientFromEnv()
        else:
            logbook.INFO("Creating connection to BlackPearl [" +endpoint + "].")
            logbook.INFO("Using access key " + access_key)

            self.client = ds3.Client(endpoint, ds3.Credentials(access_key, secret_key))


    def verifyConnection(self, logbook):
        try:
            getServiceResponse = self.client.get_service(ds3.GetServiceRequest())
            return True
        except Exception as e:
            if e.code == "InvalidAccessKeyId":
                logbook.ERROR("Invalid access key")
                print("ERROR: Invalid access key.")
            elif e.code == "InvalidSecurity":
                logbook.ERROR("Invalid secret key")
                print("ERROR: Invalid secret key")
            else:
                logbook.ERROR(e.code)
                print(e.code)
            return False

    #================================================================
    # SDK Functions
    #   Calls to the SDK
    #================================================================

    def addDataPersistenceRule(self, data_policy_id, isolation, storage_domain_id, storage_type, days_to_retain, logbook):
        return SDKCommands.createDataPersistenceRule(self.client, data_policy_id, isolation, storage_domain_id, storage_type, days_to_retain, logbook)

    def addDiskPartitionToStorageDomain(self, pool_id, storage_domain_id, write_optimization, logbook):
        return SDKCommands.createStorageDomainPoolMember(self.client, pool_id, storage_domain_id, write_optimization, logbook)

    def addTapePartitionToStorageDomain(self, storage_domain_id, tape_par_id, tape_type, auto_compaction, write_optimization, logbook):
        return SDKCommands.createStorageDomainTapeMember(self.client, storage_domain_id, tape_par_id, tape_type, auto_compaction, write_optimization, logbook)

    def createBucket(self, name, data_policy, owner, logbook):
        return SDKCommands.createBucket(self.client, name, data_policy, owner, logbook)

    def createDataPolicy(self, name, force_puts, min_spanning, blobbing, checksum_type, blob_size, get_priority, put_priority, verify_after_write, verify_priority, end_to_end_crc, versions_to_keep, rebuild_priority, versioning, logbook):
        return SDKCommands.createDataPolicy(self.client, name, force_puts, min_spanning, blobbing, checksum_type, blob_size, get_priority, put_priority, verify_after_write, verify_priority, end_to_end_crc, versions_to_keep, rebuild_priority, versioning, logbook)

    def createStorageDomain(self, name, auto_eject_threshold, auto_eject_cron, auto_eject_cancellation, auto_eject_on_completion, auto_eject_on_full, ltfs_file_naming, verification_frequency_days, auto_compaction_threshold, media_ejection_allowed, secure_media_allocation, verify_prior_to_eject, write_optimization, logbook):
        return SDKCommands.createStorageDomain(self.client, name, auto_eject_threshold, auto_eject_cron, auto_eject_cancellation, auto_eject_on_completion, auto_eject_on_full, ltfs_file_naming, verification_frequency_days, auto_compaction_threshold, media_ejection_allowed, secure_media_allocation, verify_prior_to_eject, write_optimization, logbook)
    
    def getBuckets(self, logbook):
        return SDKCommands.getBuckets(self.client, logbook)

    def getBucketInfo(self, bucket, logbook):
        return SDKCommands.getBucketInfo(self.client, bucket, logbook)

    def getBucketNames(self, logbook):
        return SDKCommands.getBucketNames(self.client, logbook)

    def getDataPolicies(self, logbook):
        return SDKCommands.getDataPolicies(self.client, logbook)

    def getDiskPartitions(self, logbook):
        return SDKCommands.getDiskPartitions(self.client, logbook)

    def getStorageDomains(self, logbook):
        return SDKCommands.getStorageDomains(self.client, logbook)

    def getTapePartitions(self, logbook):
        return SDKCommands.getTapePartitions(self.client, logbook)

    def getUsers(self, logbook):
        return SDKCommands.getUsers(self.client, logbook)
