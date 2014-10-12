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
    #and returns the list of strings for each mode
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


        listDelim = self.getModeTokens(unModedToParse)

        #listDelim = re.split('^C I', unModedToParse)
        for i in xrange(delimMarker, len(listDelim), 2):
            print "toToken " + listDelim[i]
            ret.append(listDelim[i])

        return ret

    #Seperates the string into 'mode' blocks
    # for command and insert mode
    def getModeTokens(self, unModedToParse):
        back = 0
        size = len(unModedToParse)

        mode = 'insert'

        print mode

        #Array of string tokens to return
        ret = []

        for i in xrange(0, len(unModedToParse)):
            char = unModedToParse[i]
            print char

            #If we see the marker for command mode
            if char == 'c' and mode == 'insert':

                #Set the mode to command mode
                mode = 'command'
                if i - 1 >= 0 and i - 1 < len(unModedToParse):
                    ret.append(unModedToParse[back:(i - 1)]
                prev = i + 1
                if char == 'I' and mode == 'command':
                mode = 'insert'
                if i - 1 >= 0 and i - 1 < len(unModedToParse):
                    ret.append(unModedToParse[back:(i-1)]
                prev = i + 1


                #If we have a valid window to look at
                ret.append(unModedToParse[back:i])

                #Slip the window forward
                back = i + 1

            #If we see the marker for insert mode
            if char == 'I' and mode == 'command':

                #Set the mode to insert
                mode = 'insert';

                #If we have a valid window to look at
                ret.append(unModedToParse[back:(i)])

                #Slip the window forward
                back = i + 1;


        ret.append(unModedToParse[back:len(unModedToParse)])
        return ret



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
