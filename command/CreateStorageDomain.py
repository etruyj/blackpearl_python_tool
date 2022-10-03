# CreateStorageDomain.py

def fillFieldsThenVerify(blackpearl, domain, logbook):
    if('name' in domain.keys()):
        name = domain['name']
    else:
        name = None
    
    if('auto_eject_threshold' in domain.keys()):
        auto_eject_threshold = domain['auto_eject_threshold']
    else:
        auto_eject_threshold = None
    
    if('auto_eject_upon_cron' in domain.keys()):
        auto_eject_cron = domain['auto_eject_upon_cron']
    else:
        auto_eject_cron = None

    if('auto_eject_upon_cancellaton' in domain.keys()):
        auto_eject_cancellation = domain['auto_eject_upon_cancellaton']
    else:
        auto_eject_cancellation = None

    if('auto_eject_upon_completion' in domain.keys()):
        auto_eject_on_completion = domain['auto_eject_upon_completion']
    else:
        auto_eject_on_completion = None

    if('auto_eject_on_media_full' in domain.keys()):
        auto_eject_on_full = domain['auto_eject_on_media_full']
    else:
        auto_eject_on_full = None

    if('ltfs_file_naming' in domain.keys()):
        ltfs_file_naming = domain['ltfs_file_naming']
    else:
        ltfs_file_naming = None

    if('days_to_verify' in domain.keys()):
        verification_frequency_days = domain['days_to_verify']
    else:
        verification_fequency_days = None
    
    auto_compaction_threshold = None

    if('media_ejection_allowed' in domain.keys()):
        media_ejection_allowed = domain['media_ejection_allowed']
    else:
        media_eject_allowed = None

    if('secure_media_allocation' in domain.keys()):
        secure_media_allocation = domain['secure_media_allocation']
    else:
        secure_media_allocation = None

    if('verify_prior_to_auto_eject' in domain.keys()):
        verify_prior_to_eject = domain['verify_prior_to_auto_eject']
    else:
        verify_prior_to_eject = None

    if('write_optimization' in domain.keys()):
        write_optimization = domain['write_optimization']
    else:
        write_optimization = None

    logbook.DEBUG("Calling verifyThenCreate()...")
    return verifyThenCreate(blackpearl, name, auto_eject_threshold, auto_eject_cron, auto_eject_cancellation, auto_eject_on_completion, auto_eject_on_full, ltfs_file_naming, verification_frequency_days, auto_compaction_threshold, media_ejection_allowed, secure_media_allocation, verify_prior_to_eject, write_optimization, logbook)

def verifyThenCreate(blackpearl, name, auto_eject_threshold, auto_eject_cron, auto_eject_cancellation, auto_eject_on_completion, auto_eject_on_full, ltfs_file_naming, verification_frequency_days, auto_compaction_threshold, media_ejection_allowed, secure_media_allocation, verify_prior_to_eject, write_optimization, logbook):
    #Add more checks are requirements are determined.
    if(name == None):
        logbook.ERROR("Storage domain is missing required field: name")
        print("Storage domain is missing required field: name")
    else:
        logbook.DEBUG("Calling blackpearl.createStorageDomain()...")
        return blackpearl.createStorageDomain(name, auto_eject_threshold, auto_eject_cron, auto_eject_cancellation, auto_eject_on_completion, auto_eject_on_full, ltfs_file_naming, verification_frequency_days, auto_compaction_threshold, media_ejection_allowed, secure_media_allocation, verify_prior_to_eject, write_optimization, logbook)

