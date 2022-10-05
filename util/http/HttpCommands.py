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
