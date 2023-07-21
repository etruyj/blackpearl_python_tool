#====================================================================
#   Cache.py
#       Description:
#           These command relate to the BlackPearl cache.
#====================================================================

from ds3 import ds3

def forceClear(blackpearl, log):
    log.DEBUG("blackpearl.force_full_cache_reclaim_spectra_s3(ds3.ForceFullCacheReclaimSpectraS3Request())")
    
    try:
        response = blackpearl.force_full_cache_reclaim_spectra_s3(ds3.ForceFullCacheReclaimSpectraS3Request())

        print(response)
    except Exception as e:
        print(e)
