#====================================================================
#   TapePartition.py
#       Description:
#           A container class for the tape partition information
#           returned by the SDK.
#====================================================================

class TapePartition:

    #============================================
    # Getters
    #============================================
    
    def getPartitionId(self):
        return self.partition_id

    def getName(self):
        return self.name

    #============================================
    # Setters
    #============================================
    
    def setAutoCompaction(self, d):
        self.auto_compaction = d

    def setAutoQuiesce(self, d):
        self.auto_quiesce = d

    def setDriveIdleTimeout(self, d):
        self.drive_idle_timeout = d

    def setDriveType(self, d):
        self.drive_type = d

    def setErrorMessage(self, d):
        self.error_message = d

    def setPartitionId(self, d):
        self.partition_id = d

    def setImportExportConfig(self, d):
        self.import_export_config = d

    def setLibraryId(self, d):
        self.library_id = d

    def setMinReadReserve(self, d):
        self.min_read_reserved_drives = d

    def setMinWriteReserve(self, d):
        self.min_write_reserved_drives = d

    def setName(self, d):
        self.name = d

    def setQuiesced(self, d):
        self.quiesced = d

    def setSerialNumber(self, d):
        self.serial_number = d

    def setState(self, d):
        self.state = d

    auto_compaction = None
    auto_quiesce = None
    drive_idle_timeout = None
    drive_type = None
    error_message = None
    partition_id = None
    import_export_config = None
    libary_id = None
    min_read_reserved_drives = None
    min_write_reserved_drives = None
    name = None
    quiesced = None
    serial_number = None
    state = None
