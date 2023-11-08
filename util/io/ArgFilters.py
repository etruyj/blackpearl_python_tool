#====================================================================
# ArgFilters.py
#   Parses the filters for the scripts arguements. This will allow
#   multiple filters parameters to be passed by the user.
#   
#   Options
#       Major parameters should be separated by a semi-colon.
#       Option settings can be set using a colon.
#       Multiple options can be specified by comma separation.
#       EXAMPLE: --filter key1:value;key2:value,value
#====================================================================

def parseParameters(filters):
    response = {}

    # Break the string into the major parameters.
    params = filters.split(";")

    for param in params:
        # Split the key value pair.
        key_values = param.split(":")
        
        # Check to see if the key has values assigned. If not raise an Exception
        if(len(key_values) == 2):
            # Check to see if multiple values are passed.
            if("," in key_values[1]):
                # If multiple values are passed split them and create a list.
                values = key_values[1].split(",")

                value_list = []
                for value in values:
                    value_list.append(value)

                response[key_values[0]] = value_list
            else:
                response[key_values[0]] = key_values[1]

        else:
            raise Exception("Invalid parameter. No values defined for filter [" + key_values[0] + "]")
    
    return response
