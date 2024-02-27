from structures.BucketSummary import BucketSummary
from structures.TapeSummary import TapeSummary
from structures.UserSummary import UserSummary

import ui.display.ConvertCSV as ConvertCSV
import ui.display.ConvertTable as ConvertTable
import ui.display.Print as Print
import ui.display.Save as Save
import os

def fileContents(path):
    if(os.path.exists(path)):
        f = open(path)
        print(f.read())
        f.close()

    else:
        print("Error [" + path + "] does not exist.")

def output(output, output_format="csv", file=None, first_run=True):
    toPrint = []

    # Handle error outputs. If the output is a single string
    # there is no need to format it and it should be printed
    # to the shell instead of saved to a file.
    if(isinstance(output, str)):
        toPrint.append(output)
        file =""
    else:
        # Covert output to the desired format
        match output_format:
            case "csv":
                toPrint = ConvertCSV.toOutput(output, first_run)
            case "table":
                toPrint = ConvertTable.toOutput(output, first_run)
            case _:
                toPrint = ConvertTable.toOutput(output, first_run)

    if(file==None or file==""):
        Print.toShell(toPrint)
    else:
        # For saving the file, two pieces of information need to be tracked
        # should we append the file (or create new) and should the output
        # path be printed multiple times. Both of this triggers relate to 
        # whether this is the first run of the script.
        # If it is the first run:
        #   append is false (aka not first_run)
        #   print_file_path is true (aka first_run)
        # The inverse is true in for the reverse.
        Save.appendToFile(toPrint, file, not first_run, first_run) 
