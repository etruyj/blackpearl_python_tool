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

def output(output, output_format="csv", file=None, first_run=True, re_run=False):
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
        # Whether it should be an append or fresh file is the opposite
        # of whether or not this is the first run. The same is true about
        # whether the file path should be printed being the opposite off
        # the state of re_run.
        Save.appendToFile(toPrint, file, not first_run, not re_run)
