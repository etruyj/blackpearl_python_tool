#!/usr/bin/env python3

import sys
import ui.ArgParser as aparser
import ui.display.Display as Display
from ui.Controller import Controller
from ds3 import ds3

aparser.parseArgs(sys.argv)

if(aparser.isValid()):
    controller = Controller(aparser.getEndpoint(), aparser.getUsername(), aparser.getPassword(), aparser.getAccessKey(), aparser.getSecretKey())

    if controller.clientValid():
        response = None # Declare response as none to allow testing for valid response.

        match aparser.getCommand():
            case "configure":
                response = controller.configureBP(aparser.getOption4())
            case "delete-objects":
                response = controller.deleteObjects(aparser.getOption1(), aparser.getOption4(), aparser.getOption2())
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
                response = controller.listObjects(aparser.getOption1())
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
            case "tape-report":
                response = controller.tapeReport(aparser.getOption2(), aparser.getOption3())
            case _:
                print("ERROR: Invalid command selected. Please type help to see valid commands.")
        
        if(response != None):
            Display.output(response, aparser.getOutputFormat(), aparser.getOption4())
    else:
        # Connection is invalid
        print("Unable to connect to BlackPearl at " + aparser.getEndpoint() + " with username " + aparser.getUsername())

elif(not aparser.printedText()):
   print("Invalid option selected. Type --help to see valid options")
