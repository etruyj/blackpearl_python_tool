#====================================================================
# ui/controller.py
#   Description:
#       Handles calls to different systems
#====================================================================

from util.BPConnector import BPConnector
from util.Logger import Logger

import command.ConfigureBlackPearl as ConfigureBlackPearl
import command.ListBuckets as ListBuckets
import command.ListDataPolicies as ListDataPolicies
import command.ListPools as ListPools
import command.ListStorageDomains as ListStorageDomains
import command.ListTapes as ListTapes
import command.ListTapePartitions as ListTapePartitions
import command.ListUsers as ListUsers

class Controller:
    def __init__(self, endpoint, username, password, access_key, secret_key):
        self.logbook = Logger("../log/bp_script.log", "10 KiB", 2, 2)
        self.blackpearl = BPConnector(endpoint, username, password, access_key, secret_key, self.logbook)

    def clientValid(self):
        return self.blackpearl.verifyDataConnection(self.logbook)
    
    def configureBP(self, file_path):
        return ConfigureBlackPearl.fromFile(self.blackpearl, file_path, self.logbook)

    def fetchConfig(self):
        print("this worked too")

    def listBuckets(self):
        return ListBuckets.createList(self.blackpearl, self.logbook)

    def listDataPolicies(self):
        return ListDataPolicies.createList(self.blackpearl, self.logbook)

    def listPools(self):
        return ListPools.createList(self.blackpearl, self.logbook)

    def listStorageDomains(self):
        return ListStorageDomains.createList(self.blackpearl, self.logbook)

    def listTapesAll(self):
        return ListTapes.allTapes(self.blackpearl, self.logbook)

    def listTapePartitions(self):
        return ListTapePartitions.all(self.blackpearl, self.logbook)

    def listUsers(self):
        return ListUsers.createList(self.blackpearl, self.logbook)
