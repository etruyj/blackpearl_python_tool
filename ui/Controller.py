#====================================================================
# ui/controller.py
#   Description:
#       Handles calls to different systems
#====================================================================

from util.BPConnector import BPConnector
from util.Logger import Logger

import command.ListBuckets as ListBuckets
import command.ListUsers as ListUsers

class Controller:
    def __init__(self, endpoint, access_key, secret_key):
        self.logbook = Logger("../log/bp_scrip.log", 1024, 1, 1)
        self.blackpearl = BPConnector(endpoint, access_key, secret_key, self.logbook)

    def clientValid(self):
        return self.blackpearl.verifyConnection(self.logbook)
    
    def fetchConfig(self):
        print("this worked too")

    def listBuckets(self):
        return ListBuckets.createList(self.blackpearl, self.logbook)

    def listUsers(self):
        return ListUsers.createList(self.blackpearl, self.logbook)
