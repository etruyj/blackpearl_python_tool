#====================================================================
# BucketGroupTapes
#   Description:
#       This contains the tape information when grouped by bucket.
#====================================================================

class BucketGroupTapes:
    #============================================
    # Getters
    #============================================
    def getAvailableCapacity(self):
        return self.capacity_available

    def getBucketName(self):
        return self.name

    def getTapeCount(self):
        return self.tape_count

    def getTotalCapacity(self):
        return self.capacity_total

    def getUsedCapacity(self):
        return self.capacity_used

    #============================================
    # Setters
    #============================================
    def addAvailableCapacity(self, d):
        # error handle null values
        if(d == None):
            d = 0

        self.capacity_available += int(d)

    def addTapeCapacity(self, total, available):
        self.addTotalCapacity(total)
        self.addAvailableCapacity(available)
        self.addUsedCapacity(total, available)

    def addTape(self):
        self.tape_count += 1

    def addTotalCapacity(self, d):
        # error handle null values
        if(d == None):
            d = 0

        self.capacity_total += int(d)

    def addUsedCapacity(self, total, available):
        # Error handle null values
        if(total == None):
            total = 0

        if(available == None):
            available = 0

        self.capacity_used += int(total) - int(available)

    def setAvailableCapacity(self, d):
        # Error handle null values
        if(d == None):
            d = 0

        self.capacity_available = d

    def setBucketName(self, bucket):
        self.name = bucket

    def setTapeCapacity(self, total, available):
        self.setAvailableCapacity(available)
        self.setTotalCapicity(total)
        self.setUsedCapacity(total, available)

    def setTapeCount(self, count):
        self.tape_count = count

    def setTotalCapacity(self, d):
        # Error handle null values
        if(d == None):
            d = 0

        self.capacity_total = d

    def setUsedCapacity(self, total, available):
        # Error handle null values
        if(total == None):
            total = 0

        if(available == None):
            available = 0

        self.capacity_used = int(total) - int(available)

    #============================================
    # Variables
    #============================================
    capacity_available = 0
    capacity_total = 0
    capacity_used = 0
    name = None
    tape_count = 0
    
