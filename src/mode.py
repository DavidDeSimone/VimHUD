# Class that define a text input mode
# Each class has:
#     A starting symbol that signifies its beginning
#     A string which signifies it's name
class Mode:

    def __init__(self, name):
        self.name = name;
        self.tokens = "":
        
        #Fills the command list
        self.commands = fillCommands(name)

    #Parses the string for command tokens under the following scheme
    #Looks at starting character, tests to see if it is in the command list
    #TODO rest of scheme
    def parse(self, toParse):
        prev = ''
        tokens = []

        frontWindow = 0
        endWindow = 0

        while frontWindow < len(toParse) && endWindow < len(toParse):
            if self.isCommand(toParse[frontWindow:endWindow]) && endWindow - frontWindow <= 5:
                prev = toParse[frontWindow:endWindow]
                endWindow++
            elif prev != '':
                self.tokens.append(prev)
                frontWindow = endWindow + 1
                endWindow = frontWindow
                prev = ''
            else:
                frontWindow++
                endWindow = frontWindow
                prev = ''
        
        return tokens




    
    def process(self):
        print 'processing, actually do something here maybe??????'

    #Tests if the given string is in the command list
    def isCommand(self, str):
        if str in self.commands:
            return true

        return false

    def fillCommands(self, name):
        f = open(name + '.txt')

        lines = f.readLines();

        for line in lines:
            self.commands.append(line)
