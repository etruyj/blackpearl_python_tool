from structures.BucketSummary import BucketSummary
from structures.TapeSummary import TapeSummary
from structures.UserSummary import UserSummary

import ui.display.ConvertCSV as ConvertCSV
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

def output(output, output_format="csv", file=None):
    toPrint = []

    # Covert output to the desired format
    if(output_format == "csv"):
        toPrint = ConvertCSV.toOutput(output)

    if(file==None or file==""):
        Print.toShell(toPrint)
    else:
        Save.toFile(toPrint, file)
