#====================================================================
#   Save.py
#       Description:
#           Saves the output to the specified file.
#====================================================================

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
