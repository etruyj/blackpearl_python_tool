#!/usr/bin/env python3

import sys
import ui.ArgParser as aparser
import ui.display.Display as Display
from ui.Controller import Controller
from ds3 import ds3

aparser.loadConfiguration()
aparser.parseArgs(sys.argv)

if(aparser.isValid()):
    controller = Controller(aparser.getEndpoint(), aparser.getUsername(), aparser.getPassword(), aparser.getAccessKey(), aparser.getSecretKey(), aparser.getLogCount(), aparser.getLogLevel(), aparser.getLogLocation(), aparser.getLogSize())

    if controller.clientValid():
        response = None # Declare response as none to allow testing for valid response.

        match aparser.getCommand():
            case "command-test":
                response = controller.test(aparser.getOption1(), aparser.getOption3())
            case "clear-cache":
                response = controller.clearCache();
            case "configure":
                response = controller.configureBP(aparser.getOption4())
            case "delete-objects":
                response = controller.deleteObjects(aparser.getOption1(), aparser.getOption4(), aparser.getOption2())
            case "delete-tape" | "delete-tapes":
                response = controller.deleteTape(aparser.getOption1(), aparser.getOption2(), aparser.getOption3(), aparser.getOption4())
            case "eject-tape" | "eject-tapes" | "export-tape" | "export-tapes":
                response = controller.ejectTape(aparser.getOption1(), aparser.getOption2(), aparser.getOption3(), aparser.getOption4())
            case "fetch-config":
                response = controller.fetchConfig()
            case "get-database":
                response = controller.downloadNewestDatabase(aparser.getOption3(), aparser.getOption4())
            case "job-report":
                response = controller.jobReport(aparser.getOption3())
            case "list-buckets":
                response = controller.listBuckets()
            case "list-data-policies" | "list-policies":
                response = controller.listDataPolicies()
            case "list-objects":
                response = controller.listObjects(aparser.getOption1(), aparser.getObjectFetchLimit())
            case "list-pools":
                response = controller.listPools()
            case "list-storage-domains" | "list-domains":
                response = controller.listStorageDomains()
            case "list-tapes":
                response = controller.listTapesAll()
            case "list-tape-partitions":
                response = controller.listTapePartitions()
            case "list-users":
                response = controller.listUsers()
            case "mark-read-only":
                response = controller.makeBucketReadOnly(aparser.getOption1())
            case "put-object":
                response = controller.putObject(aparser.getOption1(), aparser.getOption4(), aparser.getOption3())
            case "stage-objects":
                response = controller.stageObjects(aparser.getOption1(), aparser.getOption4())
            case "tape-report":
                response = controller.tapeReport(aparser.getOption2(), aparser.getOption3())
            case _:
                print("ERROR: Invalid command selected [" + aparser.getCommand() + "]. Please type help to see valid commands.")
        
        if(response != None):
            Display.output(response, aparser.getOutputFormat(), aparser.getOption4())
    else:
        # Connection is invalid
        print("Unable to connect to BlackPearl at " + aparser.getEndpoint() + " with username " + aparser.getUsername())

elif(not aparser.printedText()):
   print("Invalid option selected. Type --help to see valid options")
