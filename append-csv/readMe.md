#Append CSV File

 This program is quite simple and its purpose is to append the following:
	'https://spscommerce.atlassian.net/browse/' to any column specified by the user.
	User will select a '.csv' file, can select an optional output directory, and will 
	input a column number they want to append to.

## Setup as a .exe
There are a few options to make a .exe file
```
py2exe, only works on windows
PyInstaller, works on windows and Linux
Py2app will work for Macs
```
	
There are a whole host of options available for setting this up to run cross-platforms	
In my case I used py2exe. 
Install py2exe, open cmd window in the same directory as the three files in this folder
run the following:
```
$ python setup.py py2exe
```
This will create the necessary distro folder with your Main.exe
  
###Author
  
  jpjohnson571
