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
    def __init__(self, mode, toParse):
        self.mode = mode
        self.toParse = toParse
        self.regexs = []
        self.desc = []

    #Reads in the list of regexs from disk
    #and checks to see if they are contained in
    #the passed string toParse
    def process():
        f = open(self.mode + '_regex.txt')

        regexFull = f.readlines()
        self.processRegex(regexFull)

        for regex in self.regexs:
            regexp = re.compile(regex)
            if regexp.search(toParse) is not None:
                print 'FOUND REGEX, CALLING FOO()'

    #Function used to reading regexs in from disk
    #Regexs are found in <mode>_regex.txt with the following format
    #<regular expression>\t<single line description of regex>
    def processRegex(self, regexFull):
        for line in regexFull:
            ls = string.split(line, '\t')

            self.regexs.append(ls[0])
            self.desc.append(ls[1])
