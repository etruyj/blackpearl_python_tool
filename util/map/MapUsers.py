#====================================================================
#   MapUsers.py
#       Description:
#           Creates a dictionary of [String, String] to determine
#           user name from id and user id from name.
#====================================================================

from structures.UserSummary import UserSummary

def createIDNameMap(users):
    user_map = {}

    if(users != None):
        for user in users:
            user_map[user.uuid] = user.name

    return user_map

def createNameIDMap(users):
    user_map = {}
    
    if(users != None):
        for user in users:
            user_map[user.name] = user.uuid

    return user_map

