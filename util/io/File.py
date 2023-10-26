#====================================================================
# File.py
#   Description:
#       Handles read/write operations to files
#====================================================================

import os

def load(file):
    #============================================
    # load
    #   Loads the file line by line into a list
    #   object and returns that object. Only to be
    #   used when there will only be a finite number
    #   of lines in the file. If the size of the
    #   file cannot be controlled for, use
    #   partialParse instead.
    #============================================

    try:
        data = []
        in_file = open(file, "r", encoding='utf-8')

        for line in in_file:
            # Need to remove end of line (EOL) characters from
            # the input data.
            # line = line[:-1] this is not descriminating enough.
            line = line.rstrip('\n')
            data.append(line)

        in_file.close()
        return data
    except Exception as e:
        raise e

def loadLines(file, start=0, buffer=1000):
    #============================================
    # loadLine INCOMPLETE
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

def saveLines(file_path, lines):
    try:
        out_file = open(file_path + ".tmp", "w")

        for line in lines:
            out_file.write(line + "\n")

        out_file.close()
        os.replace(file_path + ".tmp", file_path)
    except Exception as e:
        raise e
