from Read import getUser, getMessage
from Socket import *
from Initialize import joinRoom
from UserList import *
from Ships import getShip
import time
import re


messageQueue = []
s = openSocket()
joinRoom(s)
runServer = True


def getShipTypeID(m):
    if "frigate" in m:
        return 1
    elif "destroyer" in m:
        return 2
    elif "cruiser" in m:
        return 3
    else:
        return 0


def getFactionID(f):
    if "amarr" in f:
        return 1
    elif "caldari" in f:
        return 2
    elif "gallente" in f:
        return 3
    elif "minmatar" in f:
        return 4
    else:
        return 0


def processMessageQueue():
    for item in messageQueue:
        sendMessage(s, item)
        time.sleep(0.125)  # Queue messages instead of blasting the server.


def getRandomType():
    return random.randrange(1, 3)


def getWinners(numWinners):
    winnerList = []
    for x in range(0, numWinners):
        winner = getWinner()
        deleteUser(winner)
        winnerList.append(winner)
    return winnerList


def matchup(shiptype, factionid, teamsize):
    players = getWinners(teamsize * 2)
    for user in players:
        userShip = getShip(shiptype, factionid)
        messageQueue.append("/w {}".format(user) + " you fly a {}".format(userShip))
    if teamsize == 1:
        messageQueue.append("{}".format(players[0]) + " will battle against {}".format(players[1]))
    else:
        messageQueue.append("The teams are as follows: ")
        teamMessage = ""
        for player in range(0, teamsize):
            teamMessage += players[player] + " "
        teamMessage += "VS. "
        for player in range(teamsize, teamsize * 2):
            teamMessage += players[player] + " "

        messageQueue.append(teamMessage)

    processMessageQueue()


while runServer:
    response = s.recv(1024).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        # print(response)
        user = getUser(response)
        message = getMessage(response)
        print(user + " typed: " + message)
        if "!enter" in message:
            if addUser(user):
                sendMessage(s, "{} entered".format(user))

        elif "!reset" in message and "cwittofur" in user:
            resetUsers()

        elif "!matchup" in message and "cwittofur" in user:
            if userCount() < 2:
                sendMessage(s, "Not enough entrants")
            else:
                shipTypeID = getShipTypeID(message)
                shipFactionID = getFactionID(message)
                if shipTypeID == 0:
                    shipTypeID = getRandomType()
                matchup(shipTypeID, shipFactionID, 1)

        elif "!team" in message and "cwittofur" in user:
            size = int(re.search(r"\d", message).group(0))
            if userCount() < size * 2:
                sendMessage(s, "Not enough entrants")
            else:
                shipTypeID = getShipTypeID(message)
                shipFactionID = getFactionID(message)
                if shipTypeID == 0:
                    shipTypeID = getRandomType()
                matchup(shipTypeID, shipFactionID, size)

        elif "!shutdown" in message and "cwittofur" in user:
            runServer = False
            sendMessage(s, "The bot is shutting down; fly safe o7")

    time.sleep(1 / RATE)
