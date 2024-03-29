# StorageUnits.py
#   Description:
#       Convert storage units to and from bytes

def bytesToHumanReadable(storage):
    # convert storage to int
    # It appears python defaults all objects to string when
    # passed in a function.
    storage = int(storage)
    unit = "B"

    while(storage >= 1024):
        match(unit):
            case "B":
                storage = storage / 1024
                unit = "KiB"
            case "KiB":
                storage = storage / 1024
                unit = "MiB"
            case "MiB":
                storage = storage / 1024
                unit = "GiB"
            case "GiB":
                storage = storage / 1024
                unit = "TiB"
            case "TiB":
                storage = storage / 1024
                unit = "PiB"
            case "PiB":
                storage = storage / 1024
                unit = "EiB"

    format_float = str(round(storage, 2))
    return format_float + " " + unit

def humanReadableToBytes(storage):
    if(str(storage).find(" ") == -1):
        # Doesn't contain a space
        # No units specified
        # Assuming this is bytes.
        return storage
    else:
        # Units are probably present.
        # Attempting to covert to bytes.
        unit = storage[(storage.find(" ") + 1):]
        storage = int(storage[:storage.find(" ")])
        
        while(unit != "B"):
            match(unit):
                case "EiB":
                    storage = storage * 1024
                    unit = "PiB"
                case "PiB":
                    storage = storage * 1024
                    unit = "TiB"
                case "TiB":
                    storage = storage * 1024
                    unit = "GiB"
                case "GiB":
                    storage = storage * 1024
                    unit = "MiB"
                case "MiB":
                    storage = storage * 1024
                    unit = "KiB"
                case "KiB":
                    storage = storage * 1024
                    unit = "B"
                case "EB":
                    storage = storage * 1000
                    unit = "PB"
                case "PB":
                    storage = storage * 1000
                    unit = "TB"
                case "TB":
                    storage = storage * 1000
                    unit = "GB"
                case "GB":
                    storage = storage * 1000
                    unit = "MB"
                case "MB":
                    storage = storage * 1000
                    unit = "KB"
                case "KB":
                    storage = storage * 1000
                    unit = "B"

    return storage


