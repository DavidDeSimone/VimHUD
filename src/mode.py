# Class that define a text input mode
# Each class has:
#     A starting symbol that signifies its beginning
#     A set of terminating symbols that clarify it's ending
#     A string which signifies it's name
class Mode:
    def __init__(self, name, sSyms, tSyms):
        self.name = name;
        self.sSyms = sSyms;
        self.tSyms = tSyms;
        self.tokens = "":

    def parse(self):
        

    def process(self):
        

    
