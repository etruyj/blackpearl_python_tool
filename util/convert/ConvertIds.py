#====================================================================
# ConvertIds.py
#   Description:
#       Converts ids to names based on the provided map
#====================================================================

def findName(identifier, id_name_map, log_message, logbook):
    # Override the existing identifier with a name
    # if it is present in the map. Otherwise return
    # the identifier in the map.
    # Log message should state what type of item is being
    # queried, Bucket, Storage Domain, etc, for messaging.

    if(id_name_map != None):
        if(identifier != None):
            if(identifier in id_name_map):
                identifier = id_name_map[identifier]
            else:
                logbook.WARN(log_message + " ID [" + identifier + "] not found in list.")

    return identifier
