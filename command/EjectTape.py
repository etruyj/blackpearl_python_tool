#====================================================================
# EjectTape.py
#   Description:
#       Sends the command to delete the specified tape barcode.
#====================================================================

import command.TapeReport as TapeReport
import util.io.File as File

def byBarcode(blackpearl, barcode, logbook):
    try:
        logbook.INFO("Ejecting tape with barcode " + barcode)

        return blackpearl.ejectTape(barcode, logbook)
    except Exception as e:
        logbook.ERROR(e.__str__())
        return e.__str__()

def fromFile(blackpearl, file_path, max_moves, logbook):
    try:
        logbook.INFO("Ejecting tapes listed in " + file_path + " up to the maximum specified (" + str(max_moves) + ") tapes.")
        logbook.DEBUG("Calling File.load(" + file_path + ")...")

        tape_list = File.load(file_path)
        logbook.INFO("Found (" + str(len(tape_list)) + ") tapes in file.")

    except Exception as e:
        logbook.ERROR(e.__str__())
        return e.__str__() 

    # eject statistics [0: list position, 1: successes, 2: failures]
    stats = sendEjects(blackpearl, tape_list, max_moves, logbook)
    
    # Save remaining tapes back to the original file.
    if(stats[0] < len(tape_list)):
        try:
            File.saveLines(file_path, tape_list[stats[0]:])
        except Exception as e:
            logbook.WARN(e.__str__())
            print(e.__str__())

    return "Eject commands sent for (" + str(stats[1]) + ") tapes."

def fromFilteredList(blackpearl, filter_params, max_moves, logbook):
    try:
        logbook.INFO("Ejecting tapes that match filter [" + filter_params + "] up to the maximum specified (" + str(max_moves) + ") tapes.")
        logbook.DEBUG("Calling TapeReport.createReport('', " + filter_params + ")...")
        tape_report = TapeReport.createReport("", filter_params, blackpearl, logbook)

        logbook.INFO("Filter returned a list of (" + str(len(tape_report)) + ") tapes.")

    except Exception as e:
        logbook.ERROR(e.__str__())
        return e.__str__()

    # For modularity, tape_report needs to be converted into a tape list.
    tape_list = []
    for tape in tape_report:
        tape_list.append(tape.getBarcode())

    stats = sendEjects(blackpearl, tape_list, max_moves, logbook)

    return "Eject commands sent for (" + str(stats[1]) + ") tapes."

def sendEjects(blackpearl, tape_list, max_moves, logbook):
    counter = 0
    success = 0
    failed = 0
 
    # Eject tapes.
    #   No try catch allows the function to process even if something fails.
    while(counter < len(tape_list) and success < int(max_moves)):
        if("barcode" not in tape_list[counter] and "bar_code" not in tape_list[counter]):
            result = byBarcode(blackpearl, tape_list[counter], logbook)
  
            if("Unable" in result or "does not exist" in result):
                failed += 1
                print(result)
            else:
                success += 1

            counter += 1
    
    logbook.INFO("Successfully ejected (" + str(success) + ") tapes.")
    logbook.INFO("Failed to eject (" + str(failed) + ") tapes.")

    stats = [counter, success, failed]

    return stats
