#====================================================================
# Ds3Blob.py
#   Description:
#       This class holds blob information returned by the SDK commands.
#====================================================================

from structures.sdk.Tape import Tape

class Ds3Blob:
    #============================================
    # Getters
    #============================================
    #============================================
    # Setters
    #============================================

    def importBlob(self, b):
        self.setBucket(b['Bucket'])
        self.setId(b['Id'])
        self.setInCache(b['InCache'])
        self.setLatest(b['Latest'])
        self.setLength(b['Length'])
        self.setName(b['Name'])
        self.setOffset(b['Offset'])
        self.setVersionId(b['VersionId'])
        self.setPhysicalPlacement(b['PhysicalPlacement'])

    def setBucket(self, b):
        self.Bucket = b

    def setId(self, i):
        self.Id = i

    def setInCache(self, i):
        self.InCache = i

    def setLatest(self, l):
        self.Latest = l

    def setLength(self, l):
        self.Length = l

    def setName(self, n):
        self.Name = n

    def setOffset(self, o):
        self.Offset = o

    def setVersionId(self, v):
        self.VersionId = v

    def setPhysicalPlacement(self, p):
        placement = Placement()
        placement.addLocations(p)
        self.PhysicalPlacement = placement

    #============================================
    # Variables
    #============================================

    Bucket = None
    Id = None
    InCache = False
    Latest = None
    Length = None
    Name = None
    Offset = None
    VersionId = None
    PhysicalPlacement = None

class Placement:
    #============================================
    # Getters
    #============================================
    #============================================
    # Setters
    #============================================

    def addLocations(self, locations):
        if(len(locations['TapeList']) > 0):
            self.TapeList = self.addTapeLocations(locations['TapeList'])

    def addTapeLocations(self, tape_locations):
        tape_list = []

        for t in tape_locations:
            try:
                tape = Tape()
                tape.importTape(t)
                tape_list.append(tape)
                print(tape.getBarcode())
            except Exception as e:
                print(t)
                raise e
  
        return tape_list

    #============================================
    # Variables
    #============================================

    S3TargetList = []
    AzureTargetList = []
    Ds3TargetList = []
    TapeList = []
    PoolList = []
