#====================================================================
# ObjectSummary.py
#   This is the output information for the list-objects command.
#====================================================================

class ObjectSummary:
    #============================================
    # Variables
    #============================================
    _id = None
    bucket_name = None
    creation_date = None
    etag = None
    in_cache = None
    owner = None
    name = None
    size = None
    version_id = None
    version_latest = None


    #============================================
    # Getters
    #============================================
   
    def getBucketName(self):
        return self.bucket_name

    def getCreationDate(self):
        return self.creation_date

    def getEtag(self):
        return self.etag

    def getId(self):
        return self._id

    def getInCache(self):
        return self.in_cache

    def getOwner(self):
        return self.owner

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def getVersionId(self):
        return self.version_id

    def getVersionLatest(self):
        return self.version_latest

    #============================================
    # Settors
    #============================================

    def setBucketName(self, b):
        self.bucket_name = b

    def setCreationDate(self, c):
        self.creation_date = c

    def setEtag(self, e):
        self.etag = e

    def setId(self, i):
        self._id = i

    def setInCache(self, i):
        self.in_cache = i

    def setOwner(self, o):
        self.owner = o

    def setName(self, n):
        self.name = n

    def setSize(self, s):
        self.size = s

    def setVersionId(self, v):
        self.version_id = v

    def setVersionLatest(self, v):
        self.version_latest = v
