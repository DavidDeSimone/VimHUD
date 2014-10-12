import math
import string

usefullness_file_name= "usefullness.txt"
user_stats_file_name = "user_stats.txt"
command_description_file_name = "command_description.txt"
command_description_insert_file_name = "command_description_insert.txt"

def load_stats():
    usefulness = dict()
    user_stats = dict()
    load_usefull(usefulness)
    load_user_stats(user_stats)
    return usefulness, user_stats

def load_usefull(usefulness):
    usefulness_file = open(usefullness_file_name, 'r')
    for line in usefulness_file:
        line = string.split(line, '\t')
        print line[0]
        usefulness[line[0]] = int(line[1])

def load_user_stats(user_stats):
    user_stats_file = open(user_stats_file_name, 'r')
    for line in user_stats_file:
        line = line.split()
        user_stats[line[0]] = math.exp(-int(line[1])/200.0)#learn constant??

def combine_features(usefullness, user_stats, recent_stats):
    #assert(len(usefullness) == len(user_stats) and len(user_stats) == len(recent_stats))
    probabilities = list()
    for key in usefullness.keys():
        probabilities.append((usefullness[key]+recent_stats[key])*recent_stats[key])
    print probabilities

def main():
    usefullness, user_stats = load_stats();
    recent_stats = usefullness
    print usefullness
    print user_stats
    combine_features(usefullness, user_stats, recent_stats)

if __name__ == "__main__":
    main()
