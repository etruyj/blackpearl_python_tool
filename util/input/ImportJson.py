# ImportJson.py
#   Reads a json file into a variable.

import json

def fromFile(path):
    try:
        f = open(path)
        
        data = json.load(f)

        f.close()

        return data
    except Exception as e:
        print(e)
