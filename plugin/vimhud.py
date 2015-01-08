from os.path import expanduser
import string
import sys

home = expanduser("~")
plugin_path = '/.vim/bundle/VimHUD/plugin/'

def main():
    update()

def update():
    #Open current Vim character buffer found in home
    vimLog = open(home + '/.vimlog', 'r+')

    freqSet = pullFreq(vimLog)
    writeShortStats(freqSet)
    writeLongStats(freqSet)
    emptyFile(vimLog)
    vimLog.close()

def pullFreq(log):
    dic = initDict()

    commandSet = readCommands(log)

    for command in commandSet:
        if dic.has_key(command):
            dic[command] =  int(dic[command] + 1)
        else:
            dic[command] = 1


    return dic

# Parses all of the commands VIM present in a text file
# Returns a set containing each command present
def readCommands(file_t):
    se = list()
    cmd = fillCommandList('command')
    ins = fillCommandList('insert')

    #print cmd

    for line in file_t.readlines():
        tokens = readVimTokens(line)

        #Token objects are lists in the form [word, mode]
        for tok in tokens:
            ln = tok[0]
            mode = tok[1]

            for x in xrange(0, len(ln)):
                lon_len = 0
                lon_word = ''

                if mode == 'C':
                    for word in cmd:
                        if ln[x: x + len(word)] == word:
                            if lon_len < len(word):
                                lon_len = len(word)
                                lon_word = word

                        if lon_word != '':
                            se.append(lon_word)
                            x += lon_len

                elif ln[1] == 'I':
                    for word in ins:
                        if ln[x: x + len(word)] == word:
                            if lon_len < len(word):
                                lon_len = len(word)
                                lon_word = word

                        if long_word != '':
                            se.append(lon_word)
                            x += lon_len

    return se

# Tokenizes input based on current Vim modes
# Returns an array of tokens in the form [token, mode]
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
            ret_list.append([to_add, 'C'])
            end_i = x

        elif str_t[x] == 'I' and command_mode == True:
            command_mode = False
            to_add = str_t[end_i:x]
            ret_list.append([to_add, 'I'])
            end_i = x

    #print 'Printing Return List'
    #print ret_list
    return ret_list


# Reads in the commands for the specified modes
#Modes for standard Vim include Insert and Command
def fillCommandList(mode_t):
    se = set()

    f = open(home + plugin_path + mode_t + '.txt')
    lines = f.readlines()

    for line in lines:
        item = string.split(line)
        se.add(item[0])

    return se

def diff(x1, x2):
    return x1 - x2

def writeShortStats(freqSet):
    shortFile = open(home + plugin_path + 'short_term.txt', 'w')

    emptyFile(shortFile)
    writeFile(shortFile, freqSet)

    shortFile.close()

def writeLongStats(freqSet):
    longFile = open(home + plugin_path + 'long_term.txt', 'r+')

    fileDict = readDict(longFile)
    merged = mergeDicts(freqSet, fileDict)

    emptyFile(longFile)
    writeFile(longFile, merged)

    longFile.close()


def readDict(file_t):
    dic = initDict()

    lines = file_t.readlines()

    for line in lines:
        keyvalue = line.split()
        key = keyvalue[0]
        value = keyvalue[1]

        dic[key] = value

    return dic

# Creates a dictionary of all python commands, with frequency
# initalized to 0
def initDict():
    dict_r = dict()

    #Read command-mode commands file
    command_f = open(home + plugin_path + 'command.txt', 'r')

    lines = command_f.readlines()

    for line in lines:
        keys = line.split()
        key = keys[0]

        dict_r[key] = 0

    #Read Insert-mode command file
    insert_f = open(home + plugin_path + 'insert.txt', 'r')

    lines = insert_f.readlines()

    for line in lines:
        keys = line.split()
        key = keys[0]

        dict_r[key] = 0

    return dict_r



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
