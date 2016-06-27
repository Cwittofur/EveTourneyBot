import re

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
CHAT_BOT = re.compile(r"^!lottery")

def getUser(line):
    user = re.search(r"\w+", line).group(0)
    return user

def getMessage(line):
    message = CHAT_MSG.sub("", line)
    return message
