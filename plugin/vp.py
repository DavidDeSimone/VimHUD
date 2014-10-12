import sys
from mode import Mode
from modeslist import ModesList
from processor import Processor


# Parser class
# As Vim is a modular editor, we associate a 'Mode' object
# with each given Vim mode. That object finds text written
# in its mode, and parses commands based off of that
class Parser:
    def __init__(self, str):
        #The string to parse
        self.toParse = str;

        #An object that stores an array of all modes
        self.ModesList = ModesList(self.toParse)

        #The list of commands parsed from the string
        self.tokens = [];


    def parseStr(self):
        for mode in self.ModesList.Modes:

            #Parse and process the commands for the mode
            print self.toParse
            mode.parse()
            strs = mode.tokens

            #Extract the tokens for the mode
            #and add them to the complete list
            for str in strs:

               print 'String ' + str

               self.tokens.append(str)

    def printTokens(self):
        for mode in self.ModesList.Modes:
            tokList = mode.tokens

            print 'Printing ' + mode.name
            for tok in tokList:
                print 'Token ' + tok

    def update(self):
        f = open('~/.vimlog', 'r+')
        print 'File Opened'
        lines = f.read()
        
        parse = Parser(lines)
        parse.parseStr()


        for mode in self.ModesList.Modes:
            tokList = mode.tokens

            for tok in tokList:
                self.addFreq(tok)



        'Cleaning File...'
        f.seek(0)
        f.truncate()
        f.close()


        def addFreq(self):
            f = open('user_short_stats.txt')

            self.clean(f)

            lines = f.readlines()

            for line in lines:
               seps = string.split(line, '\t')
                if len(line) == 2:
                    lrt = ""

                    com = seps[0]
                    freq = seps[1]

                    freq_int = int(freq) + '\t'
                    freq_int += 1

                    freq = str(freq_int) + '\n'

                    lrt += com
                    lrt += freq

                    


        def clean(self, f):
            lines = f.readlines()

            lrt = ""

            for line in lines:
                seps  = string.split(line, '\t')
                if len(seps) == 2:

                    com = seps[0]
                    freq = seps[1]

                    freq_int = 1
                    freq = str(freq_int) = '\n'

                    lrt += com + '\t'
                    lrt += freq

                    f.write(lrt)



# Create the parser for the input file
#parse = Parser(sys.argv[1])
#parse.parseStr()
#parse.printTokens()
