#====================================================================
# BucketGroupedJob.py
#       Description:
#           This class holds information for jobs grouped by bucket
#====================================================================

class BucketGroupedJob:
    #============================================
    # Getters
    #============================================
    
    def getBucket(self):
        return self.bucket

    def getJobCount(self):
        return self.job_count 

    def getReadCount(self):
        return self.job_read 

    def getWriteCount(self):
        return self.job_write 

    def getDataRead(self):
        return self.data_read_in_bytes 

    def getDataWrite(self):
        return self.data_written_in_bytes 

    def getDurationTotalRead(self):
        return self.duration_total_read 

    def getDurationTotalWrite(self):
        return self.duration_total_writes 

    def getDurationAverageRead(self):
        return self.duration_average_read 

    def getDurationAverageWrite(self):
        return self.duration_average_write

    #============================================
    # Setters
    #============================================

    def addDataRead(self, data):
        if(data == None):
            data = 0

        self.data_read_in_bytes += int(data)

    def addDataWritten(self, data):
        if(data == None):
            data = 0

        self.data_written_in_bytes += int(data)

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
    job_count = 0
    job_read = 0
    job_read_ignore = 0 # private value for tracking the average info
    job_write = 0
    job_write_ignore = 0 # privte value for tracking the average info
    data_read_in_bytes = 0
    data_written_in_bytes = 0
    duration_total_read = 0
    duration_total_writes = 0
    duration_average_read = 0
    duration_average_write = 0
