#====================================================================
# File.py
#   Description:
#       Handles read/write operations to files
#====================================================================

import os

def loadLines(file, start=0, buffer=1000):
    #============================================
    # loadLine
    #   Loads the specified number of lines into a
    #   a list. If less lines are present than the
    #   amount allowed in the buffer, just those lines
    #   will be returned.
    #============================================

    try:
        data = []
        in_file = open(file, "r")
        counter = 0
        line = in_file.readline()

        while(line == True and counter < buffer):
            data.append(line)
            counter += 1

        in_file.close()
        return data
    except Exception as e:
        raise e

def partialParse(file, buffer=1000):
    #============================================
    # partialParse
    #   Description:
    #       Read the first $buffer lines of the file.
    #       Lines read are returned to the file.
    #============================================

    try:
        data = []
        remaining_lines = 0

        with open(file, "r") as in_file, open(file + ".tmp", "w") as out_file:
            for x in range(buffer):
                line = in_file.readline()
                
                # Exit the loop if end of file is reached.
                if(line == "" or line == None):
                    break
               
                # Strip the endline character from the line.
                line = line[:-1]
                data.append(line)
            
            for line in in_file:
                # Exit the loop if end of file is reached.
                if(line == ""):
                    break;

                out_file.write(line)
                remaining_lines += 1
            
            in_file.close()
            out_file.close()

        # If data was saved to the .tmp file
        # replace the original file with the tmp
        # otherwise delete both files.
        if(remaining_lines > 0):
            os.replace(file + ".tmp", file)
        else:
            os.remove(file)
            os.remove(file + ".tmp")

        return data

    except Exception as e:
        raise e
