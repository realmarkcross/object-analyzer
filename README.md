# Application Purpose

---
The purpose of this application is to provide a command line tool to query the AWS cloud provider for S3 information.

*Please note the following from python.org:*
Due to the way most Linux distributions are handling the Python 3 migration, Linux users using the system Python 
without creating a virtual environment first should replace the python command in this tutorial with python3 and the 
pip command with pip3 --user. Do not run any of the commands in this tutorial with sudo: if you get a permissions error,
 come back to the section on creating virtual environments, set one up, and then continue with the tutorial as written.


### Platform-Specific Installation Details for Mac and Ubuntu Users:
1. Download the object-analyzer package with files.

2. Ensure the first line of main.py is:
`#!/usr/bin/env python3`

or if using Python3 installed via Homebrew:
    #!/usr/local/bin/python3

3. In Terminal, locate and navigate to the location of the main.py file and make the file executable with:
    chmod +x main.py

4. Make sure you're in the folder with main.py and execute the application with:
    ./main.py


*NOTE: To create a desktop launcher for the application:*

Open the file called desktop.launcher and update the following:
`    Exec = /path-to-files/main.py`

(If you would like an icon for the desktop launcher, please include the following line:
`Icon = /path-to-icon-file/name-of-icon.ext`

Copy the desktop.launcher to the desktop (or other location) and the application should open.

### Command-line options (flags):

---

*You may also type main.py -h to get a list of the available options described below:*

`-u` or `--unit`

- specifies the unit of measure applicable to file size.  
- options include b for bytes (default), kb for kilobytes, mb for megabytes, or gb for gigabytes

example usage: `python main.py -u kb`

`-f or --format`

- specifies the format of the returned data.  
- options include object=python dictionary or pretty=pretty formatted (default.)

example usage: `main.py -f object`

`-r or --resource` (for future use)

this option enables additional future AWS services to be added to the tool such as EC2 or any other API addressable services.


### Application Requirements

---

The application requires Python3 and the boto3 package from Amazon.  
If boto3 is not automatically installed when you run the application, it will need to be installed via PIP with:
```pip install boto3```
    
This tool makes the following assumptions:
- that you have already created your AWS credentials using the AWS CLI and that they are located in:
    ~/.aws/credentials
- that the AWS region was already set using the same tool noted in the previous step.

If you have not run the AWS CLI tool yet, please download the AWS CLI tool and run the command 'aws configure' before proceeding.
More information here: (https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)

**Command Line Tool Documentation**

The tool currently returns a select amount of information based on a specific set of requirements:

- S3 Bucket Name
- Bucket Creation Date
- Number of Files (Object keys) in the Bucket
- Total size of the Files (Object keys) in the Bucket
- Last Modified Date of the most recently modified file

You may use the tool by simply calling Python from the command line followed by the main.py file name, like this:

```python main.py (options/flags)```

You can choose to have the output formatted in a Python dictionary or with pretty print with the --format option (see flag descriptions above.)

You can also choose to have the size of the files displayed in bytes, kilobytes, megabytes or gigabytes with the --unit option (see flag descriptions above.)

End of File
    
 
