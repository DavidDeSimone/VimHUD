# Class for organizing Input modes for vim

import string
import re
from mode import Mode

class ModesList:
    def __init__(self, unModedToParse):
        self.Modes = []
        self.populateModes(unModedToParse)

    #Populates the list from modes from a list
    #found on disk
    def populateModes(self, unModedToParse):
        #Read in the modes from modelist
        #on disk
        str = self.readModes()

        #Create the list of modes from mode strings
        for modeStr in str:

            #Create the string for the mode
            toParse = self.getModedString(modeStr, unModedToParse) 

            #Passes the mode, and the array of string to parse
            mode = Mode(modeStr, toParse)
            self.Modes.append(mode)
    


    #Parses the string for the current mode
    #and returns 
    def getModedString(self, modeStr, unModedToParse):
        ret = []

        #Knowing we always start in Insert mode,
        #if we delimit by I and \ESC, we will get
        #our tokens based on the parity of the
        #delimMarker
        delimMarker = 0

        if modeStr == "command":
            delimMarker = 1
        else:
            delimMarker = 0
         

        listDelim = getModeTokens(unModedToParse)

        #listDelim = re.split('^C I', unModedToParse)
        for i in xrange(delimMarker, len(listDelim), 2):
            print "toToken " + listDelim[i]
            ret.append(listDelim[i])
            
        return ret

    #Seperates the string into 'mode' blocks
    # for command and insert mode
    def getModeTokens(unModedToParse):
        front = 0
        back = 0
        size = len(unModedToParse)

        

        while front < size:
            
            


    

    #Reads the modes list from disk and 
    #returns a string array
    def readModes(self):
        modearray = [];

        modeFile = open("modes.txt");

        content = modeFile.readlines();
        for line in content:
            #Mode strings will be in the form
            #<mode name> <starting char>
            #list = string.split(line)



            modearray.append(line.rstrip());
            
        return modearray;
