#!/usr/bin/env python3

import os
import sys
from os.path import expanduser
home = expanduser("~")


#######################################3
#	Check for Valid Flags
########################################

if len(sys.argv) > 1:
	downloadLink = sys.argv[1]
else:
	error = "Unable to comply. File URL not specified."
	print(error)
	exit()


