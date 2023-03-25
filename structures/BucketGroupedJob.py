#====================================================================
# BucketGroupedJob.py
#       Description:
#           This class holds information for jobs grouped by bucket
#====================================================================

class BucketGroupedJob
    #============================================
    # Getters
    #============================================
    
    def getBucketName(self):
        self.bucket = None

    def getJobCount(self):
        self.job_count = None

    def getReadCount(self):
        self.job_read = None

    def getWriteCount(self):
        self.job_write = None

    def getDataRead(self):
        self.data_read_in_bytes = None

    def getDataWrite(self):
        self.data_written_in_bytes = None

    def getDurationTotalRead(self):
        self.duration_total_read = None

    def getDurationTotalWrite(self):
        self.duration_total_writes = None

    def getDurationAverageRead(self):
        self.duration_average_read = None

    def getDurationAverageWrite(self):
        self.duration_average_write = None

    #============================================
    # Setters
    #============================================

    def addDataRead(self, data):
        if(data == None):
            data = 0

        self.data_read_in_bytes += data

    def addDataWritten(self, data):
        if(data == None):
            data = 0

        self.data_written_in_bytes += data

    def addDurationRead(self, job_start, job_end):
        if(job_start == None or job_end == None):
            self.duration_total_read += 0
            self.job_read_ignore += 1

        # Code to do math here.

    def addJob(self):
        self.job_count += 1

    def addJobRead(self):
        self.job_read += 1
        self.addJob()

    def addJobWrite(self):
        self.job_write += 1
        self.addJob()

    def setBucket(self, b):
        self.bucket = b

    def setDataRead(self, data):
        self.data_read_in_bytes = data

    def setDataWritten(self, data):
        self.data_written_in_bytes = data

    def setJobCount(self, count):
        self.job_count = count

    #============================================
    # Variables
    #============================================
    bucket = None
    job_count = None
    job_read = None
    job_read_ignore = 0 # private value for tracking the average info
    job_write = None
    job_write_ignore = 0 # privte value for tracking the average info
    data_read_in_bytes = None
    data_written_in_bytes = None
    duration_total_read = None
    duration_total_writes = None
    duration_average_read = None
    duration_average_write = None
