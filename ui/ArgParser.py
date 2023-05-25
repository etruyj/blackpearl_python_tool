#====================================================================
# ui/Argparser.py
#   Description:
#        Handles parsing command line arguments into operational
#        variables.
#====================================================================

import ui.display.Display as Display

# Variable declarations
https = True
is_valid = True
command_set = False
option1_set = False
option2_set = False
option3_set = False
option4_set = False
option1 = None
option2 = None
option3 = None
option4 = None
print_text = False
endpoint = "127.0.0.1"
username = "none"
password = "none"
access_key = "none"
secret_key = "none"
command = "none"
output_format = "table"

def parseArgs(args):
    global is_valid
    global print_text
    
    # range(1, len(args)) is used as arg 0 is the script itself
    for i in range(1, len(args)):
        match args[i]:
            case "-a" | "--access" | "--access-key":
                i += 1
                setAccessKey(args[i])
            case "-c" | "--command":
                i += 1
                setCommand(args[i])
            case "-e" | "--endpoint":
                i += 1
                setEndpoint(args[i])
            case "-h" | "--help":
                Display.fileContents("../lib/help/options.txt")
                is_valid = False
                print_text = True
            case "--http":
                https = False
            case "-k" | "--secret" | "--secret-key":
                i += 1
                setSecretKey(args[i])
            case "--option1" | "--bucket":
                i += 1
                setOption1(args[i])
            case "--option2" | "--group-by":
                i += 1
                setOption2(args[i])
            case "--option3" | "--filter":
                i += 1
                setOption3(args[i])
            case "--option4" | "--file":
                i += 1
                setOption4(args[i])
            case "--output-format":
                i += 1
                setOutputFormat(args[i])
            case "-p" | "--password":
                i += 1
                setPassword(args[i])
            case "-u" | "--user" | "--username":
                i += 1
                setUsername(args[i])
            case "--version":
                Display.fileContents("../lib/help/version.txt")
                is_valid = False
                print_text = True

# Getters

def getAccessKey():
    return access_key

def getCommand():
    return command

def getEndpoint():
    return endpoint

def getOption1():
    if(option1 != None):
        return option1
    else:
        return ""

def getOption2():
    if(option2 != None):
        return option2
    else:
        return ""

def getOption3():
    if(option3 != None):
        return option3
    else:
        return ""

def getOption4():
    if(option4 != None):
        return option4
    else:
        return ""

def getOutputFormat():
    if(output_format != None):
        return output_format
    else:
        return "table"

def getSecretKey():
    return secret_key

def isValid():
    return is_valid

def getPassword():
    return password

def getUsername():
    return username

def printedText():
    return print_text

# Setters

def setAccessKey(key):
    global access_key 
    access_key = key

def setCommand(cmd):
    global command_set
    global command
    global is_valid

    if(command_set):
        is_valid = False
    else:
        command = cmd
        command_set = True

def setEndpoint(ip):
    global endpoint
    endpoint = ip

def setOption1(op):
    global option1_set
    global option1
    global is_valid
    if(option1_set):
        is_valid = False
    else:
        option1 = op
        option1_set = True

def setOption2(op):
    global option2_set
    global option2
    global is_valid
    if(option2_set):
        is_valid = False
    else:
        option2 = op
        option2_set = True

def setOption3(op):
    global option3_set
    global option3
    global is_valid
    if(option3_set):
        is_valid = False
    else:
        option3 = op
        option3_set = True

def setOption4(op):
    global option4_set
    global option4
    global is_valid
    if(option4_set):
        is_valid = False
    else:
        option4 = op
        option4_set = True

def setOutputFormat(ou):
    global output_format
    output_format = ou

def setPassword(pw):
    global password
    password = pw

def setUsername(user):
    global username
    username = user

def setSecretKey(key):
    global secret_key
    secret_key = key
