#====================================================================
#   ListUsers.py
#       Description:
#           Provides a list of users
#====================================================================

import util.Logger as Logger

from structures.UserSummary import UserSummary

def createList(blackpearl, logbook):
    logbook.DEBUG("Calling blackpearl.getUsers()");
    output = []
    user_list = []
    
    user_list = blackpearl.getUsers(logbook)

   
    if(user_list == None):
        print("Unable to retrieve user list")
        logbook.ERROR("Unable to retrieve user list")
    else:
        for user in user_list:
            summary = UserSummary()
            summary.name = user['Name']
            summary.uuid = user['Id']

            output.append(summary)

    return output
