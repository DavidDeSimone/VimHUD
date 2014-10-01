import sys


# Create the parser for the input file 
parse = Parser(sys.argv[1]);
parse.printTokens();

class Parser:
    def __init__(self, str):
        self.toParse = str;
        self.tokens = [];
        self.tokMark = TokenMarker()

    def parseStr(self):
        



    def printTokens(self):
        for x in xrange(0, len(self.tokens)):
            print self.tokens[x];
