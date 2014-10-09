# Class for organizing Input modes for vim
class ModesList:
    def __init__(self):
        self.Modes = [];
        self.populateModes();

    #Populates the list from modes from a list
    #found on disk
    def populateModes(self):
        str = self.readModes()

        #Create the list of modes from disk
        for modeStr in str:
            mode = Mode(modeStr);
            Modes.append(mode);
        
    #Reads the modes list from disk and 
    #returns a string array
    def readModes(self):
        modearray = [];

        modeFile = open("modes.txt");

        content = modeFile.readlines();
        for line in content:
            modearray.append(line);
