import string


# Class that define a text input mode
# Each class has:
#     A starting symbol that signifies its beginning
#     A string which signifies it's name
class Mode:

    def __init__(self, name):
        self.name = name
        self.tokens = []
        self.process()
        self.commands = []
        self.fillCommands()

    #Parses the string for command tokens under the following scheme
    #Looks at starting character, tests to see if it is in the command list
    #TODO rest of scheme
    def parse(self, toParse):
        prev = ''
        tokens = []
        print 'Parsing..'

        frontWindow = 0
        endWindow = 1


        while frontWindow < len(toParse) and endWindow < len(toParse):
            print frontWindow
            print endWindow 

            print toParse[frontWindow:endWindow]


            if self.isCommand(toParse[frontWindow:endWindow]) and endWindow - frontWindow <= 5: 
                #if the current window is a command
                #within the window length
                print 'isCommand'
                prev = toParse[frontWindow:endWindow]
                endWindow += 1
            elif prev != '':
                #if we are not extending a current string
                print 'Ending TOK'
                print prev
                self.tokens.append(prev)
                frontWindow = endWindow + 1
                endWindow = frontWindow + 1
                prev = ''
            else:
                #else we are ending a command
                print 'else'
                frontWindow += 1
                endWindow = frontWindow + 1
                prev = ''
        
        self.tokens = tokens

    def process(self):
        print 'processing, actually do something here maybe??????'

    #Tests if the given string is in the command list
    def isCommand(self, str):
        if str in self.commands:
            return True

        return False


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

    
