#====================================================================
# Configuration.py
#   Description:
#       This class loads configuration files into the program.
#====================================================================

import os
import yaml

def load():
    # This is the configuration file name.
    file_name = "nacre.yml"
    config = []

    for path in os.curdir, "../", os.path.expanduser("~"), "/etc/nacre/", os.environ.get("NACRE_CONF"):
        try:
            with open(os.path.join(path, file_name), "r") as file:
                data = yaml.safe_load_all(file)
                
                for doc in data:
                    config.append(doc)
                
                return config
        except Exception as e:
            pass

def update(document, updated_values):
    # This is the configuration file name
    file_name = "nacre.yml"
    config = []

    for path in os.curdir, "../", os.path.expanduser("~"), "/etc/nacre/", os.environ.get("NACRE_CONF"):
        try:
            with open(os.path.join(path, file_name), "r") as file:
                data = yaml.safe_load_all(file)
                
                for doc in data:
                    config.append(doc)
            
            for doc in config:
                if(document in doc):
                    doc[document] = updated_values

            with open(os.path.join(path, file_name), "w") as file:
                yaml.dump_all(config, file)

        except Exception as e:
            pass

    
