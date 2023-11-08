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
        # Do-While Loop
        #   Fuding this to keep the logic clean for memory management
        #   with larger calls. For example, the list-objects command
        #   could conceivable have millions of returns. Instead of 
        #   parsing a potential unlimited data set, data will be handled
        #   in batches.
        #
        # Loop Variables
        #   first_run: first run of the loop. True to force initial execution.
        #               This will also be used to determine if column headers
        #               should be printed.
        #   re_run: does the function require another iteration.
        #   starting_position: for looped results, what page should the results start on.
        first_run = True
        re_run = False
        starting_position = None

        while first_run or re_run: # fudging a do-while loop.
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
                    results = controller.listObjects(aparser.getOption1(), aparser.getOption3(), aparser.getObjectFetchLimit(), starting_position)
                    if(isinstance(results, str)):
                        response = results
                    else:
                        response = results["results_list"]
                    
                        if(results["objects_remaining"] > 0):
                            re_run = True
                            starting_position = results["starting_page"]
                        else:
                            re_run = False
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
                Display.output(response, aparser.getOutputFormat(), aparser.getOption4(), first_run, re_run)
   
        
            # Reset first run
            first_run = False
        #========================================
        # END OF DO-WHILE
        #========================================
    else:
        # Connection is invalid
        print("Unable to connect to BlackPearl at " + aparser.getEndpoint() + " with username " + aparser.getUsername())

elif(not aparser.printedText()):
   print("Invalid option selected. Type --help to see valid options")
