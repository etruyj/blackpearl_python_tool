# HttpHandler
#   Handles HTTP requests to the management path of the BlackPearl

import requests

def authenticate(address, username, password, logbook):
    logbook.INFO("Authenticating with BlackPearl at " + address + " with username " + username)

    json_body = {'username': username, 'password': password}

    r = requests.post("https://" + address + "/api/tokens.json", data = json_body, verify=False)

    if(r.status_code >= 200 and r.status_code <= 230):
        return r.text
    else:
        logbook.ERROR("[" + r.status_code + "] " + r.text);

def get(address, token, logbook):
    logbook.INFO("GET: " +  address);

    request_headers = {"Authorization" : "Bearer " + token}

    r = requests.get(address, headers=request_headers, verify=False)

    if(r.status_code >=200 and r.status_code <= 230):
        return r.text
    else:
        logbook.ERROR("[" + r.status_code + "] " + r.text);
