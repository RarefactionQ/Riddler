import random

# COIN1 = 5
# COIN2 = 6
# COIN3 = 7

LENGTH = 40

record = {}

def set_the_record():
    for x in range(1,LENGTH+7):
        record[x] = 0

def print_the_record():
    s = ""
    for x in range(1,LENGTH+1):
        s += str(record[x])+", "
    print s

def roll():
    return int(random.random()*6 + 1)

def step(index):
    # print str(index)
    index += roll()
    record[index] = record[index]+1
    return index

def play_game():
    index = 0
    while index < LENGTH+1:
        index = step(index)

def play_coin_game(coin1,coin2,coin3):
    index = 0
    while index < LENGTH+1:
        index = step(index)
        if index == coin1 or index == coin2 or index == coin3:
            return 1
    return 0


def wins_loses(wins,tries):
    print "Wins: "+str(wins)
    print "Tries: "+str(tries)+" "+str(100.0*wins/tries)+"%"

def legal_coin(c1,c2,c3):
    if c1 == c2 or c2 == c3 or c1 == c3:
        return False
    if (c1-1) == c2 or (c1-1) == c3:
        return False
    if (c1+1) == c2 or (c1+1) == c3:
        return False
    if (c2-1) == c1 or (c2-1) == c3:
        return False
    if (c2+1) == c1 or (c2+1) == c3:
        return False
    if (c3-1) == c1 or (c3-1) == c2:
        return False
    if (c3+1) == c1 or (c3+1) == c2:
        return False
    return True


def best_coin_combo():
    c1 = 0
    best = 0.0
    bestseq = ""

    for x in range(LENGTH):
        c1 += 1
        c2 = 1
        c3 = 1
        for y in range(LENGTH):
            c2 += 1
            c3 = 1
            for z in range(LENGTH):
                c3 += 1
                wins = 0
                if legal_coin(c1,c2,c3):
                    for i in range(TRIES):
                        wins += play_coin_game(c1,c2,c3)
                        if 100.0*wins/TRIES > best:
                            best = 100.0*wins/TRIES
                            bestseq = str(c1)+","+str(c2)+","+str(c3)
                            print str(best)
                            print bestseq



set_the_record()
TRIES = 10000
# wins = 0 
# for x in range(TRIES):
    # play_game()
# for x in range(TRIES):
    # wins += play_coin_game(COIN1,COIN2,COIN3)
# wins_loses(wins,TRIES)
# print_the_record()
best_coin_combo()



