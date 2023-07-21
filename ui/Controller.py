#====================================================================
# ui/controller.py
#   Description:
#       Handles calls to different systems
#====================================================================

from util.BPConnector import BPConnector
from util.Logger import Logger
#import util.Configuration as Configuration

import command.ConfigureBlackPearl as ConfigureBlackPearl
import command.DeleteLostTapes as DeleteLostTapes
import command.DeleteObjects as DeleteObjects
import command.DownloadDatabase as DownloadDatabase
import command.EjectTape as EjectTape
import command.JobReport as JobReport
import command.LimitBucketSize as LimitBucketSize
import command.ListBuckets as ListBuckets
import command.ListDataPolicies as ListDataPolicies
import command.ListObjects as ListObjects
import command.ListPools as ListPools
import command.ListStorageDomains as ListStorageDomains
import command.ListTapes as ListTapes
import command.ListTapePartitions as ListTapePartitions
import command.ListUsers as ListUsers
import command.PutObject as PutObject
import command.ReadOnlyBucket as ReadOnlyBucket
import command.TapeReport as TapeReport

class Controller:
    def __init__(self, endpoint, username, password, access_key, secret_key):
        self.logbook = Logger("../log/bp_script.log", "100 KiB", 2, 2)
        self.blackpearl = BPConnector(endpoint, username, password, access_key, secret_key, self.logbook)

        if(username != None or username != ""):
            self.user = username
        else:
            self.user = access_key

    def clientValid(self):
        return self.blackpearl.verifyConnection(self.logbook)
    
    def configureBP(self, file_path):
        return ConfigureBlackPearl.fromFile(self.blackpearl, file_path, self.logbook)

    def deleteObjects(self, bucket, file_path, buffer):
        # Handle potential inputs.
        if(buffer == None or buffer=="" or int(buffer) <= 0):
            buffer = 1000
        
        return DeleteObjects.fromFile(self.blackpearl, bucket, file_path, self.logbook, self.user, buffer)

    def deleteTape(self, barcode="", max_moves="", filter_params="", file_path=""):
        # Set max moves to 10 if invalid.
        if(max_moves == None or max_moves == "" or int(max_moves) <= 0):
            self.logbook.INFO("Maximum number of moves not specified. Setting to 10.")
            max_moves = 10

        # Determine which command the user would like to use.
        if(barcode == "" and file_path == "" and filter_params == ""):
            # No input was specified.
            return "Invalid input selected. Please specify tape --barcode, filter parameters with --filter, or tape list --file."
        elif(barcode == "" and filter_params == ""):
            # File path was specified.
            return DeleteLostTapes.fromFile(self.blackpearl, file_path, max_moves, self.logbook)
        elif(file_path == "" and filter_params == ""):
            # barcode was specified.
            return DeleteLostTapes.byBarcode(self.blackpearl, barcode, self.logbook)
        else:
            # Use a filter to determine which tapes to eject.
            return DeleteLostTapes.fromFilteredList(self.blackpearl, filter_params, max_moves, self.logbook)

    def downloadNewestDatabase(self, file_prefix, file_path):
        return DownloadDatabase.mostRecent(self.blackpearl, file_prefix, file_path, self.logbook)

    def ejectTape(self, barcode="", max_moves="", filter_params="", file_path=""):
        # Set max moves to 10 if invalid.
        if(max_moves == None or max_moves == "" or int(max_moves) <= 0):
            self.logbook.INFO("Maximum number of moves not specified. Setting to 10.")
            max_moves = 10

        # Determine which command the user would like to use.
        if(barcode == "" and file_path == "" and filter_params == ""):
            # No input was specified.
            return "Invalid input selected. Please specify tape --barcode, filter parameters with --filter, or tape list --file."
        elif(barcode == "" and filter_params == ""):
            # File path was specified.
            return EjectTape.fromFile(self.blackpearl, file_path, max_moves, self.logbook)
        elif(file_path == "" and filter_params == ""):
            # barcode was specified.
            return EjectTape.byBarcode(self.blackpearl, barcode, self.logbook)
        else:
            # Use a filter to determine which tapes to eject.
            return EjectTape.fromFilteredList(self.blackpearl, filter_params, max_moves, self.logbook)

    def fetchConfig(self):
        print("this worked too")

    def jobReport(self, filter_by):
        return JobReport.createReport(self.blackpearl, filter_by, self.logbook)

    def listBuckets(self):
        return ListBuckets.createList(self.blackpearl, self.logbook)

    def listDataPolicies(self):
        return ListDataPolicies.createList(self.blackpearl, self.logbook)

    def listObjects(self, bucket):
        # Basic List Objects
        #return ListObjects.createList(bucket, self.blackpearl, self.logbook)
        # Advanced
        return ListObjects.withPhysicalLocations(bucket, "not-used", self.blackpearl, self.logbook)

    def listPools(self):
        return ListPools.createList(self.blackpearl, self.logbook)

    def listStorageDomains(self):
        return ListStorageDomains.createList(self.blackpearl, self.logbook)

    def listTapesAll(self):
        return ListTapes.createList(self.blackpearl, self.logbook)

    def listTapePartitions(self):
        return ListTapePartitions.all(self.blackpearl, self.logbook)

    def listUsers(self):
        return ListUsers.createList(self.blackpearl, self.logbook)

    def putObject(self, bucket, path, key=""):
        if(key == None or key == ""):
            return PutObject.toBlackPearl(self.blackpearl, bucket, path, self.logbook)
        else:
            return PutObject.toBlackPearl(self.blackpearl, bucket, key, path, self.logbook)

    def tapeReport(self, group_by, filter_by):
        return TapeReport.createReport(group_by, filter_by, self.blackpearl, self.logbook)

    def test(self, option):
        return LimitBucketSize.checkLimits(self.blackpearl, self.logbook)
