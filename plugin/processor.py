# Class for determining common vim patterns
# in people's input to power suggestion engine
#
# Accomplishes this by matching patterns found in regex.txt
# against the strings passed to the contructor

import string
import re

class Processor:

    #Constructor for the command processor
    #Passed two arguments
    #   mode, the current moade for the string being parsed
    #   toParse, the string to be parsed for regexs
    #   sugg, the suggested command to use instead of the
    #   key commands used
    def __init__(self, mode, toParse):
        self.mode = mode
        self.toParse = toParse
        self.regexs = []
        self.desc = []
        self.sugg = []

    #Reads in the list of regexs from disk
    #and checks to see if they are contained in
    #the passed string toParse
    def process(self):
        f = open(self.mode + '_regex.txt')

        regexFull = f.readlines()
        self.processRegex(regexFull)

        for regex in self.regexs:
            regexp = re.compile(regex)
            if regexp.search(self.toParse) is not None:
                self.getSuggestion(regex)



    def getSuggestion(self, regex):
        for i in xrange(0, len(self.regexs)):
            if regex == self.regexs[i]:
                for sug in self.sugg[i]:
                    self.recordFreq(sug)


    #Function used to reading regexs in from disk
    #Regexs are found in <mode>_regex.txt with the following format
    #<regular expression>\t<single line description of regex>
    def processRegex(self, regexFull):
        #print regexFull
        for line in regexFull:
            #We ignore all lines begininng with '#'
            if line[0] != '#':
                ls = string.split(line, '\t')
                #print ls
                self.regexs.append(ls[0])
                self.desc.append(ls[2])
                #self.sugg.append(ls[2])

                suggs = []

                for i in xrange(3, len(ls)):
                        suggs.append(ls[i].rstrip())
                        #print 'Sugg ' + ls[i]

                self.sugg.append(suggs)


    #Records the frequency of suggestions
    def recordFreq(self, suggestion):
        f = open('user_long_stats.txt', 'r+')

        #print suggestion
        lines = f.readlines()

        lineToWrite = []

        for line in lines:
                tabsep = string.split(line, '\t')

                if len(tabsep) == 2:
                    reg = tabsep[0]
                    freq = tabsep[1]

                    if reg == suggestion:
                        print 'Found ' + reg
                        freq_int = int(freq)
                        freq_int += 1
                        freq = str(freq_int) + '\n'
                        
                    ltr = ""
                    ltr += reg + '\t'
                    ltr += freq

                    lineToWrite.append(ltr)

        f.seek(0)
        for ln in lineToWrite:
            f.write(ln)



        f.close()

#p = Processor("insert", "qqqaaasdasdasa")
#p.process()
