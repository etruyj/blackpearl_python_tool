#====================================================================
#   TapeSummary.py
#       Description:
#           A container for summary information about the tape.
#====================================================================

class TapeSummary:
    #============================================
    # Getters
    #============================================
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

    #============================================
    # Setters
    #============================================
    def setBarcode(self, d):
        self.barcode = d

    def setBucket(self, d):
        self.bucket = d

    def setState(self, d):
        self.state = d

    def setStorageDomain(self, d):
        self.storage_domain = d

    def setTapeType(self, d):
        self.tape_type = d

    def setTapePartition(self, d):
        self.tape_partition = d


    #============================================
    # Variables
    #============================================
    barcode = None
    bucket = None
    state = None
    storage_domain = None
    tape_type = None
    tape_partition = None
