#====================================================================
# ObjectDetails.py
#   Description:
#       This contains the detailed object information from the SDK
#       get_objects_with_full_details_spectra_s3() command. The
#       result field for this SDK call is structured as ObjectList: []
#       where this class will hold the objects included in that list.
#====================================================================

from structures.sdk.Ds3Blob import Ds3Blob
from structures.sdk.Tape import Tape

class ObjectDetails:
    def __init__(self):
        # Declare lists up here as these values are not reset
        # with class initialization if they are initially declared
        # as zero.
        self.AzureTargetList = []
        self.Ds3TargetList = []
        self.PoolList = []
        self.S3TargetList = []
        self.TapeList = []
        self.PhysicalPlacement = { "AzureTargetList", "Ds3TargetList", "TapeList", "PoolList", "S3TargetList" }


    #============================================
    # Getters
    #============================================

    def blobs(self):
        return self.Blobs

    def getBlobsBeingPersisted(self):
        if(self.BlobsBeingPersisted == None):
            return 0
        else:
            return self.BlobsBeingPersisted

    def getDegradedBlobCount(self):
        if(self.BlobsDegraded == None):
            return 0
        else:
            return self.BlobsDegraded
    
    def getCachedBlobCount(self):
        if(self.BlobsCached == None):
            return 0
        else:
            return self.BlobsCached

    def getTotalBlobCount(self):
        if(self.BlobsTotal == None):
            return 0
        else:
            return self.BlobsTotal

    def getBucketId(self):
        return self.BucketId

    def getCreationDate(self):
        return self.CreationDate

    def getETag(self):
        return self.ETag

    def getId(self):
        return self.Id

    def getName(self):
        return self.Name

    def getOwner(self):
        return self.Owner

    def getSize(self):
        return self.Size

    def getTapeCount(self):
        return len(self.TapeList)

    def getTapes(self):
        return self.TapeList

    def getType(self):
        return self.Type

    def isLatest(self):
        return self.Latest

    def isInCache(self):
        if(self.BlobsInCache == self.BlobsTotal):
            return True
        else:
            return False

    #============================================
    # Setters
    #============================================
    
    def importObject(self, o):
        if(self.getName() != None):
            print(self.getName() + " " + self.getTapeCount())
        self.setBlobs(o['Blobs'])
        self.setBlobsPersisted(o['BlobsBeingPersisted'])
        self.setBlobsDegraded(o['BlobsDegraded'])
        self.setBlobsInCache(o['BlobsInCache'])
        self.setBlobsTotal(o['BlobsTotal'])
        self.setBucketId(o['BucketId'])
        self.setCreationDate(o['CreationDate'])
        self.setETag(o['ETag'])
        self.setId(o['Id'])
        self.setLatest(o['Latest'])
        self.setName(o['Name'])
        self.setOwner(o['Owner'])
        self.setSize(o['Size'])
        self.setType(o['Type'])

        # Physical Placement
        for obj in o['Blobs']['ObjectList']:
            # Tape Locations
            if(obj['PhysicalPlacement']['TapeList'] != None):
                for tape in obj['PhysicalPlacement']['TapeList']:
                    t = Tape()
                    t.importTape(tape)
                    self.TapeList.append(t)

    def setBlobs(self, b):
        if(b != None):
            blob = Ds3Blob()
            for ds3b in b['ObjectList']:
                blob.importBlob(ds3b)
                self.Blobs.append(blob)

    def setBlobsPersisted(self, b):
        self.BlobsBeingPersisted = b

    def setBlobsDegraded(self, b):
        self.BlobsDegraded = b

    def setBlobsInCache(self, b):
        self.BlobsInCache = b

    def setBlobsTotal(self, b):
        self.BlobsTotal = b

    def setBucketId(self, b):
        self.BucketId = b

    def setCreationDate(self, c):
        self.CreationDate = c

    def setETag(self, e):
        self.ETag = e

    def setId(self, i):
        self.Id = i

    def setLatest(self, l):
        self.Latest = l
    
    def setName(self, n):
        self.Name = n

    def setOwner(self, o):
        self.Owner = o

    def setSize(self, s):
        self.Size = s

    def setType(self, t):
        self.Type = t
    
    #============================================
    # Variables
    #============================================

    Blobs = []
    BlobsBeingPersisted = None
    BlobsDegrated = None
    BlobsInCache = None
    BlobsTotal = None
    BucketId = None
    CreationDate = None
    ETag = None
    Id = None
    Latest = None
    Name = None
    Owner = None
    Size = None
    Type = None
