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

class Logger:

    def __init__(self, location, max_size, count, level):
        self.path = location
        self.log_size = max_size
        self.log_count = count
        self.log_level = level

    def DEBUG(self, line):
        self.writeLog("DEBUG: " + line, 1)

    def ERROR(self, line):
        self.writeLog("ERROR: " + line, 4)

    def INFO(self, line):
        self.writeLog("INFO: " + line, 2)

    def WARN(self, line):
        self.writeLog("WARN: " + line, 3)

    def writeLog(self, line, level):
        now = datetime.now()
        datestr = now.strftime("%Y/%m/%d %H:%M:%S")

        if(level >= self.log_level):
            #write log
            f = open(self.path, "a")
            f.write(datestr + " : " + line + "\n")
            f.close()
