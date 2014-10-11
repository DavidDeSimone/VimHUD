import sys
from mode import Mode
from modeslist import ModesList



# Parser class
# As Vim is a modular editor, we associate a 'Mode' object
# with each given Vim mode. That object finds text written
# in its mode, and parses commands based off of that
class Parser:
    def __init__(self, str):
        #The string to parse
        self.toParse = str;

        #An object that stores an array of all modes
        self.ModesList = ModesList()

        #The list of commands parsed from the string
        self.tokens = [];


    def parseStr(self):
        for mode in self.ModesList.Modes:
           
            #Parse and process the commands for the mode
            print 'Parsing...'
            print self.toParse
            mode.parse(self.toParse)
            mode.process()
            strs = mode.tokens

            #Extract the tokens for the mode
            #and add them to the complete list
            for str in strs:
               self.tokens.append(str)

    def printTokens(self):
        for x in xrange(0, len(self.tokens)):
            print self.tokens[x]


# Create the parser for the input file 
parse = Parser(sys.argv[1])
parse.parseStr()
parse.printTokens()
