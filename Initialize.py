from Socket import sendMessage


def joinRoom(s):
    Loading = True
    while Loading:
        readbuffer = s.recv(1024).decode("utf-8")
        temp = readbuffer.split("\n")

        for line in temp:
            print(line)
            Loading = loadingComplete(line)
            if not Loading:
                break

    sendMessage(s, "Successfully joined chat")


def loadingComplete(line):
    if "End of /NAMES list" in line:
        return False
    else:
        return True
