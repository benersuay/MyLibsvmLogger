MyLibsvmLogger
=============

A Python module that can save a 2D array to a txt file in libsvm format.


## Usage ##

Import the class

    from MyLibsvmLogger import *

Get an instance

    logger = MyLibsvmLogger()

Add data to your log

    logger.append([label, attr1Instance, ..., attrNInstance])

Whenever you're done.

    logger.save_and_close()

In addition, if you want to pickle your log array

    logger.save_and_close(doPickle=True)

One could also do

    logger.load_from_pickle(/my/Pickle/FileName)
    logger.save_and_close()
