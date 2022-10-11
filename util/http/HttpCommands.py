# HttpCommands
#   HTTP Commands for the BlackPearl Management Interface

import json
import util.http.HttpHandler as HttpHandler

def authenticate(url, username, password, logbook):
    response = HttpHandler.authenticate(url, username, password, logbook)

    if(response != None):
        try:
            auth = json.loads(response)
            
            logbook.INFO("Authentication successful.")
            return auth['token']
        except Exception as e:
            print(e)
            logbook.ERROR(e)
            return "none"
    else:
        logbook.ERROR("Failed to authenticate with username " + username)
        return "none"

def createCifsShare(endpoint, token, name, path, volume_id, readonly, service_id, logbook):
    logbook.INFO("Creating CIFS share [" + name + "]...")

    url = "https://" + endpoint + "/api/shares"

    logbook.DEBUG("Calling HttpHandler.post(" + url + ")...")

    request_body = { "name": name, "path": path, "type": "Cifs", "readonly": readonly, "volume_id": volume_id, "service_id": service_id}
    
    response = HttpHandler.post(url, token, request_body, logbook)

    if(response != None):
        return response
    else:
        print("WARNING: Unabled to create share [" + name + "]")
        logbook.ERROR("Unable to create share [" + name + "]")

def createNfsShare(endpoint, token, comment, volume_id, mount_point, path, access_control, service_id, logbook):
    logbook.INFO("Creating NFS share [" + mount_point + "]...")

    url = "https://" + endpoint + "/api/shares"

    logbook.DEBUG("Calling HttpHandler.post(" + url + ")...")

    request_body = { "comment": comment, "mount_point": mount_point, "path": path, "type": "Nfs", "volume_id": volume_id, "access_control": access_control, "service_id": service_id}
    
    response = HttpHandler.post(url, token, request_body, logbook)

    if(response != None):
        return response
    else:
        print("WARNING: Unabled to create share [" + mount_point + "]")
        logbook.ERROR("Unable to create share [" + mount_point + "]")

def createVailShare(endpoint, token, name, volume_id, service_id, logbook):
    logbook.INFO("Creating Vail share [" + name + "]...")

    url = "https://" + endpoint + "/api/vail_shares"
    
    logbook.DEBUG("Calling HttpHandler.post(" + url + ")...")

    request_body = { "name": name, "type": "Vail", "service_id": service_id, "volume_id": volume_id }

    reponse = HttpHander.post(url, token, request_body, logbook)

    if(response != None):
        return response
    else:
        print("WARNING: Unable to create Vail share [" + name + "].")
        logbook.ERROR("Unable to create Vail share [" + name + "].")

def createVolume(endpoint, token, access_time, case_insensitive, compression, deduplication, name, nfi_repeat_schedule_daily, nfi_repeat_schedule_hour, nfi_repeat_schedule_minute, nfi_repeat_schedule_unit, nfi_repeat_schedule_weekly, nfi_volume_policy_bucket_id, nfi_volume_policy_cron_string, nfi_volume_policy_enabled, nfi_volume_policy_nfi_system_id, nfi_volume_policy, pool_id, quota, reservation, read_only, size, snapshot_change_threshold, vol_type, logbook):
    logbook.INFO("Creating volume [" + name + "]...")

    url = "https://" + endpoint + "/api/volumes"

    logbook.DEBUG("Calling HttpHandler.post(" + url + ")...")

    request_body = { "atime": access_time, "caseinsensitive": case_insensitive, "compression": compression, "deduplication": deduplication, "name": name, "nfi_repeat_schedule_daily_value": nfi_repeat_schedule_daily, "nfi_repeat_schedule_hourly_value": nfi_repeat_schedule_hour, "nfi_repeat_schedule_minute_value": nfi_repeat_schedule_minute, "nfi_repeat_schedule_unit": nfi_repeat_schedule_unit, "nfi_repeat_schedule_weekly_days": nfi_repeat_schedule_weekly, "nfi_volume_policy_bucket_id": nfi_volume_policy_bucket_id, "nfi_volume_policy_cron_string": nfi_volume_policy_cron_string, "nfi_volume_policy_enabled": nfi_volume_policy_enabled, "nfi_volume_policy_nfi_system_id": nfi_volume_policy_nfi_system_id, "nfi_volume_policy_policy": nfi_volume_policy, "pool_id": pool_id, "quota": quota, "read_only": read_only, "reservation": reservation, "size": size, "snapshot_change_threshold": snapshot_change_threshold, "type": vol_type }

    response = HttpHandler.post(url, token, request_body, logbook)

    if(response != None):
        return response
    else:
        logbook.ERROR("Unabled to create volume [" + name + "]")
        print("WARNING: Unabled to create volume [" + name + "]")

