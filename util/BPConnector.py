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
            try:
                self.managementPathAuthentication(endpoint, username, password, logbook)

                if(self.validConnection):
                    self.retrieveDataPathParameters(endpoint, username, logbook)
        
                    # Save this for verifying connectivity.
                    self.management_path = endpoint
            except Exception as e:
                logbook.ERROR(e.__str__())
                raise e
        else:
            self.dataPathAuthentication(endpoint, access_key, secret_key, logbook)

    def dataPathAuthentication(self, endpoint, access_key, secret_key, logbook):
        try:
            logbook.INFO("Accessing data path: " + endpoint)

            if(access_key == "none" and secret_key == "none"):
                logbook.INFO("Creating client with environmental variables")
        
                self.data_path_client = ds3.createClientFromEnv()
            else:
                logbook.INFO("Creating connection to BlackPearl [" + endpoint + "].")
                logbook.INFO("Using access key " + access_key)

                self.data_path_client = ds3.Client(endpoint, ds3.Credentials(access_key, secret_key))
        except Exception as e:
            print(e)
            self.validConnection = False

    def managementPathAuthentication(self, endpoint, username, password, logbook):
        logbook.INFO("Accessing management path...")
        try:
            self.token =  self.authenticate(endpoint, username, password, logbook)

            # Verify the connection
            if(self.token == "none"):
                self.validConnection = False
        except Exception as e:
            logbook.ERROR(e.__str__())

            if("nodename nor servname provided" in e.__str__()):
                raise Exception("Failed to resolve hostname: " + endpoint)
            else:
                raise Exception("Failed to connect to BlackPearl management port: " + endpoint)
            

    def retrieveDataPathParameters(self, endpoint, username, logbook):
        logbook.INFO("Searching for data path credentials...")

        try:
            data_path = HttpCommands.getDataPathIP(endpoint, self.token, logbook)
            data_port = HttpCommands.getDataPathPort(endpoint, self.token, logbook)
            keys = HttpCommands.findDs3Credentials(endpoint, self.token, username, logbook)
    
            if(keys != None):
                self.dataPathAuthentication(data_path + ":" + data_port, keys['access_key'], keys['secret_key'], logbook)
            else:
                # If keys were able to be found, don't attempt to connect to the BlackPearl
                # and just mark the data path client as None (null) to allow for the 
                # the script to check if the connection is valid.
                self.data_path_client = None
        except Exception as e:
            logbook.ERROR(e.__str__())
            raise e

    def verifyConnection(self, logbook):
        if(self.validConnection and self.verifyDataConnection(logbook)):
            return True
        else:
            return False

    def verifyDataConnection(self, logbook):
        try:
            if(self.data_path_client != None):
                getServiceResponse = self.data_path_client.get_net_client()
                return True
            else:
                logbook.ERROR("Unable to connect to data path.")
                print("ERROR: Unable to connect to data path.")
                return False
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

    def createNASPool(self, pool, logbook):
        return HttpCommands.createPool(self.management_path, self.token, pool, logbook)

    def createNfsShare(self, comment, volume, mount_point, path, access_control, service_id, logbook):
        return HttpCommands.createNfsShare(self.management_path, self.token, comment, volume, mount_point, path, access_control, service_id, logbook)

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
        try:
            return SDKCommands.createDataPersistenceRule(self.data_path_client, data_policy_id, isolation, storage_domain_id, storage_type, days_to_retain, logbook)
        except Exception as e:
            raise e

    def addDiskPartitionToStorageDomain(self, pool_id, storage_domain_id, write_optimization, logbook):
        try:
            return SDKCommands.createStorageDomainPoolMember(self.data_path_client, pool_id, storage_domain_id, write_optimization, logbook)
        except Exception as e:
            raise e

    def addTapePartitionToStorageDomain(self, storage_domain_id, tape_par_id, tape_type, auto_compaction, write_optimization, logbook):
        try:
            return SDKCommands.createStorageDomainTapeMember(self.data_path_client, storage_domain_id, tape_par_id, tape_type, auto_compaction, write_optimization, logbook)
        except Exception as e:
            raise e

    def createBucket(self, name, data_policy, owner, logbook):
        try:
            return SDKCommands.createBucket(self.data_path_client, name, data_policy, owner, logbook)
        except Exception as e:
            raise e

    def createDataPolicy(self, name, force_puts, min_spanning, blobbing, checksum_type, blob_size, get_priority, put_priority, verify_after_write, verify_priority, end_to_end_crc, versions_to_keep, rebuild_priority, versioning, logbook):
        try:
            return SDKCommands.createDataPolicy(self.data_path_client, name, force_puts, min_spanning, blobbing, checksum_type, blob_size, get_priority, put_priority, verify_after_write, verify_priority, end_to_end_crc, versions_to_keep, rebuild_priority, versioning, logbook)
        except Exception as e:
            raise e

    def createDiskPartition(self, name, partition_type, logbook):
        try:
            return SDKCommands.createDiskPartition(self.data_path_client, name, partition_type, logbook)
        except Exception as e:
            raise e

    def createStorageDomain(self, name, auto_eject_threshold, auto_eject_cron, auto_eject_cancellation, auto_eject_on_completion, auto_eject_on_full, ltfs_file_naming, verification_frequency_days, auto_compaction_threshold, media_ejection_allowed, secure_media_allocation, verify_prior_to_eject, write_optimization, logbook):
        try:
            return SDKCommands.createStorageDomain(self.data_path_client, name, auto_eject_threshold, auto_eject_cron, auto_eject_cancellation, auto_eject_on_completion, auto_eject_on_full, ltfs_file_naming, verification_frequency_days, auto_compaction_threshold, media_ejection_allowed, secure_media_allocation, verify_prior_to_eject, write_optimization, logbook)
        except Exception as e:
            raise e

    def getBuckets(self, logbook):
        try:
            return SDKCommands.getBuckets(self.data_path_client, logbook)
        except Exception as e:
            raise e

    def getBucketInfo(self, bucket, logbook):
        try:
            return SDKCommands.getBucketInfo(self.data_path_client, bucket, logbook)
        except Exception as e:
            raise e

    def getBucketNames(self, logbook):
        try:
            return SDKCommands.getBucketNames(self.data_path_client, logbook)
        except Exception as e:
            raise e

    def getCompletedJobs(self, logbook):
        try:
            return SDKCommands.getCompletedJobs(self.data_path_client, logbook)
        except Exception as e:
            raise e

    def getDataPolicies(self, logbook):
        try:
            return SDKCommands.getDataPolicies(self.data_path_client, logbook)
        except Exception as e:
            raise e

    def getDiskPartitions(self, logbook):
        try:
            return SDKCommands.getDiskPartitions(self.data_path_client, logbook)
        except Exception as e:
            raise e

    def getObjects(self, bucket_name, logbook):
        try:
            return SDKCommands.getObjects(self.data_path_client, bucket_name, logbook)
        except Exception as e:
            raise e


    def getPools(self, logbook):
        try:
            return SDKCommands.getPools(self.data_path_client, logbook)
        except Exception as e:
            raise e

    def getStorageDomainMembers(self, logbook):
        try:
            return SDKCommands.getStorageDomainMembers(self.data_path_client, logbook)
        except Exception as e:
            raise e

    def getStorageDomains(self, logbook):
        try:
            return SDKCommands.getStorageDomains(self.data_path_client, logbook)
        except Exception as e:
            raise e

    def getTapePartitions(self, logbook):
        try:
            return SDKCommands.getTapePartitions(self.data_path_client, logbook)
        except Exception as e:
            raise e

    def getTapesAll(self, logbook):
        try:
            return SDKCommands.getTapesAll(self.data_path_client, logbook)
        except Exception as e:
            raise e

    def getUsers(self, logbook):
        try:
            return SDKCommands.getUsers(self.data_path_client, logbook)
        except Exception as e:
            raise e
