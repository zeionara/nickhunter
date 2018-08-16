import random

EVEN = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','x','z','q','ch','sh']
EVEN_LENGTH = len(EVEN)
ODD = ['a','e','i','o','u','w','y','ua','io','ia','oa']
ODD_LENGTH = len(ODD)
MIN_LENGTH = 3
MAX_LENGTH = 6

def get_new_nick():
    next_odd = random.random() > 0.5;
    nick_length = random.randint(MIN_LENGTH, MAX_LENGTH)
    nick = ''
    for i in range(nick_length):
        if next_odd:
            nick = nick + ODD[random.randint(0, ODD_LENGTH - 1)]
        else:
            nick = nick + EVEN[random.randint(0, EVEN_LENGTH - 1)]
        next_odd = not next_odd
    return nick
