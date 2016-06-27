import socket
from Settings import *


def openSocket():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))
    return s


def openWhisperSocket():
    ws = socket.socket()
    ws.connect((WHOST, PORT))
    ws.send("PASS {}\r\n".format(PASS).encode("utf-8"))
    ws.send("NICK {}\r\n".format(NICK).encode("utf-8"))
    ws.send("JOIN {}\r\n".format(WCHAN).encode("utf-8"))


def sendMessage(s, message):
    messageTemp = "PRIVMSG " + CHAN + " :" + message + "\r\n"
    s.send(messageTemp.encode("utf-8"))
    print("Sent: " + messageTemp)


def sendWhisper(ws, user, message):
    messageTemp = "PRIVMSG " + CHAN + " :/w {} ".format(user) + message + "\r\n"
    ws.send(messageTemp.encode("utf-8"))
    print("Whispered: " + messageTemp)

