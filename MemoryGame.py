import random
import time
import sys

def generate_sequence(difficulty):
    numlist = []
    i=0
    while i < int(difficulty):
        rand = random.randint(1,101)
        numlist.append(rand)
        i+=1
    return numlist


def get_list_from_user(difficulty):
    usernumlist = []
    i=0
    while i < int(difficulty):
        usernumlist.append(int(input("Enter number:")))
        i+=1
    return usernumlist


def is_list_equal(complist,userlist):
    if complist == userlist:
        return True
    else:
        return False


def play(difficulty):
    complist = generate_sequence(difficulty)
    sys.stdout.write(str(complist))
    sys.stdout.flush()
    time.sleep(0.7)
    sys.stdout.write('\r' + ' ' * len(complist) + '\r')
    sys.stdout.flush()
    print()
    userlist = get_list_from_user(difficulty)
    return is_list_equal(complist, userlist)

