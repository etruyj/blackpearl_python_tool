#====================================================================
# Job.py
#   Description:
#       This class acts as a container for the job information returned
#       by the API for the active, cancelled, and completed jobs.
#====================================================================

class Job:
    #============================================
    # Getters
    #============================================
    def getBucketId(self):
        return self.bucket_id

    def getCachedSize(self):
        return self.cached_size_in_bytes
    
    def getChunkProccessOrder(self):
        return self.chunk_client_processing_order_guarante
    
    def getCompletedSize(self):
        return self.completed_size_in_bytes
    
    def getCreatedAt(self):
        return self.created_at
    
    def getDateCompleted(self):
        return self.date_completed

    def getErrorMessage(self):
        return self.error_message

    def getId(self):
        return self.job_id

    def getNaked(self):
        return self.naked

    def getName(self):
        return self.name

    def getOriginalSize(self);
        return self.original_size_in_bytes

    def getPriority(self):
        return self.priority
    
    def getRechunked(self):
        return self.rechunked

    def getRequestType(self):
        return self.request_type

    def getTruncated(self):
        return self.truncated

    def getUserId(self):
        return self.user_id
    #============================================
    # Setters
    #============================================
    def setBucketId(self, bid):
        self.bucket_id = bid

    def setCachedSize(self, in_bytes):
        self.cached_size_in_bytes = in_bytes
    
    def setChunkProccessOrder(self, order):
        self.chunk_client_processing_order_guarante = order
    
    def setCompletedSize(self, in_bytes):
        self.completed_size_in_bytes = in_bytes
    
    def setCreatedAt(self, date_time):
        self.created_at = date_time
    
    def setDateCompleted(self, date_time):
        self.date_completed = date_time

    def setErrorMessage(self, msg):
        self.error_message = msg

    def setId(self, jid):
        self.job_id = jid

    def setNaked(self, t):
        self.naked = t

    def setName(self, n):
        self.name = n

    def setOriginalSize(self, in_bytes);
        self.original_size_in_bytes = in_bytes

    def setPriority(self, p):
        self.priority = p
    
    def setRechunked(self, r):
        self.rechunked = r

    def setRequestType(self, rtype):
        self.request_type = rtype

    def setTruncated(self, trunc):
        self.truncated = trunc

    def setUserId(self, uid):
        self.user_id = uid
             
    #============================================
    # Variables
    #============================================
    bucket_id = None
    cached_size_in_bytes = None
    chunk_client_processing_order_guarante = None
    completed_size_in_bytes = None
    created_at = None
    date_completed = None
    error_message = None
    job_id = None
    naked = None
    name = None
    original_size_in_bytes = None
    priority = None
    rechunked = None
    request_type = None
    truncated = None
    user_id = None

