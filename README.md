# blackpearl_python_tool (nacre)
The blackpearl_python_tool (script name: nacre) is a Python 3.10 script to interact with the BlackPearl via both the management and data ports. Which port is determined by the operation desired. Access to both network addresses is recommended as this script allows for DS3 access without having to know a users access_key and secret_key. Those can be retrieved for the user after logging in with UI credentials.

## Commands  
configure&emsp;&emsp;Configure the BlackPearl with the specified --file in JSON format.

configure           Configure the BlackPearl with the specified json configuration file. Requires --endpoint, --username, --password, --file.  
delete-object       Deletes objects from the BlackPearl. Specify --bucket and --file listing the objects to be deleted.  
get-database        Downloads the most recent BlackPearl database to the downloads directory. A different file name can be specified with --file. A different directory can be specified with --path. A prefix, such as hostname, can be added to the file with --prefix.  
eject-tape          Issues the command for the BlackPearl to move the tape specified by --barcode or tapes listing in tape list --file from storage slots to entry/exit. Use [--max-moves | --moves] to specify entry/exit size. The plural eject-tapes also works.  
export-tape         Issues the command for the BlackPearl to move the tape specified by --barcode or tapes listing in tape list --file from storage slots to entry/exit. Use [--max-moves | --moves] to specify entry/exit size. The plural export-tapes also works.  
job-report          Provides a list of data written and read from a bucket over the desired period. Accepts --filter [ days | hours ]:INTEGER  
list-buckets        Provides a list of all buckets visible to the user on the BlackPearl  
put-object          Puts an object to the BlackPearl. Specify --bucket, --file, and (optionally) --key to rename the object.  
tape-report         Creates a report of all the tapes in the library. --group-by can group results by a field. --filter can filter the results. 


## Options 
--access-key(-a) | BlackPearl user ds3 access key (only required if connecting to the data path).
--barcode | The tape barcode 
--bucket            The bucket name 
--command(-c)       The command to execute 
--endpoint(-e)      The IP address or URL of the management port or data port of the BlackPearl  
--file              Specify a file name for read from or write to operations  
--filter            Specify a key value pair to filter by such as barcode, state, and status. Example --filter state:scratch.  
                        Accepted values:  
                            - tape-report: barcode:PARTIAL_STRING, state:[NORMAL | EJECTED | LOST], status:[ blank | scratch | in-use ]  
--group-by          Specify a field to group tape report items by. Accepted values: bucket  
--key               The key (name) of the object.  
--max-moves/--moves Specify the maximum number of moves to execute. Used to control for available EE slots.  
--output-format     The formatting to use for output. Options: csv | table  
--password(-p)      BlackPearl login password  
--path              The path to a file directory.  
--secret-key(-k)    BlackPearl user ds3 secret key (only required if connecting to the data path).   
--username(-u)      BlackPearl login username  

## Operating Systems
Three binaries exist for the log parser depending on the operating system. All three binaries can be located in the bin/ directory of this script. ./nacre is the Linux version of the script (specifically compiled with Ubuntu 22). Some Debian and Redhat versions do not have the required dependencies to use this script. In this case, a Docker container can be used to create an Ubuntu environment for this script. ./nacre_osx is the MacOs version of the script. This is compiled and tested with MacOS. ./nacre_win.exe is the Windows executable for this script. It's compiled and tested with Windows 10. 

## Command Examples
All examples will us the Linux version of the script. The functionality is the same through all three binaries. To use these scripts with a different operating system, swap the command to use the binary corresponding to the desired operating system.

### Configure the BlackPearl
A configuration JSON can be used by the script to create buckets, data policies, storage domains, pools, volumes, and NAS shares. It can also be used to add activation keys to the BlackPearl. The expected uses for this script would be to refresh the BlackPearl from logs after a re-image, a chassis swap, or in the event of a catastrophic event that causes configuration loss. This script can also be used for the automated deployment of multiple BlackPearls off a basic configuration. A configuration can be pulled from BlackPearl logs via the BlackPearl log parser.
 
> ./nacre -e MGMT_IP -u USERNAME -p PASSWORD -c configure --file path/to/config.json

### Delete Objects
This script can be used to simplify object deletes either by specifying an individual file or specifying a file listing all the objects to be deleted. Two options are presented at the beginning of this script. The user can either DELETE ALL files specified by either method or VERIFY each file before the delete command is executed. DELETE ALL will not take any additional inputs and all objects will be deleted. VERIFY will provide a prompt for each object to be deleted and require DELETE to be entered to confirm the deletion of the object. This script will create an audit log of all objects deleted with the command. This log is stored in the log/ directory and put back into the target bucket to create a record of the deletes.

> ./nacre -e MGMT_IP -u USERNAME -p PASSWORD -c delete-objects --bucket BUCKET --file path/to/delete_list.txt

### Download Most Recent Database
This python tool can be used to download the most recent version of the BlackPearl database backup to local storage. This workflow can be used as an added backup to the BlackPearl's internal database backup process. If no additional flags are provided the database will be downloaded to the Downloads/ directory of the local machine and retain the object name in the BlackPearl bucket. A --prefix can be applied in front of the file name to distinguish the logset, such as in environments with multiple BlackPearls. A different download location can be specified with the --path parameter. A full path/file-name.tar.xz can be explicitly defined with the --file flag. These flags can be mixed and combined to get the desired output with the exception of explicitly defining the file name (--file).

#### Default command
> ./nacre -e MGMT_IP -u USERNAME -p PASSWORD -c get-database

#### Download to Desktop
> ./nacre -e MGMT_IP -u USERNAME -p PASSWORD -c get-database --path ~/Desktop

#### Add a prefix "BP1" to the backup.
> ./nacre -e MGMT_IP -u USERNAME -p PASSWORD -c get-databse --prefix BP1

#### Download the backup to Deskop with the name bp_backup.
> ./nacre -e MGMT_IP -u USERNAME -p PASSWORD -c get-database --file ~/Desktop/bp_backup.tar.xz


