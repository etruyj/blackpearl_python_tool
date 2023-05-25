# AddDataPersistenceRule.py
#   Add a data persistence rule to a storage domain

def verifyThenAdd(blackpearl, data_policy_id, isolation, storage_domain_id, storage_type, min_days_to_retain, logbook):
    if(storage_type == "permanent" and min_days_to_retain != None):
        logbook.WARN("Invalid data persistence rule. Permanent storage does not require a minimum days_to_retain field.")
        logbook.WARN("Setting days_to_retain to 0.")
        print("Invalid data persistence rule. Permanent storage does not require a minimum days_to_retain field.")
        print("Setting days_to_retain to None.")
        min_days_to_retain = None

    if(storage_type == "temporary" and min_days_to_retain == None):
        logbook.WARN("Invalid data persistence rule. Temporary storage requires a minimum days_to_retain field.")
        print("Invalid data persistence rule. Temporary storage requires a minimum days_to_retain field.")
    else:
        return blackpearl.addDataPersistenceRule(data_policy_id, isolation, storage_domain_id, storage_type, min_days_to_retain, logbook)
