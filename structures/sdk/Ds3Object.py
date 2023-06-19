#====================================================================
# Ds3Object.py
#   Description:
#       A container class for the objects returned by SDK getBucket()
#       command.
#====================================================================

class Ds3Object:
    #============================================
    # Getters
    #============================================
    def getEtag(self):
        if(self.etag == None):
            return "none"
        else:
            return self.etag

    def getIsLatest(self):
        if(self.is_latest == None):
            return "none"
        else:
            return self.is_latest

    def getKey(self):
        if(self.key == None):
            return "none"
        else:
            return self.key

    def getLastModified(self):
        if(self.last_modified == None):
            return "never"
        else:
            return self.last_modified

    def getOwnerDisplayName(self):
        if(self.owner_display_name == None):
            return "none"
        else:
            return self.owner_display_name

    def getOwnerId(self):
        if(self.owner_id == None):
            return "none"
        else:
            return self.owner_id

    def getSize(self):
        if(self.size == None):
            return 0
        else:
            return self.size

    def getStorageClass(self):
        if(self.storage_class == None):
            return "none"
        else:
            return self.storage_class

    def getVersionId(self):
        if(self.version_id == None):
            return "none"
        else:
            return self.version_id

    #============================================
    # Setters
    #============================================
    def setEtag(self, e):
        self.etag = e

    def setIsLatest(self, i):
        self.is_latest = i

    def setKey(self, k):
        self.key = k

    def setLastModified(self, l):
        self.last_modified = l

    def setOwner(self, display_name, owner_id):
        self.owner_display_name = display_name
        self.owner_id = owner_id

    def setSize(self, s):
        self.size = s

    def setStorageClass(self, s):
        self.storage_class = s

    def setVersionId(self, v):
        self.version_id = v

    #============================================
    # Vars
    #============================================
    etag = None
    is_latest = None
    key = None
    last_modified = None
    owner_display_name = None
    owner_id = None
    size = None
    storage_class = None
    version_id = None
