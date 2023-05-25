#=====================================================================
# BucketSummary.py
#   Description:
#       Holds bucket summary information.
#   
#       Info:
#           - name
#           - owner
#           - datapolicy
#           - size
#=====================================================================

from structures.Summary import Summary

class BucketSummary(Summary):
    def __init__(self):
        super().__init__()

    #============================================
    # Getters
    #============================================
    
    def getDataPolicy(self):
        return self.data_policy

    def getId(self):
        return self.uuid

    def getName(self):
        return self.name

    def getOwner(self):
        return self.owner

    def getSize(self):
        return self.size


    #============================================
    # Setters
    #============================================

    def setId(self, d):
        self.uuid = d;

    def setName(self, n):
        self.name = n

    def setOwner(self, o):
        self.owner = o

    def setDataPolicy(self, d):
        self.data_policy = d
    
    def setSize(self, s):
        self.size = s

    owner = "none"
    data_policy = "none"
    size = 0

