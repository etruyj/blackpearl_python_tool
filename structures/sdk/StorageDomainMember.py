#====================================================================
#   StorageDomainMember.py
#       Description:
#           A container class for all the information returned by
#           the ds3.get_storage_domain_members_spectra_s3() SDK call
#====================================================================

class StorageDomainMember:
    #============================================
    # Getters
    #============================================

    def getMemberId(self):
        return self.member_id

    def getDomainId(self):
        return self.storage_domain_id

    #============================================
    # Setters
    #============================================
    
    def setCompactionThreshold(self, d):
        self.auto_compaction_threshold = d

    def setId(self, d):
        self.member_id = d

    def setPoolPartitionId(self, d):
        self.pool_partition_id = d
    
    def setTapePartitionId(self, d):
        self.tape_partition_id = d

    def setState(self, d):
        self.state = d

    def setStorageDomainId(self, d):
        self.storage_domain_id = d

    def setTapeType(self, d):
        self.tape_type = d

    def setWritePreference(self, d):
        self.write_preference = d

    #============================================
    # Variables
    #============================================

    auto_compaction_threshold = None
    member_id = None
    pool_partition_id = None
    storage_domain_id = None
    state = None
    tape_partition_id = None
    tape_type = None
    write_preference = None
