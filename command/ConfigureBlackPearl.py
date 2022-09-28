# ConfigureBlackPearl.py
#   Reads a json configuration file and excutes the commands
#   necessary to perform this configuration.

import command.CreateDataPolicy as CreateDataPolicy
import command.ListDataPolicies as ListDataPolicies
import command.ListStorageDomains as ListStorageDomains
import command.ListUsers as ListUsers
import util.input.ImportJson as ImportJson
import util.map.MapDataPolicies as MapDataPolicies
import util.map.MapStorageDomains as MapStorageDomains
import util.map.MapUsers as MapUsers
import util.Logger as Logger

import collections.abc

def fromFile(blackpearl, file_path, logbook):
    logbook.INFO("Configuring BlackPearl with configuration file " + file_path)
    logbook.DEBUG("Calling ImportJson.fromFile(" + file_path + ")...")

    success = [8]
    config = ImportJson.fromFile(file_path)
    
    if(config == None):
        logbook.ERROR("Unable to open file.")
    else:
        # BP Log Parser Fetch Array
        # Check for and correct.
        if(isinstance(config, collections.abc.Sequence)):
            config = config[0]

        # Basic Report to Logs
        logbook.INFO("Configuration loaded.")
        if('buckets' in config.keys()):
            logbook.INFO("Configuration contains (" + str(len(config['buckets'])) + ") buckets.")
        if('data_policies' in config.keys()):
            logbook.INFO("Configuration contains (" + str(len(config['data_policies'])) + ") data policies.")
        if('storage_domains' in config.keys()):
            logbook.INFO("Configuration contains (" + str(len(config['storage_domains'])) + ") storage_domains.")
        if('disk_partitions' in config.keys()):
            logbook.INFO("Configuration contains (" + str(len(config['disk_partitions'])) + ") disk partitions.")
        if('pools' in config.keys()):
            logbook.INFO("Configuration contains (" + str(len(config['pools'])) + ") pools.")
        if('volumes' in config.keys()):
            logbook.INFO("Configuration contains (" + str(len(config['volumes'])) + ") volumes.")
        if('shares' in config.keys()):
            logbook.INFO("Configuration contains (" + str(len(config['shares'])) + ") shares.")

        # Create Data Policies
        if('data_policies' in config.keys()):
            success[0] = createDataPolicies(blackpearl, config['data_policies'], logbook)

        # Create Buckets
        if('buckets' in config.keys()):
            #success[0] = createBuckets(blackpearl, config['buckets'], logbook)
            pass

        report(success, config, logbook)

#========================================
# Inner Functions
#========================================

def createBuckets(blackpearl, bucket_list, logbook):
    success = 0
    
    logbook.DEBUG("Calling ListDataPolicies.createList()...")
    policy_list = ListDataPolicies.createList(blackpearl, logbook)
    logbook.DEBUG("Calling MapDataPolicies.createNameIDMap()...")
    policy_map = MapDataPolicies.createNameIDMap(policy_list)

    logbook.DEBUG("Calling ListUsers.createList()...")
    user_list = ListUsers.createList(blackpearl, logbook)
    logbook.DEBUG("Calling MapUsers.createNameIDMap()...")
    user_map = MapUsers.createNameIDMap(user_list)

    logbook.DEBUG("Calling blackpearl.createBucket()..")
    for bucket in bucket_list:
        if(bucket['data_policy'] not in policy_map.keys()):
            logbook.WARN("Cannot identify data policy [" + bucket['data_policy'] + "] for bucket [" + bucket['name'] + "]")
            logbook.WARN("Skipping blackpearl.createBucket(" + bucket['name'] + ")")
        elif(bucket['owner'] not in user_map.keys()):
            logbook.WARN("Cannot identify user [" + bucket['owner'] + "] for bucket [" + bucket['name'] + "]")
            logbook.WARN("Skipping blackpearl.createBucket(" + bucket['name'] + ")")
        else:
            result = blackpearl.createBucket(bucket['name'], policy_map[bucket['data_policy']], user_map[bucket['owner']], logbook)

            if(result != None):
                success += 1

    return success

def createDataPolicies(blackpearl, policy_list, logbook):
    success = 0

    logbook.DEBUG("Calling ListStorageDomains.createList()...")
    domain_list = ListStorageDomains.createList(blackpearl, logbook)

    logbook.DEBUG("Calling MapStorageDomains.createNameIDMap()...")
    domain_map = MapStorageDomains.createNameIDMap(domain_list)

    logbook.DEBUG("Calling CreateDataPolicy.fillMissingFieldsThenVerify()...")

    for policy in policy_list:
        result = CreateDataPolicy.fillMissingFieldsThenVerify(blackpearl, policy, logbook)
       
        print(result)
        if(result != None):
            success += 1

            for domain in policy['data_persistence_rules']:
                print(domain['name'])

    return success

def report(success, config, logbook):
    if('buckets' in config.keys() and success[0] != None):
            logbook.INFO("Sucessfully created " + str(success[0]) + "/" + str(len(config['buckets'])) + " buckets.")

