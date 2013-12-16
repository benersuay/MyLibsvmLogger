# Halit Bener Suay
# benersuay@wpi.edu
# December, 2013
#
# A class of data logger that saves the data in libsvm format
#
# Usage
# 
# Import the module
# from MyLibsvmLogger import *
#
# Get an instance
# logger = MyLibsvmLogger()
#
# Add data to your log
# logger.append([label, attr1Instance, ..., attrNInstance])
#
# Whenever you're done
# logger.save_and_close()
#
# One could also do
# 
# logger.load_from_pickle(myPickleFileName)
# logger.save_and_close()

import time
import pickle

class MyLibsvmLogger():
    def __init__(self,fname=None):
        self.startTime = time.strftime("%Y-%m-%d-%H-%M-%S") # Get the time-stamp for naming the file
        if(fname == None):
            self.fname = str(self.startTime) # Name the txt file
        else:
            self.fname = fname
        self.log = []
        self.format = ".txt"
        
    def append(self,entry):
        self.log.append(entry)

    def save_and_close(self,doPickle=False):
        try:
            logWriter=open(self.fname+self.format,"w");

            for e in self.log:
                thisEntry = str(int(e[0])) # make sure label is integer
                for aIdx, a in enumerate(e[1:]):
                    # don't save if the feature is zero
                    if(a != 0.0 or a != 0): 
                        thisEntry += " "+str(aIdx+1)+":"+str(a)
                thisEntry += "\n"    
                logWriter.write(thisEntry)

            logWriter.close()
        except Exception, err:
            print "Error saving file: "+self.fname+self.format
            print err


        try:
            if(doPickle):
                pickle.dump(self.log, open(self.fname+".p","wb"))
        except Exception, err:
            print "Error pickling file: "+self.fname+".p"
            print err

    def load_from_pickle(self,pickleFileName):
        try:
            self.log = pickle.load(open(pickleFileName,"rb"))
        except Exception, err:
            print "Error loading file: "+pickleFileName
            print err
