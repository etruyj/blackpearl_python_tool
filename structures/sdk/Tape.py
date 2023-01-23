#====================================================================
# Tape.py
#   Description:
#       Holds all tape data returned by the getTapes API call
#====================================================================

class Tape:
    #============================================
    # Getters
    #============================================
    def getBarcode(self):
        return self.barcode

    def getBucketId(self):
        return self.bucket_id

    def getState(self):
        return self.state

    def getStorageDomainMemberId(self):
        return self.storage_domain_id

    def getTapeType(self):
        return self.tape_type

    def getPartitionId(self):
        return self.partition_id

    #============================================
    # Setters
    #============================================
    def setAssignedToStorageDomain(self, v):
        self.assigned_to_storage_domain = v

    def setAvailableCapacity(self, c):
        self.available_raw_capacity = c

    def setBarcode(self, b):
        self.barcode = b

    def setBucketId(self, b):
        self.bucket_id = b

    def setDescription(self, d):
        self.description = d

    def setEjectDate(self, d):
        self.eject_date = d

    def setEjectLabel(self, d):
        self.eject_label = d

    def setEjectLocation(self, d):
        self.eject_location = d

    def setEjectPending(self, d):
        self.eject_pending = d

    def setFullOfData(self, d):
        self.full_of_data = d

    def setId(self, d):
        self.tape_id = d

    def setLastAccessed(self, d):
        self.last_accessed = d

    def setLastCheckpoint(self, d):
        self.last_checkpoint = d

    def setLastModified(self, d):
        self.last_modified = d

    def setLastVerified(self, d):
        self.last_verified = d

    def setPartiallyVerifiedEndOfTape(self, d):
        self.partially_verified_end_of_tape = d

    def setPartitionId(self, d):
        self.partition_id = d

    def setPreviousState(self, d):
        self.previous_state = d

    def setSerialNumber(self, d):
        self.serial_number = d

    def setState(self, d):
        self.state = d

    def setStorageDomainId(self, d):
        self.storage_domain_id = d

    def setTakeOwnershipPending(self, d):
        self.take_ownership_pending = d

    def setTotalRawCapacity(self, d):
        self.total_raw_capacity = d

    def setType(self, d):
        self.tape_type = d

    def setVerifyPending(self, d):
        self.verify_pending = d

    def setWriteProtected(self, d):
        self.write_protected = d

    #============================================
    # Variables
    #============================================
    assigned_to_storage_domain = False
    available_raw_capacity = None
    barcode = None
    bucket_id = None
    description = None
    eject_date = None
    eject_label = None
    eject_location = None
    eject_pending = None
    full_of_data = False
    tape_id = None
    last_accessed = None
    last_checkpoint = None
    last_modified = None
    last_verified = None
    partially_verified_end_of_tape = None
    partition_id = None
    previous_state = None
    serial_number = None
    state = None
    storage_domain_member_id = None
    take_ownership_pending = None
    total_raw_capacity = None
    tape_type = None
    verify_pending = None
    write_protected = None
