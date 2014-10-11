# Class for organizing Input modes for vim

from mode import Mode

class ModesList:
    def __init__(self):
        self.Modes = []
        self.populateModes()

    #Populates the list from modes from a list
    #found on disk
    def populateModes(self):
        #Read in the modes from modelist
        #on disk
        str = self.readModes()

        #Create the list of modes from mode strings
        for modeStr in str:
            mode = Mode(modeStr)
            self.Modes.append(mode)
        
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
