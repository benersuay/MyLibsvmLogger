#!/usr/bin/env python
#
# Halit Bener Suay
# benersuay@wpi.edu
#
# December, 2013

from MyLibsvmLogger import *

# Get an instance of the logger. 
# You can pass in a file name if you'd like to MyLibsvmLogger("my_log")
logger = MyLibsvmLogger()

# Add data
logger.append([1, 0.15, -0.3, 0.8])
logger.append([0, -0.1, 0.3, 0.95])

# Save and close in txt format (human readable)
logger.save_and_close()

# Save and close in a binary file
logger.save_and_close(doPickle=True)
