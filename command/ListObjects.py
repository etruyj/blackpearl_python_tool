#====================================================================
# ListObjects.py
#	Description:
#		Provides a list of objects in the specified bucket.
#====================================================================

import util.Logger as Logger
from structures.sdk.Ds3Object import Ds3Object

def createList(blackpearl, bucket, logbook):
    logbook.INFO("Creating list of objects for bucket [" + bucket + "].")

    try:
        logbook.DEBUG("Calling blackpearl.getObjects()")
        output = []

        object_info = blackpearl.getObjects(bucket, logbook)
   
        if(object_info == None):
            logbook.ERROR("Unable to return objects for the specified bucket.")
        else:
            for ds3_object in object_info:
                info = Ds3Object()
                
                info.setEtag(ds3_object['ETag'])
                info.setIsLatest(ds3_object['IsLatest'])
                info.setKey(ds3_object['Key'])
                info.setLastModified(ds3_object['LastModified'])
                info.setOwner(ds3_object['Owner']['DisplayName'], ds3_object['Owner']['ID'])
                info.setSize(ds3_object['Size'])
                info.setStorageClass(ds3_object['StorageClass'])
                info.setVersionId(ds3_object['VersionId'])

                output.append(info)

        return output
    except Exception as e:
        print(e.__str__())
