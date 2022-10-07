#====================================================================
#   MapServices.py
#       Description:
#           Creates a dictionary of [String, String] to determine
#           service name from id and service id from name.
#====================================================================

def createIDNameMap(services):
    service_map = {}

    if(services != None):
        for service in services:
            service_map[service['id']] = service_map['name']

    return sevice_map

def createNameIDMap(services):
    service_map = {}
    
    if(services != None):
        for service in services:
            service_map[service['name']] = service['id']

    return service_map

