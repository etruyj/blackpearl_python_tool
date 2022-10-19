#====================================================================
#   Logger.py
#       Description:
#           A basic logging script.
#
# log levels
#   0 - no logs
#   1 - debug
#   2 - info
#   3 - warn
#   4 - error
#====================================================================

from datetime import datetime
import util.convert.StorageUnits as StorageUnits
import os

class Logger:

    def __init__(self, location, max_size, count, level):
        self.path = location
        self.log_size = StorageUnits.humanReadableToBytes(max_size)
        self.log_count = count
        self.log_level = level

    def DEBUG(self, line):
        self.log("DEBUG: " + line, 1)

    def ERROR(self, line):
        self.log("ERROR: " + line, 4)

    def INFO(self, line):
        self.log("INFO: " + line, 2)

    def WARN(self, line):
        self.log("WARN: " + line, 3)

    def log(self, line, level):
        self.checkSize()
        self.writeLog(line, level)

    def writeLog(self, line, level):
        now = datetime.now()
        datestr = now.strftime("%Y/%m/%d %H:%M:%S")

        if(level >= self.log_level):
            #write log
            f = open(self.path, "a")
            f.write(datestr + " : " + line + "\n")
            f.close()
    
    def checkSize(self):
        if(os.path.exists(self.path)):
            size = os.stat(self.path).st_size
        else:
            size = 0

        if(size > int(self.log_size)):
            # Let the user know logs rolled.
            self.writeLog("Maximum log size reached. Rolling logs.", 5)
            self.rotateLogs()

    def rotateLogs(self):
        # Remove the last log if max has been reached.
        if(self.log_count == 1):
            os.remove(self.path)
        elif(os.path.exists(self.path + "." + str(self.log_count))):
            os.remove(self.path + "." + str(self.log_count))

        # Rotate logs.
        #   Go from last to 
        for i in range((self.log_count - 1), -1, -1):
            original_path = self.path + "." + str(i)
            if(i == 0 and self.log_count > 1):
                os.rename(self.path, self.path + ".1")
            elif(os.path.exists(original_path)):
                # move file
                suffix_len = len(str(i))
                new_path = original_path[:(len(original_path) - suffix_len)]
                try:
                    os.rename(original_path, new_path + str(i+1))
                except Exception as e:
                    print(e)
