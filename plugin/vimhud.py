from os.path import expanduser
import string
import sys

home = expanduser("~")

def main():
    update()
    
def update():
    #Open current Vim character buffer found in home
    vimLog = open(home + '/.vimlog', 'r+')

    freqSet = pullFreq(vimLog)
    writeShortStats(freqSet)
    writeLongStats(freqSet)
    
    vimLog.close()

def pullFreq(log):
    dic = dict()

    commandSet = readCommands(log)

    for command in commandSet:
        if dic.has_key(command):
            dic[command] =  int(dic[command] + 1) 
        else:
            dic[command] = 1

    
    return dic


def readCommands(file_t):
    se = set()
    cmd = fillCommandList('command')
    ins = fillCommandList('insert')

    #print cmd

    for line in file_t.readlines():
        tokens = readVimTokens(line)

        for ln in tokens:
            for x in xrange(0, len(ln)):
                lon_len = 0
                lon_word = ''

                for word in cmd:
                    if ln[x: x + len(word)] == word:
                        if lon_len < len(word):
                            lon_len = len(word)
                            lon_word = word 
                
                    if lon_word != '':
                        se.add(lon_word)
                        x += lon_len
            
    #print se
    return se

# Tokenizes input based on current Vim modes
# Returns an array of tokens
def readVimTokens(str_t):
    end_i = 0

    ret_list = list()

    command_mode = False

    for x in xrange(0, len(str_t)):

        #print ord(str_t[x])

        #Escape Character is 27 in ASCII
        if ord(str_t[x]) == 27:
            #print 'In Command Mode'
            command_mode = True
            to_add = str_t[end_i:x]
            ret_list.append(to_add)
            end_i = x
            
        elif str_t[x] == 'I' and command_mode == True:
            command_mode = False
            to_add = str_t[end_i:x]
            ret_list.append(to_add)
            end_i = x
        



    #print 'Printing Return List'
    #print ret_list
    return ret_list


# Reads in the commands for the specified modes 
#Modes for standard Vim include Insert and Command
def fillCommandList(mode_t):
    se = set()

    f = open(mode_t + '.txt')
    lines = f.readlines()

    for line in lines:
        item = string.split(line)
        se.add(item[0])

    
    return se

def diff(x1, x2):
    return x1 - x2

def writeShortStats(freqSet):
    shortFile = open('short_term.txt', 'w')
    
    emptyFile(shortFile)
    writeFile(shortFile, freqSet)
    
    shortFile.close()

def writeLongStats(freqSet):
    longFile = open('long_term.txt', 'r+')

    fileDict = readDict(longFile)
    merged = mergeDicts(freqSet, fileDict)
    
    emptyFile(longFile)
    writeFile(longFile, merged)

    longFile.close()


def readDict(file_t):
    dic = dict()

    lines = file_t.readlines()

    for line in lines:
        keyvalue = line.split()
        key = keyvalue[0]
        value = keyvalue[1]

        dic[key] = value
        
    return dic

def mergeDicts(freqSet, fileDict):
    for key, value in freqSet.iteritems():
        if fileDict.has_key(key):
            fileDict[key] = int(value + int(fileDict[key]))
        else:
            fileDict[key] = value

    return fileDict

def emptyFile(f):
    f.seek(0)
    f.truncate()
    
def writeFile(file_t, freq_set):
    for key, value in freq_set.iteritems():
        file_t.write(key + ' ' + str(value) + '\n')

        
if __name__ == "__main__":
    main()
