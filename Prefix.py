from random import randint

prefix = ["어...", "어", "어", "에...", "...", "그"]

def addPrefix(list):
    for i in range(int(len(list) / 1.5)):
        list.insert(randint(1, len(list)-1), prefix[randint(0,len(prefix)-1)])
    return list

def combine(list):
    return ' '.join(list) + '\n\n'