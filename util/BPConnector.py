#===================================================================
# BPConnector.py
#   Description:
#       A wrapper class for the ds3 object returned by the SDK
#===================================================================

from ds3 import ds3
from util.Logger import Logger

import util.http.HttpCommands as HttpCommands
import util.sdk.SDKCommands as SDKCommands

class BPConnector:
    def __init__(self, endpoint, username, password, access_key, secret_key, logbook):
        # Determine if the connection information is valid.
        self.validConnection = True

        if(username != "none" and password != "none"):
            self.managementPathAuthentication(endpoint, username, password, logbook)

            self.retrieveDataPathParameters(endpoint, username, logbook)
        
            # Save this for verifying connectivity.
            self.management_path = endpoint
        else:
            self.dataPathAuthentication(endpoint, access_key, secret_key, logbook)

    def dataPathAuthentication(self, endpoint, access_key, secret_key, logbook):
        logbook.INFO("Accessing data path...")
        if(access_key == "none" and secret_key == "none"):
            logbook.INFO("Creating client with environmental variables")
        
            self.data_path_client = ds3.createClientFromEnv()
        else:
            logbook.INFO("Creating connection to BlackPearl [" +endpoint + "].")
            logbook.INFO("Using access key " + access_key)

            self.data_path_client = ds3.Client(endpoint, ds3.Credentials(access_key, secret_key))
        
    def managementPathAuthentication(self, endpoint, username, password, logbook):
        logbook.INFO("Accessing management path...")
        self.token =  self.authenticate(endpoint, username, password, logbook)

        # Verify the connection
        if(self.token == "none"):
            self.validConnection = False

    def retrieveDataPathParameters(self, endpoint, username, logbook):
        logbook.INFO("Searching for data path credentials...")

        data_path = HttpCommands.getDataPathIP(endpoint, self.token, logbook)
        keys = HttpCommands.findDs3Credentials(endpoint, self.token, username, logbook)

        self.dataPathAuthentication(data_path, keys['access_key'], keys['secret_key'], logbook)

    def verifyDataConnection(self, logbook):
        try:
            getServiceResponse = self.data_path_client.get_service(ds3.GetServiceRequest())
            return True
        except Exception as e:
            if(e.code == "InvalidAccessKeyId"):
                logbook.ERROR("Invalid access key.")
                print("ERROR: Invalid access key.")
            elif(e.code == "InvalidSecurity"):
                logbook.ERROR("Invalid secret key.")
                print("ERROR: Invalid secret key.")
            else:
                logbook.ERROR(e.code)
                print(e.code)
            
            return False

    def verifyManagementConnection(self, logbook):
        try:
            test = HttpCommands.getNetworkInterfaces(self.management_path, self.token, logbook)

            if(test != None):
                return True
            else:
                logbook.ERROR("Unable to connect to management path.")
                return False
        except Exception as e:
            logbook.ERROR("Failed to validate connection to management path.")
            print(e)
            print("ERROR: Failed to validate connection to management path.")

    #===============================================================
    # HTTP Functions
    #   HTTP Calls to the Management Path
    #===============================================================

    def addActivationKey(self, key, logbook):
        return HttpCommands.addActivationKey(self.management_path, self.token, key, logbook)

    def authenticate(self, url, username, password, logbook):
        return HttpCommands.authenticate(url, username, password, logbook)

    def createCifsShare(self, name, path, volume_id, readonly, service_id, logbook):
        return HttpCommands.createCifsShare(self.management_path, self.token, name, path, volume_id, readonly, service_id, logbook)

    def createNfsShare(self, comment, volume, mount_point, path, access_control, service_id, logbook):
        return HttpCommands.createNfsShare(self.management_path, self.token, comment, volume, mount_point, path, access_control, service_id, logbook)

    def createPool(self, pool, logbook):
        return HttpCommands.createPool(self.management_path, self.token, pool, logbook)

    def createVailShare(self, name, service_id, volume_id, logbook):
        return HttpCommands.createVailShare(self.management_path, self.token, name, service_id, volume_id, logbook)

    def createVolume(self, access_time, case_insensitive, compression, deduplication, name, nfi_repeat_schedule_daily, nfi_repeat_schedule_hour, nfi_repeat_schedule_minute, nfi_repeat_schedule_unit, nfi_repeat_schedule_weekly, nfi_volume_policy_bucket_id, nfi_volume_policy_cron_string, nfi_volume_policy_enabled, nfi_volume_policy_nfi_system_id, nfi_volume_policy, pool_id, quota, reservation, read_only, size, snapshot_change_threshold, vol_type, logbook):
        return HttpCommands.createVolume(self.management_path, self.token, access_time, case_insensitive, compression, deduplication, name, nfi_repeat_schedule_daily, nfi_repeat_schedule_hour, nfi_repeat_schedule_minute, nfi_repeat_schedule_unit, nfi_repeat_schedule_weekly, nfi_volume_policy_bucket_id, nfi_volume_policy_cron_string, nfi_volume_policy_enabled, nfi_volume_policy_nfi_system_id, nfi_volume_policy, pool_id, quota, reservation, read_only, size, snapshot_change_threshold, vol_type, logbook)


    def getDataDisks(self, logbook):
        return HttpCommands.getDataDisks(self.management_path, self.token, logbook)

    def getServices(self, logbook):
        # Literally get services
        # Not DS3_JAVA_CLI's get_services
        return HttpCommands.getServices(self.management_path, self.token, logbook)

    def getNASPools(self, logbook):
        return HttpCommands.getPools(self.management_path, self.token, logbook)

    def getVolumes(self, logbook):
        return HttpCommands.getVolumes(self.management_path, self.token, logbook)

    #================================================================
    # SDK Functions
    #   Calls to the SDK
    #================================================================

    def addDataPersistenceRule(self, data_policy_id, isolation, storage_domain_id, storage_type, days_to_retain, logbook):
        return SDKCommands.createDataPersistenceRule(self.data_path_client, data_policy_id, isolation, storage_domain_id, storage_type, days_to_retain, logbook)

    def addDiskPartitionToStorageDomain(self, pool_id, storage_domain_id, write_optimization, logbook):
        return SDKCommands.createStorageDomainPoolMember(self.data_path_client, pool_id, storage_domain_id, write_optimization, logbook)

    def addTapePartitionToStorageDomain(self, storage_domain_id, tape_par_id, tape_type, auto_compaction, write_optimization, logbook):
        return SDKCommands.createStorageDomainTapeMember(self.data_path_client, storage_domain_id, tape_par_id, tape_type, auto_compaction, write_optimization, logbook)

    def createBucket(self, name, data_policy, owner, logbook):
        return SDKCommands.createBucket(self.data_path_client, name, data_policy, owner, logbook)

    def createDataPolicy(self, name, force_puts, min_spanning, blobbing, checksum_type, blob_size, get_priority, put_priority, verify_after_write, verify_priority, end_to_end_crc, versions_to_keep, rebuild_priority, versioning, logbook):
        return SDKCommands.createDataPolicy(self.data_path_client, name, force_puts, min_spanning, blobbing, checksum_type, blob_size, get_priority, put_priority, verify_after_write, verify_priority, end_to_end_crc, versions_to_keep, rebuild_priority, versioning, logbook)

    def createDiskPartition(self, name, partition_type, logbook):
        return SDKCommands.createDiskPartition(self.data_path_client, name, partition_type, logbook)

    def createStorageDomain(self, name, auto_eject_threshold, auto_eject_cron, auto_eject_cancellation, auto_eject_on_completion, auto_eject_on_full, ltfs_file_naming, verification_frequency_days, auto_compaction_threshold, media_ejection_allowed, secure_media_allocation, verify_prior_to_eject, write_optimization, logbook):
        return SDKCommands.createStorageDomain(self.data_path_client, name, auto_eject_threshold, auto_eject_cron, auto_eject_cancellation, auto_eject_on_completion, auto_eject_on_full, ltfs_file_naming, verification_frequency_days, auto_compaction_threshold, media_ejection_allowed, secure_media_allocation, verify_prior_to_eject, write_optimization, logbook)
    
    def getBuckets(self, logbook):
        return SDKCommands.getBuckets(self.data_path_client, logbook)

    def getBucketInfo(self, bucket, logbook):
        return SDKCommands.getBucketInfo(self.data_path_client, bucket, logbook)

    def getBucketNames(self, logbook):
        return SDKCommands.getBucketNames(self.data_path_client, logbook)

    def getDataPolicies(self, logbook):
        return SDKCommands.getDataPolicies(self.data_path_client, logbook)

    def getDiskPartitions(self, logbook):
        return SDKCommands.getDiskPartitions(self.data_path_client, logbook)

    def getPools(self, logbook):
        return SDKCommands.getPools(self.data_path_client, logbook)

    def getStorageDomains(self, logbook):
        return SDKCommands.getStorageDomains(self.data_path_client, logbook)

    def getTapePartitions(self, logbook):
        return SDKCommands.getTapePartitions(self.data_path_client, logbook)

    def getUsers(self, logbook):
        return SDKCommands.getUsers(self.data_path_client, logbook)
