# HttpHandler
#   Handles HTTP requests to the management path of the BlackPearl

import json
import requests
from requests.exceptions import ConnectTimeout
from urllib3.exceptions import InsecureRequestWarning


def authenticate(address, username, password, logbook):
    logbook.INFO("Authenticating with BlackPearl at " + address + " with username " + username)

    json_body = {'username': username, 'password': password}

    # Attempt Connection
    try:
        # Suppress insecure SSL certificate warning.
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    
        r = requests.post("https://" + address + "/api/tokens.json", data = json_body, verify=False, timeout=3)

        if(r.status_code >= 200 and r.status_code <= 230):
            return r.text
        else:
            print("[" + str(r.status_code) + "] " + r.text);
            logbook.ERROR("[" + str(r.status_code) + "] " + r.text);
    except ConnectTimeout:
        logbook.ERROR("Connection timed out.")
    except Exception as e:
        logbook.ERROR(e.__str__())
        raise e

def get(address, token, logbook):
    logbook.INFO("GET: " +  address);

    request_headers = {"Authorization" : "Bearer " + token}

    try:
        # Suppress insecure SSL certificate warning.
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    
        r = requests.get(address, headers=request_headers, verify=False, timeout=3)

        if(r.status_code >=200 and r.status_code <= 230):
            return r.text
        else:
            logbook.ERROR("[" + str(r.status_code) + "] " + r.text);
    except ConnectTimeout:
        logbook.ERROR("Connection timed out.")
    except Exception as e:
        logbook.ERROR(e.__str__())
        raise e

def post(address, token, request_body, logbook):
    logbook.INFO("POST: " + address)

    request_headers = {"Authorization" : "Bearer " + token, "Content-Type": "application/json", "User-Agent": "Python-3.10-requests", "Accept": "*/*", "Connection": "keep-alive"}

    request_body = json.dumps(request_body)

    try:
        # Suppress insecure SSL certificate warning.
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    
        r = requests.post(address, headers=request_headers, data = request_body, verify=False, timeout=3)

        if(r.status_code >=200 and r.status_code <=230):
            return r.text
        else:
            logbook.ERROR("[" + str(r.status_code) + "] " + r.text)
            logbook.ERROR(str(request_body))
    except ConnectTimeout:
        logbook.ERROR("Connection timed out.")
    except Exception as e:
        logbook.ERROR(e.__str__())
        raise e
