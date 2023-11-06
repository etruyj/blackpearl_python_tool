#====================================================================
# ui/Argparser.py
#   Description:
#        Handles parsing command line arguments into operational
#        variables.
#====================================================================

import ui.display.Display as Display
import util.Configuration as Configuration
import util.convert.StorageUnits as StorageUnits

# Variable declarations
https = True
is_valid = True
command_set = False
log_count = 3
log_level = 2
log_location = "../log/"
log_name = "bp_main.log"
log_size = 102400
object_fetch_limit = 500
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

def configureLogging(log_settings):
    if log_settings == None or len(log_settings) == 0:
        print("Configuration file missing log settings. Using defaults.")
    else:
        # Log Count
        if 'log_count' in log_settings:
            log_count = log_settings['log_count']
        else:
            print("log_count not specified in configuration file. Using default " + str(log_count))

        # Log Level
        if 'log_level' in log_settings:
            match log_settings['log_level']:
                case "NONE":
                    log_level = 0
                case "DEBUG":
                    log_level = 1
                case "INFO":
                    log_level = 2
                case "WARNING":
                    log_level = 3
                case "ERROR":
                    log_level = 4
                case _:
                    print("Invalid log level specified in configuration file. Please specify NONE, DEBUG, INFO, WARNING, or ERROR.")

        else:
            print("log_level not specified in configuration file. Using default INFO")

        # Log Path
        if "log_location" in log_settings:
            log_location = log_settings['log_location']
            
            if( not (log_location[:-1] == "/" or log_location[:-1] == "\\")):
                log_location = log_location + "/"

        else:
            print("log_location not present in configuration file. Using default: " + log_location)

        # Log Name
        if "log_name" in log_settings:
            log_name = log_settings['log_name']
        else:
            print("log_name not present in configuraiton file. Using default: " + log_name)

        # Log Size
        if "log_size" in log_settings:
            log_size = log_settings['log_size']
        else:
            print("log_size not present in configuration file. Using default: " + str(log_size))

def configureSettings(settings):
    global object_fetch_limit # scope is clashing for some reason.
    try:
        if(settings != None and len(settings) > 0):
            if('max_moves' in settings):
                option2 = settings["max_moves"]
        
            if('object_fetch_limit' in settings):
                object_fetch_limit = settings["object_fetch_limit"]
            else:
                print("object_fetch_limit not found in configuration file. Using default value: " + str(object_fetch_limit))

        else:
            print("No script settings found in the configuration file. Using default values.")


    except Exception as e:
        print("ERROR: " + e.__str__())

def loadConfiguration():
    try:
        config = Configuration.load()
    
        for doc in config:
            if 'logging' in doc:
                configureLogging(doc['logging'])
            elif 'settings' in doc:
                configureSettings(doc['settings'])
    except Exception as e:
        print("ERROR: " + e.__str__())

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
            case "--option1" | "--bucket" | "--barcode":
                i += 1
                setOption1(args[i])
            case "--option2" | "--group-by" | "--max-moves" | "--moves" | "--buffer":
                i += 1
                setOption2(args[i])
            case "--option3" | "--filter" | "--prefix" | "--key":
                i += 1
                setOption3(args[i])
            case "--option4" | "--file" | "--path":
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

def getLogCount():
    return log_count

def getLogLevel():
    return log_level

def getLogLocation():
    return log_location + log_name

def getLogSize():
    return log_size

def getObjectFetchLimit():
    return object_fetch_limit

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
