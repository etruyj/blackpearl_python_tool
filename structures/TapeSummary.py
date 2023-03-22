#====================================================================
#   TapeSummary.py
#       Description:
#           A container for summary information about the tape.
#====================================================================

class TapeSummary:
    #============================================
    # Getters
    #============================================
    def getAvailableCapacity(self):
        return self.capacity_available

    def getBarcode(self):
        return self.barcode

    def getBucket(self):
        return self.bucket

    def getState(self):
        return self.state

    def getStorageDomain(self):
        return self.storage_domain

    def getTapeType(self):
        return self.tape_type

    def getTapePartition(self):
        return self.tape_partition

    def getTotalCapacity(self):
        return self.capacity_total
    
    def getUsedCapacity(self):
        return self.capacity_used

    #============================================
    # Setters
    #============================================
    def setAvailableCapacity(self, d):
        # Error handle null values
        # Present for unknown tapes.
        if(d == None):
            d = 0

        self.capacity_available = d

    def setBarcode(self, d):
        self.barcode = d

    def setBucket(self, d):
        self.bucket = d

    def setTapeCapacity(self, total, available):
        self.setAvailableCapacity(available)
        self.setTotalCapacity(total)
        self.setUsedCapacity()

    def setState(self, d):
        self.state = d

    def setStorageDomain(self, d):
        self.storage_domain = d

    def setTapeType(self, d):
        self.tape_type = d

    def setTapePartition(self, d):
        self.tape_partition = d

    def setTotalCapacity(self, d):
        # Error handle no values.
        # Present for unknown tapes.
        if(d == None):
            d = 0

        self.capacity_total = d

    def setUsedCapacity(self):
        self.capacity_used = int(self.capacity_total) - int(self.capacity_available)

    #============================================
    # Variables
    #============================================
    barcode = None
    bucket = None
    capacity_available =0
    capacity_total = 0
    capacity_used = None
    state = None
    storage_domain = None
    tape_type = None
    tape_partition = None
