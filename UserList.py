import random

usersInPool = ["cwittofur", "zarnorith", "pr0zzak", "ugThump", "celine", "tarlith"]
# usersInPool = []


def addUser(name):
    if name in usersInPool:
        return False
    else:
        usersInPool.append(name)
        return True


def deleteUser(name):
    usersInPool.remove(name)


def userCount():
    return len(usersInPool)


def resetUsers():
    usersInPool.clear()


def getWinner():
    numUsers = len(usersInPool)
    if numUsers > 1:
        o = random.randrange(1, numUsers)
    elif numUsers == 1:
        o = 0
    else:
        return None
    return usersInPool[o]
