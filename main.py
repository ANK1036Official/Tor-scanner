#!/usr/bin/python3
import random, socks, socket, threading
threadsl = 5
count = 0 # dont mess with this
threadcount = 0 # mess mess with this
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
def torsitel():
    global count
    count +=1
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    num = ["2","3","4","5","6","7"]
    decider = random.randint(1, 2)
    if decider == 1:
        let1 = random.choice(alphabet)
    elif decider == 2:
        let1 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let2 = random.choice(alphabet)
    elif decider == 2:
        let2 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let3 = random.choice(alphabet)
    elif decider == 2:
        let3 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let4 = random.choice(alphabet)
    elif decider == 2:
        let4 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let5 = random.choice(alphabet)
    elif decider == 2:
        let5 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let6 = random.choice(alphabet)
    elif decider == 2:
        let6 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let7 = random.choice(alphabet)
    elif decider == 2:
        let7 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let8 = random.choice(alphabet)
    elif decider == 2:
        let8 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let9 = random.choice(alphabet)
    elif decider == 2:
        let9 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let10 = random.choice(alphabet)
    elif decider == 2:
        let10 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let11 = random.choice(alphabet)
    elif decider == 2:
        let11 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let12 = random.choice(alphabet)
    elif decider == 2:
        let12 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let13 = random.choice(alphabet)
    elif decider == 2:
        let13 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let14 = random.choice(alphabet)
    elif decider == 2:
        let14 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let15 = random.choice(alphabet)
    elif decider == 2:
        let15 = random.choice(num)
    decider = random.randint(1, 2)
    if decider == 1:
        let16 = random.choice(alphabet)
    elif decider == 2:
        let16 = random.choice(num)
    torsite = (let1 + let2 + let3 + let4 + let5 + let6 + let7 + let8 + let9 + let10 + let11 + let12 + let13 + let14 + let15 + let16)
    torsite = (torsite + ".onion").lower()
    with open("deadonions.txt", "r") as listl:
        if torsite in listl:
            listl.close()
            return torsitel()
        else:
            listl.close()
            try:
                torconnect = socks.socksocket()
                torconnect.connect((torsite, 80))
                message = 'GET / HTTP/1.0\r\n\r\n'
                torconnect.sendall(bytes(message, "UTF-8"))
                reply = torconnect.recv(4069)
                torconnect.close()
                print("[*] Request #" + str(count) + " Tried request on: " + format(torsite) + " request Succeeded")
                with open("aliveonions.txt", "a") as onionlist:
                    onionlist.write(format(torsite) + "\n")
                    onionlist.close()
                return torsitel()
            except Exception:
                torconnect.close()
                del torconnect
                print("Request #" + str(count) + " Tried request on: " + format(torsite) + " request Failed")
                with open("deadonions.txt", "a") as write:
                    write.write(torsite + "\n")
                    write.close()
                return torsitel()
def threads():
    global threadcount
    while 1:
        threadcount += 1
        torthread = threading.Thread(target=torsitel)
        torthread.daemon = True
        torthread.start()
        if threadcount > threadsl:
            break
    torthread.join()
threads()
