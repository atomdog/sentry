import time
import numpy
import datetime
import imaplib
import email
import smtplib


#/----------------------------------------------------------------------------------/

#time to define our globals
#here we are defining all of our global variables for the timecheck.
global year
global month
global mrelday
global wrelday
global hour
global minute
global second
global rawtime
global now
global rawmsg
global sender
global senlevel
global rawmsgar
global isp
global family
global friends
global guests
global person
global arcount
global outmsg
global flagset
global genmes

#let's define all of these real quick
now = datetime.datetime.now()
year = 0
month = 0
week = 0
mrelday = 0
wrelday = 0
hour = 0
minute = 0
second = 0
sender = 0
person = "no"
arcount = 0
rawmsgar = [[]]
flagset = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#FIX MAX PROBLEM


def timecheck():
    print "Time check initiated"
    global year, month, week, mrelday, wrelday, hour, minute, second, now
    #let's set our global variables for time to the ACTUAL time
    year = now.year
    month = now.month
    mrelday = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    #and let's print it out for continuity and for debugging purposes
    print "Year: %d." % year
    print "Month: %d." % month
    print "Day Of Month: %d." % mrelday
    print "Time Of Day: %d : %d : %d" % (hour, minute, second)

def getmail():
    print "Mail-get initiated"
    global rawmsg, sender,isp, senlevel
    rawmsg = ''
    sender = ''
    isp = ''
    def extract_body(payload):
        if isinstance(payload,str):
            return payload
        else:
            return '\n'.join([extract_body(part.get_payload()) for part in payload])

    conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    conn.login("insertemailhere", "insertemailpasswordhere")
    conn.select()
    typ, data = conn.search(None, 'UNSEEN')
    try:
        for num in data[0].split():
            typ, msg_data = conn.fetch(num, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    payload=msg.get_payload()
                    body=extract_body(payload)
                    rawmsg = body[352:]
                    tempcut = rawmsg.index("</td>")
                    rawmsg = rawmsg[:tempcut-21]
                    varFrom = msg['from']
                    sender = varFrom[:10]
                    isp = varFrom[11:]
                    print rawmsg
                    print sender
                    print isp
                    incheck()
                    packin()
                    parse()
            typ, response = conn.store(num, '+FLAGS', r'(\Seen)')
    finally:
        try:
            conn.close()
        except:
            pass
        conn.logout()

def incheck():
    print "Security checks initiated"
    global rawmsg, sender, isp, person
    person = 'no'
    if sender == "insertnumberhere":
        person = "Aidan"
    elif sender == "insertnumberhere":
        person = "Michael"
    elif sender == "insertnumberhere":
        person = "Jennifer"
    elif sender == "insertnumberhere":
        person = "Brendan"
    else:
        person = "no"
    if(person == "Aidan" or person == "Michael" or person == "Brendan" or person == "Jennifer"):
        if isp != "mms.att.net":
            person = "no"
    print "Person: " + person

def packin():
    print "Message packaging initiated"
    global rawmsg, sender, isp, person, rawmsgar, arcount
    rawmsgar.append([rawmsg[:-1], person, sender, isp])
    arcount = len(rawmsgar)
    print "At list point:"
    print arcount
    print "The message pack is:"
    print rawmsgar[arcount - 1]
def send(om, to):
    print "Send initiated"
    fromaddr = 'insertemailhere'
    toaddrs  = to
    msg = om
    username = 'insertemailhere'
    password = 'insertemailpasswordhere'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
def parse():
    print "Message comprehension initiated"
    global rawmsgar, flagset
    flagset = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    hellos = ["good morning", "Good morning", "good afternoon", "Good afternoon", "Hello", "hello", "hi", "Hi", "hey", "Hey", "what's up", "What's up", "whats up", "Whats up", "hola", "Hola"]
    goodbyes = ["goodbye", "Goodbye", "bye", "Bye", "see you", "See you", "adios", "Adios"]
    lights = ["lights", "Lights", "light", "Light"]
    off = ["off", "Off", "OFF"]
    on = ["On", "ON", "on"]
    temperature = ["temp", "Temp", "Temperature", "temperature" "how many degrees", "How many degrees"]
    aidanroom = ["Aidan's", "aidan's", "aidans", "Aidans"]
    brendanroom = ["brendans", "Brendans", "brendan's", "Brendan's"]
    kitchen = ["kitchen", "Kitchen"]
    livingroom = ["living room", "Living room", "main room", "Main room"]
    mediaroom = ["TV room", "tv room","Tv room", "Sun room", "sun room", "tvroom", "TVroom", "Tvroom"]
    masterbed = ["Master bedroom", "master bedroom", "Master bed room", "master bed room", "Master Bedroom", "Master Bed Room", "mom and dad's room", "mom and dads room", "Mom and Dad's room", "dad and moms room"]
    diningroom = ["dining room", "Dining room", "Dining Room"]
    whatis = ["what is", "what's the", "What is", "What's the"]
    arethe = ["Are the", "are the"]
    my = ["my", "My"]
    turn = ["turn", "Turn", "switch", "Switch"]
    remind = ["remind", "Remind"]
    me = ["me"]
    aidan = ["aidan", "Aidan"]
    brendan = ["brendan", "Brendan"]
    jennifer = ["Jennifer", "jennifer", "mom", "Mom"]
    michael = ["michael", "Michael", "michael's", "Michael's"]
    select = 0
    temp = ""
    temp = len(rawmsgar) - 1
    message = rawmsgar[temp]
    message = message[0]
    print message
    x = 0

    containsgreeting = False
    containsgoodbye = False
    containslights = False
    containsoff = False
    containson = False
    containstemperature = False
    containsaidanroom = False
    containsbrendanroom = False
    containskitchen = False
    containslivingroom = False
    containsmediaroom = False
    containsmasterbed = False
    containsdiningroom = False
    containswhatis = False
    containsarethe = False
    containsmy = False
    containsturn = False
    containsme = False
    containsaidan = False
    containsbrendan = False
    containsjennifer = False
    containsmichael = False
    containsremind = False
    index = 0
    for index in range(len(hellos)):
        if hellos[index] in message:
            print "Got greeting at:"
            print index
            containsgreeting = True
            flagset[select] = 1
    index = 0
    select = select + 1

    for index in range(len(goodbyes)):
        if goodbyes[index] in message:
            print "Got goodbye at:"
            print index
            containsgoodbye = True
            flagset[select] = 1
    index = 0
    select = select + 1

    for index in range(len(lights)):
        if lights[index] in message:
            print "Got lights at:"
            print index
            containslights = True
            flagset[select] = 1
    index = 0
    select = select + 1

    for index in range(len(off)):
        if off[index] in message:
            print "Got off at:"
            print index
            containsoff = True
            flagset[select] = 1
    index = 0
    select = select + 1
    for index in range(len(on)):
        if on[index] in message:
            print "Got on at:"
            print index
            containson = True
            flagset[select]= 1
    index = 0
    select = select + 1

    for index in range(len(temperature)):
        if temperature[index] in message:
            print "Got temperature at:"
            print index
            containstemperature = True
            flagset[select] =1
    index = 0
    select = select + 1

    for index in range(len(aidanroom)):
        if aidanroom[index] in message:
            print "Got Aidan's room at:"
            print index
            containsaidanroom = True
            flagset[select] = 1
    index = 0
    select = select + 1

    for index in range(len(brendanroom)):
        if brendanroom[index] in message:
            print "Got Brendan's room at:"
            print index
            containsbrendanroom = True
            flagset[select] = 1
    index = 0
    select = select + 1

    for index in range(len(kitchen)):
        if kitchen[index] in message:
            print "Got kitchen room at:"
            print index
            containskitchen = True
            flagset[select] = 1
    index = 0
    select = select + 1

    for index in range(len(livingroom)):
        if livingroom[index] in message:
            print "Got living room at:"
            print index
            containslivingroom = True
            flagset[select] = 1
    index = 0
    select = select + 1
    for index in range(len(mediaroom)):
        if mediaroom[index] in message:
            print "Got media room at:"
            print index
            containsmediaroom = True
            flagset[select] = 1
    index = 0
    select = select + 1
    for index in range(len(masterbed)):
        if masterbed[index] in message:
            print "Got masterbed room at:"
            print index
            containsmasterbed = True
            flagset[select] = 1
    index = 0
    select = select + 1

    for index in range(len(diningroom)):
        if diningroom[index] in message:
            print "Got dining room at:"
            print index
            containsdiningroom = True
            flagset[select] = 1
    index = 0
    select = select + 1

    for index in range(len(whatis)):
        if whatis[index] in message:
            print "Got whatis at:"
            print index
            containswhatis = True
            flagset[select] = 1
    index = 0
    select = select + 1
    for index in range(len(arethe)):
        if arethe[index] in message:
            print "Got arethe at:"
            print index
            containsarethe = True
            flagset[select] = 1
    index = 0
    select = select + 1

    for index in range(len(my)):
        if my[index] in message:
            print "Got my at:"
            print index
            containsmy = True
            flagset[select] = 1
    index = 0
    select = select + 1
    for index in range(len(turn)):
        if turn[index] in message:
            print "Got turn at:"
            print index
            containsturn = True
            flagset[select] = 1
    index = 0
    select = select + 1

    for index in range(len(remind)):
        if remind[index] in message:
            print "Got remind at:"
            print index
            containsremind = True
            flagset[select] = 1
    index = 0
    select = select + 1
    for index in range(len(me)):
        if me[index] in message:
            print "Got me at:"
            print index
            containsme = True
            flagset[select] = 1
    index = 0
    select = select + 1
    for index in range(len(aidan)):
        if aidan[index] in message:
            print "Got aidan at:"
            print index
            containsaidan = True
            flagset[select] = 1
    index = 0
    select = select + 1

    for index in range(len(brendan)):
        if brendan[index] in message:
            print "Got brendan at:"
            print index
            containsbrendan = True
            flagset[select] = 1
    index = 0
    select = select + 1

    for index in range(len(jennifer)):
        if jennifer[index] in message:
            print "Got jennifer at:"
            print index
            containsjennifer = True
            flagset[select] = 1
    index = 0
    select = select + 1

    for index in range(len(michael)):
        if michael[index] in message:
            print "Got michael at:"
            print index
            containsmichael = True
            flagset[select] = 1
    index = 0
    select = select + 1


    #hellos, goodbyes, lights, off, on, temperature, aidanroom, brendanroom, kitchen, living room, mediaroom, masterbed, diningroom, whatis, arethe, my, turn, aidan,
    # brendan, jennifer, michael
    select = 0
    print flagset
    print len(flagset)
    genresponse(flagset)


def genresponse(flags):
    genmes = ""
    outgoing = ""
    tempout = ""
    senst = ""
    sen = ""
    timecheck()
    global rawmsgar
    tmpr = ""
    tmpr = len(rawmsgar) - 1
    senst = rawmsgar[tmpr]

    sen = senst[1]
    greetnq = ["Hey", "Hello", "Hola", "Hi"]
    greetq = ["What's up", "How's it going", "What's going on"]
    goodbye = ["See you", "Goodbye", "Bye", "Hasta la vista", "Be safe", "Catch you later"]

    print "Response generation initiated"
    genmes = ""
    if flags[0] == 1:
        a = numpy.random.randint(0, 3)
        print a
        if a == 0:
            genmes = greetnq[numpy.random.randint(0,4)] + "," + " " + sen + ". "
        if a == 1:
            genmes = greetq[numpy.random.randint(0,3)] + "," + " " + sen + "? "
        if a == 2:
            if hour <= 4 or hour >= 18:
                genmes = "Good evening" + ", " + sen + ". "
            if hour >= 5 and hour <= 11:
                genmes = "Good morning, " + sen + ". "
            if hour >= 12 and hour <= 17:
                genmes = "Good afternoon, " + sen + ". "
    if flags[1] == 1:
        if numpy.random.randint(0, 4) < 2:
            genmes = goodbye[numpy.random.randint(0,6)] + "," + " " + sen + ". "
        else:
            if hour <= 4 or hour >= 18:
                if numpy.random.randint(0, 2) == 1:
                    genmes = "Good night" + ", " + sen + ". "
                else:
                    genmes = "Have a nice night, " + sen + ". "
            if hour >= 5 and hour <= 11:
                genmes = "Have a nice morning, " + sen + "."
            if hour >= 12 and hour <= 17:
                genmes = "Enjoy your afternoon, " + sen + ". "
    if flags[2] == 1 and flags[4] == 1 and flags[16] == 1:
        #lights, on, turn
        if numpy.random.randint(0, 4) < 2:
            genmes = genmes + "I'm turning the lights on in "
        else:
            genmes = genmes + "Lights on in "
    if flags[2] == 1 and flags[3] == 1 and flags[16] == 1:
        #lights, off, turn
        if numpy.random.randint(0, 4) < 2:
            genmes = genmes + "I'm turning the lights off in "
        else:
            genmes = genmes + "Shutting off the lights in "
    if flags[6] == 1 and flags[17] == 1 and flags[2] == 1 and flags[16] == 1:
        genmes = genmes + "Aidan's room."
    if flags[7] == 1 and flags[18] == 1 and flags[2] == 1 and flags[16] == 1:
        genmes = genmes + "Brendan's room."
    if flags[8] == 1 and flags[2] == 1 and flags[16] == 1:
        genmes = genmes + "the kitchen."
    if flags[9] == 1 and flags[2] == 1 and flags[16] == 1:
        genmes = genmes + "the living room."
    if flags[10] == 1 and flags[2] == 1 and flags[16] == 1:
        genmes = genmes + "the TV room."
    if flags[11] == 1 and flags[2] == 1 and flags[16] == 1:
        genmes = genmes + "the master bedroom."
    if flags[12] == 1 and flags[2] == 1 and flags[16] == 1:
        genmes = genmes + "the dining room."
    if flags[15] == 1 and flags[2] == 1 and flags[16] == 1:
        if sen == "Michael":
            genmes = genmes + "your room, the master bedroom."
        if sen == "Aidan":
            genmes = genmes + "your room."
        if sen == "Jennifer":
            genmes = genmes + "your room, the master bedroom"
        if sen == "Brendan":
                genmes = genmes + "your room."
    print genmes
    tempout = ""
    outgoing = ""
    tempout = len(rawmsgar) - 1
    tempout = rawmsgar[tempout]
    outgoing = tempout[2]
    outgoing = outgoing + "@"
    outgoing = outgoing + tempout[3]
    send(genmes, outgoing)
while True:
    try:
       getmail()
    except:
       pass
