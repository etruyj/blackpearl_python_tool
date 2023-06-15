#====================================================================
# ListObjects.py
#	Description:
#		Provides a list of objects in the specified bucket.
#====================================================================

import util.Logger as Logger
from structures.sdk.Ds3Object import Ds3Object
from structures.sdk.ObjectDetails import ObjectDetails

import json

def createList(bucket, blackpearl, logbook):
    logbook.INFO("Creating list of objects for bucket [" + bucket + "].")

    try:
        logbook.DEBUG("Calling blackpearl.getBucket()")
        output = []

        object_info = blackpearl.getBucket(bucket, logbook)
   
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

def withPhysicalLocations(bucket, prefix, blackpearl, logbook):
    logbook.INFO("Listing objects associated with bucket [" + bucket + "]")
   
    page_length = 2
    page_number = 0
    objects_remaining = 1
    details_list = []

    try:
        while(objects_remaining > 0):
            response = blackpearl.getObjectsWithFullDetails(bucket, prefix, page_length, page_number, logbook)

            objects_remaining = response.paging_truncated
            total_objects = response.paging_total_result_count
            object_list = response.result['ObjectList']

            print("Printing results: 0-" + str(2) + " out of " + str(total_objects))
            print("there are " + str(objects_remaining) + " objects remaining.")

            for obj in object_list:
                page_number = obj['Id'] # Excessive assignments but automatically sets to the last in the list.
                if(obj['Type'] != "FOLDER"):
                    details = ObjectDetails()
                    details.importObject(obj)
                    details_list.append(details)

    except Exception as e:
        return e.__str__()