def findDs3Credentials(endpoint, token, username, logbook):
    logbook.INFO("Finding DS3 keys for user [" + username + "]...")

    users = getUsers(endpoint, token, logbook)

    if(users != None):
        for user in users:
            if(user['name'] == username):
                keys = getUserKeys(endpoint, token, user['id'], logbook)
                return keys

def getDataPathIP(endpoint, token, logbook):
    logbook.INFO("Querying data path IP address...");
    all_interfaces = getNetworkInterfaces(endpoint, token, logbook);

    if(all_interfaces != None):
        for interface in all_interfaces:
            if(interface['type'] == "data" and interface['up']):
                for address in interface['addresses']:
                    if(not address['autoconf']):
                        logbook.INFO("Found data path address [" + interface['name'] + "] " + address['address'])
                        #strip the subnet
                        index = address['address'].find("/")
                        ip = address['address'][:index]
                        return ip
    else:
        logbook.ERROR("Unabled to determine data path address.")

def getNetworkInterfaces(endpoint, token, logbook):
    logbook.INFO("Fetching network interfaces...")
    
    url = "https://" + endpoint + "/api/network_interfaces"

    logbook.DEBUG("HttpHandler.get(" + url + ")")

    response = HttpHandler.get(url, token, logbook)

    if(response != None):
        try:
            data = json.loads(response)

            logbook.INFO("Found (" + str(len(data['data'])) + ") network interfaces.")

            return data['data']
        except Exception as e:
            print(e)
            logbook.ERROR("JSON Parse Exception")
            logbook.ERROR(e)
    else:
        logbook.ERROR("Failed to retrieve network interfaces.")

def getPools(endpoint, token, logbook):
    logbook.INFO("Fetching pools...")

    url = "https://" + endpoint + "/api/nas/pools"

    logbook.DEBUG("HttpHandler.get(" + url + ")")

    response = HttpHandler.get(url, token, logbook)

    if(response != None):
        try:
            data = json.loads(response)

            logbook.INFO("Found (" + str(len(data['data'])) + ") pools.")

            return data['data']
        except Exception as e:
            print(e)
            logbook.ERROR("JSON PARSE Exception")
            logbook.ERROR(e)
    else:
        logbook.ERROR("Failed to retrieve pool information.")

def getServices(endpoint, token, logbook):
    logbook.INFO("Fetching blackpearl services...")

    url = "https://" + endpoint + "/api/services"

    logbook.DEBUG("HttpHandler.get(" + url + ")")

    response = HttpHandler.get(url, token, logbook)

    if(response != None):
        try:
            data = json.loads(response)

            logbook.INFO("Found (" + str(len(data['data'])) + ") services.")

            return data['data']
        except Exception as e:
            print(e)
            logbook.ERROR("JSON Parse Exception")
            logbook.ERROR(e)

def getUserKeys(endpoint, token, user_id, logbook):
    logbook.INFO("Fetching ds3 keys for user [" + str(user_id) + "]...")

    url = "https://" + endpoint + "/api/ds3/keys?user_id=" + str(user_id)

    logbook.DEBUG("HttpHandler.get(" + url + ")")

    response = HttpHandler.get(url, token, logbook)

    if(response != None):
        try:
            keys = {}
            data = json.loads(response)
           
            # Iterate just in case it becomes necessary
            # but only one key_pair should exist.
            for key_pair in data['data']:
                keys['access_key'] = key_pair['auth_id']
                keys['secret_key'] = key_pair['secret_key']
            
            logbook.INFO("Found access key [" + keys['access_key'] + "]")
            
            return keys
        except Exception as e:
            print(e)
            logbook.ERROR("JSON Parse Exception")
            logbook.ERROR(e)
    else:
        logbook.ERROR("Failed to retrieve user keys")

def getUsers(endpoint, token, logbook):
    logbook.INFO("Fetching users list...")

    url = "https://" + endpoint + "/api/users?sort_by=username"

    logbook.DEBUG("HttpHandler.get(" + url + ")")

    response = HttpHandler.get(url, token, logbook)

    if(response != None):
        try:
            data = json.loads(response)

            logbook.INFO("Found (" + str(len(data['data'])) + ") users.")

            return data['data']
        except Exception as e:
            print(e)
            logbook.ERROR("JSON Parse Exception")
            logbook.ERROR(e)
    else:
        logbook.ERROR("Failed to retrieve user list.")

def getVolumes(endpoint, token, logbook):
    logbook.INFO("Fetching system volumes...")

    url = "https://" + endpoint + "/api/volumes?sort_by=name"

    logbook.DEBUG("HttpHandler.get(" + url + ")")

    response = HttpHandler.get(url, token, logbook)

    if(response != None):
        try:
            data = json.loads(response)

            logbook.INFO("Found (" + str(len(data['data'])) + ") volumes.")

            return data['data']
        except Exception as e:
            print(e)
            logbook.ERROR("JSON Parse Exception")
            logbook.ERROR(e)
    else:
        logbook.ERROR("Failed to retrieve volume list.")
