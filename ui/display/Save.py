#====================================================================
#   Save.py
#       Description:
#           Saves the output to the specified file.
#====================================================================

def appendToFile(toPrint, file_path, append, print_file_path):
    try:
        if(not append):
            file = open(file_path, 'w')
        else:
            file = open(file_path, 'a')

        if(toPrint != None):
            for line in toPrint:
                file.write(line + "\n")

        file.close()

        if(print_file_path):
            print("Output saved to " + file_path) 

    except Exception as e:
        print(e)

def toFile(toPrint, file_path):
    try:
        file = open(file_path, 'w')

        if(toPrint != None):
            for line in toPrint:
                file.write(line + "\n")

        file.close()
        
        print("Output saved to " + file_path)

    except Exception as e:
        print(e)
