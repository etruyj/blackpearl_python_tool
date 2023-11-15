#====================================================================
# ListObjects.py
#	Description:
#		Provides a list of objects in the specified bucket.
#====================================================================

import util.Logger as Logger
import util.convert.StorageUnits as StorageUnits
import util.io.ArgFilters as ArgFilters
from structures.ObjectSummary import ObjectSummary
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

def customList(bucket, filters, object_fetch_limit, starting_page, blackpearl, logbook):
    try:
        logbook.INFO("Creating custom list of objects in bucket [" + bucket + "]")
        logbook.DEBUG("Calling ArgFilters.parseParameters()...")
        filter_params = ArgFilters.parseParameters(filters)
        
        # Check to see if an object_name was specified.
        if("name" in filter_params):
            if(isinstance(filter_params["name"], list)):
                raise Exception("Invalid parameter. Object name must be a single field.")
            else:
                name = filter_params["name"]
                logbook.INFO("Querying for specific object: " + name)
        else:
            name = None

        if("fields" in filter_params):
            fields = filter_params["fields"]
        else:
            fields = "all"

        logbook.INFO("Returned fields will be: " + str(fields))
        logbook.DEBUG("Calling withPhysicalLocations()...")
        results = withPhysicalLocations(bucket, name, object_fetch_limit, starting_page, blackpearl, logbook)
        
        logbook.DEBUG("Calling summarizeResults()...")
        results["results_list"] = summarizeResults(bucket, results["results_list"], fields, logbook)

        return results
    except Exception as e:
        return e.__str__()


def summarizeResults(bucket, object_list, fields, logbook):
    if(fields == None or len(fields) == 0): # No filters were passed.
        fields = "all"

    results = []

    for obj in object_list:
        summary = ObjectSummary()

        summary.setName(obj.getName())

        if("all" in fields or "barcode" in fields):
            summary.setTapes(obj.getTapes())
        if("all" in fields or "bucket" in fields):
            summary.setBucketName(bucket)
        if("all" in fields or "created" in fields):
            summary.setCreationDate(obj.getCreationDate())
        if("all" in fields or "etag" in fields):
            summary.setEtag(obj.getETag())
        if("all" in fields or "id" in fields):
            summary.setId(obj.getId())
        if("all" in fields or "in_cache" in fields):
            summary.setInCache(obj.isInCache())
        if("all" in fields or "owner" in fields):
            summary.setOwner(obj.getOwner())
        if("all" in fields or "size" in fields):
            summary.setSize(StorageUnits.bytesToHumanReadable(obj.getSize()))
#        if("all" in fields or "version" in fields):
#            summary.setVersionId(obj.getVersionId())
#            summary.setVersionLatest(obj.isLatest())
        results.append(summary)
       
    return results


def withPhysicalLocations(bucket, prefix, object_fetch_limit, starting_object, blackpearl, logbook):
    logbook.INFO("Listing objects associated with bucket [" + bucket + "]")
   
    # Object fetch limit is the page length value. This field
    # determines how many objects will be returned by the query.
    if(starting_object == None):
        page_number = 0
    else:
        page_number = starting_object

    objects_remaining = 1
    results = {}
    details_list = []

    try:
        response = blackpearl.getObjectsWithFullDetails(bucket, prefix, object_fetch_limit, page_number, logbook)

        objects_remaining = response.paging_truncated
        total_objects = response.paging_total_result_count
        object_list = response.result['ObjectList']

        logbook.DEBUG("Retrieved " + str(len(object_list)) + " out of " + str(total_objects))
        logbook.DEBUG("there are " + str(objects_remaining) + " objects remaining.")

        for obj in object_list:
            page_number = obj['Id'] # Excessive assignments but automatically sets to the last in the list.
            if(obj['Type'] != "FOLDER"):
                details = ObjectDetails()
                details.importObject(obj)
                details_list.append(details)
      
        results["objects_remaining"] = objects_remaining
        results["starting_page"] = details_list[len(details_list)-1].getId() # starting page is the id of the last object returned
        results["results_list"] = details_list

        return results
    except Exception as e:
        return e.__str__()
