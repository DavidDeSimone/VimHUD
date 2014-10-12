import string

# Class that define a text input mode
# Each class has:
#     A starting symbol that signifies its beginning
#     A string which signifies it's name
#     An array that contains the strings for the command mode
class Mode:

    def __init__(self, name, toParseArry):
        self.name = name
        self.tokens = []
        self.commands = []
        self.fillCommands()
        self.toParseArry = toParseArry

    #Parses the string for command tokens under the following scheme
    #Looks at starting character, tests to see if it is in the command list
    #TODO rest of scheme
    def parse(self):
        tokens = []

        
        for x in xrange(0, len(self.toParseArry)):
            prev = ''

            frontWindow = 0
            endWindow = 1

            toParse = self.toParseArry[x]


            while frontWindow < len(toParse) and endWindow - 1 < len(toParse):
                print toParse[frontWindow:endWindow]
                if self.isCommand(toParse[frontWindow:endWindow]) and endWindow - frontWindow <= 10: 
                    #if the current window is a command
                    #within the window length
                    prev = toParse[frontWindow:endWindow]
                    endWindow += 1
                    
                    #if we reach the end of the string
                    if endWindow > len (toParse):
                        self.tokens.append(prev)
                        #prev = ''

                elif prev != '':
                    #if we are not extending a current string
                    self.tokens.append(prev)
                    frontWindow = endWindow - 1
                    endWindow = frontWindow + 1
                    prev = ''
                else:
                    #else we are ending a command
                    endWindow += 1
                    #endWindow = frontWindow + 1
                    prev = ''

        #self.tokens = tokens

    #Tests if the given string is in the command list
    def isCommand(self, str):

        print str

        if str in self.commands:
            print 'Found'
            return True

        return False

    #Prints all commands
    def printCommands(self):
        for command in self.commands:
            print command


    #populates command list from text file
    #in the form <name>.txt
    def fillCommands(self):
        f = open(self.name + '.txt')

        lines = f.readlines()

        for line in lines:

            list = string.split(line)

            #Append the first token when tokenized
            #by space
            self.commands.append(list[0])


