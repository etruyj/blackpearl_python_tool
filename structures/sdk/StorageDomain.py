#=====================================================================
#   StorageDomain.py
#       Description:
#           A container for the Storage Domain information returned
#           by the SDK ds3.GetStorageDomainsSpectraS3Request
#=====================================================================

class StorageDomain:
    #============================================
    # Getters
    #============================================
   
    def getId(self):
        return self.domain_id

    def getName(self):
        return self.name

    #============================================
    # Setters
    #============================================

    def setEjectFullThreshold(self, d):
        self.auto_eject_media_full_threshold = d

    def setEjectCron(self, d):
        self.auto_eject_upon_cron = d

    def setEjectOnCancelled(self, d):
        self.auto_eject_upon_job_cancellation

    def setEjectOnCompleted(self, d):
        self.auto_eject_upon_job_completion

    def setEjectOnFull(self, d):
        self.auto_eject_upon_media_full = d

    def setId(self, d):
        self.domain_id = d

    def setLtfsFileNaming(self, d):
        self.ltfs_file_naming = d

    def setMaxTapeFragmentationPercent(self, d):
        self.max_tape_fragmentation_percent = d

    def setAutoVerificationFrequency(self, d):
        self.max_auto_verification_frequency = d

    def setMediaEjectionAllowed(self, d):
        self.media_ejection_allowed = d
    
    def setName(self, d):
        self.name = d

    def setSecureMediaAllocation(self, d):
        self.secure_media_allocation = d

    def setVerifyPriorToAutoEject(self, d):
        self.verify_prior_to_auto_eject = d

    def setWriteOptimization(self, d):
        self.write_optimization = d

    #============================================
    # Vars
    #============================================

    auto_eject_media_full_threshold = None
    auto_eject_upon_cron = None
    auto_eject_upon_job_cancellation = None
    auto_eject_upon_job_completion = None
    auto_eject_upon_media_full = None
    domain_id = None
    ltfs_file_naming = None
    max_tape_fragmentation_percent = None
    max_auto_verification_frequency = None
    media_ejection_allowed = None
    name = None
    secure_media_allocation = None
    verify_prior_to_auto_eject = None
    write_optimization = None
