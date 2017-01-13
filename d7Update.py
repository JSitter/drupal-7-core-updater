#!/usr/bin/env python3

import zipfile
import os
import sys
from os.path import expanduser
home = expanduser("~")

updaterDir = home + "/pyD7Updater/"
saveLoc = updaterDir + "d7.zip"

import urllib.request

#######################################3
#	Check for Valid Flags
########################################

if len(sys.argv) > 1:
	downloadLink = sys.argv[1]
else:
	error = "Unable to comply. File URL not specified."
	print(error)
	exit()
#Check if upload directory has been created
if not os.path.isdir(updaterDir):
	os.makedirs(updaterDir)
	os.makedirs(updaterDir + "/extracts/")

#download zip file
urllib.request.urlretrieve(downloadLink, saveLoc)

zipRef = zipfile.ZipFile(saveLoc, 'r') 
print(zipfile.ZipFile.printdir)
zipRef.extractall(updaterDir + "/extracts/")
#print(zipfile.ZipFile.namelist())
zipRef.close()


