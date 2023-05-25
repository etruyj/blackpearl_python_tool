# blackpearl_python_tool (nacre)
The blackpearl_python_tool (script name: nacre) is a Python 3.10 script to interact with the BlackPearl via both the management and data ports. Which port is determined by the operation desired. Access to both network addresses is recommended as this script allows for DS3 access without having to know a users access_key and secret_key. Those can be retrieved for the user after logging in with UI credentials.

## Commands  
configure&emsp;&emsp;Configure the BlackPearl with the specified --file in JSON format.

## Options 
--access-key(-a)&emsp;DS3 access key for data path authentication.  
--command(-c)&emsp;Command to execute. Found from the list above.  
--endpoint(-e)&emsp;IP address of either the management port or the data port of the BlackPearl depending on which pair of access credentials are used.  
--file&emsp;&emsp;Input/Output file path for commands.  
--password(-p)&emsp;GUI password for management path authentication.  
--secret-key(-k)&emsp;DS3 secret key for data path authentication.  
--user(-u)&emsp;&emsp;GUI username for management path authentication.  

## Configure the BlackPearl
