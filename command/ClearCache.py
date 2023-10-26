#====================================================================
#   ClearCache.py
#       Description:
#           Clears a BlackPearl's cache.
#====================================================================

def forceFullReclaim(blackpearl, log):
    log.INFO("Clearing BlackPearl cache...")

    try:
        blackpearl.reclaimCache(log)
        return "BlackPearl cache cleared successfully."
    except Exception as e:
        log.ERROR(e.__str__())
        return e.__str__()
