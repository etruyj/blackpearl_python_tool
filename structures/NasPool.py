# NasPool.py
#   Description:
#       A container for all the settings necessary to set-up a 
#       NAS Pool.
#
#   Subclasses:
#       - Topology
#       - Children

class Children:

    def __init__(self, disk_id, size, disk_type):
        self.children = []
        self.disk_id = disk_id
        self.size = size
        self.disk_type = disk_type

    def diskId(self):
        return self.disk_id

    def size(self):
        return self.size

    def type(self):
        return self.disk_type

    def setDiskId(self, disk):
        self.disk_id = disk

    def setSize(self, s):
        self.size = s

    def setDiskType(self, t):
        self.disk_type = t

class Stripe:

    def __init__(self, parity):
        self.children = []
        self.stripe_type = parity

    def addDisk(self, disk_id, size, disk_type):
        self.children.append(Children(disk_id, size, disk_type))

    def count(self):
        return len(self.children)

    def diskId(self, i):
        return self.children[i].diskId()

    def diskType(self, i):
        return self.children[i].diskType()

    def size(self, i):
        return self.children[i].size()

    def type(self):
        return stripe_type

class NasPool:
    name = 0
    power_saving_mode = "disabled"

    def __init__(self, parity, stripe_count):
        # Var declaration
        self.topology = []
        self.children = []
        self.disk_ids = []
        self.zil_drives = []
        self.type = "pool"
        self.health = None
        self.size = None
        self.high_water_mark = 80
        self.raw_size = 0
        self.used = 0

        # Var assignment
        self.stripes = stripe_count
        self.protection = parity
        self.protection_select = parity
        # topology is actually an array of a Stripes
        self.addStripeToTopology(parity)

    def addDiskToStripe(self, stripe, physical_path, size, disk_type):
        if(stripe < len(self.topology)):
            self.disk_ids.append(physical_path)

            self.topology[stripe].addDisk(physical_path, size, disk_type)
        else:
            return False

    def addStripeToTopology(self, parity):
        self.topology.append(Stripe(parity))

    def getStripeDiskCount(stripe):
        return len(self.topology[stripe].count())

    def getStripeDiskSize(stripe, disk):
        return self.topology[stripe].size(disk)

    def calcSizes(self):
        # Calculate the total size of the disks
        for stripe in range(0, len(self.topology)):
            for disk in range(0, len(self.getStripeDiskCount(stripe))):
                self.raw_size += self.getStripeDiskSize(stripe, disk)

        # Calculate the overhead
        # var declaration and for case "none"
        self.overhead = 0
        match(protection):
            case "mirror":
                self.overhead = self.raw_size / 2
            case "single":
                for stripe in range(0, len(self.topology)):
                    if(self.getStripeDiskCount(stripe) > 0):
                        # Only need one of the disks for overhead in 
                        # single parity mode. Grab the size of the first.
                        self.overhead += self.getStripeDiskSize(stripe, 0)
            case "double":
                for stripe in range(0, len(self.topology)):
                    if(self.getStripeDiskCount(stripe) > 1):
                        # Only need two of the disks for overhead in
                        # double parity mode. Grab the size of the first two.
                        self.overhead += self.getStripeDiskSize(stripe, 0)
                        self.overhead += self.getStripeDiskSize(stripe, 1)

        # Calc the availale space
        # Available = raw_size - overhead
        self.available = self.raw_size - self.overhead

    def name():
        return self.name

    def setName(n):
        self.name = n

    def setPowerMode(mode):
        self.power_saving_mode = mode

    def stripeCount(self):
        return len(self.topology)
