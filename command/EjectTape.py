#====================================================================
# EjectTape.py
#   Description:
#       Sends the command to delete the specified tape barcode.
#====================================================================

def byBarcode(blackpearl, barcode, logbook):
    try:
        logbook.INFO("Ejecting tape with barcode " + barcode)

        response = blackpearl.ejectTape(barcode, logbook)
    except Exception as e:
        logbook.ERROR(e.__str__())
        return e.__str__()
