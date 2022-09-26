#!/usr/bin/env python3

import sys
import ui.argparser as aparser
import ui.display.Display as Display
from ui.Controller import Controller
from ds3 import ds3

aparser.parseArgs(sys.argv)

if(aparser.isValid):
    controller = Controller(aparser.getEndpoint(), aparser.getAccessKey(), aparser.getSecretKey())

    if controller.clientValid():
        match aparser.getCommand():
         case "fetch-config":
             response = controller.fetchConfig()
         case "list-buckets":
             response = controller.listBuckets()
         case "list-users":
             response = controller.listUsers()
         case _:
             print("ERROR: Invalid command selected. Please type help to see valid commands.")

        Display.output(response)
else:
    print("Invalid option selected. Type help to see valid options")

