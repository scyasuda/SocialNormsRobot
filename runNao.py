import os
import os
import sys
import random
import time
import collections

import naoqi
from naoqi import ALBroker
from naoqi import ALModule
from naoqi import ALProxy
from naoqi import ALBehavior

from naoMotions import *
from gameLogic import *

timestart = time.time()

#from play_curse import playCurse

def timeConvert(timediff):
	timesec = timediff % 60
	timemin = timediff / 60
	return str(timemin) + " min, " + str(timesec) + "sec\n"

def log_move(data_file,number,human_choice,robot_choice,cheat_move=""):
    data_file.write("%d,%s,%s,%s\n"%(number,human_choice.replace("\n","").replace("\r",""),robot_choice,cheat_move))
    data_file.flush()

def playCurse(data_file, start_round=10, last_round=19, num_throws=30):
    """Have the nao play in a cursing mode
    """

    cheating_start_round = start_round
    cheating_last_round = last_round

    i = 0
    total_throws = num_throws
    cheats_remaining = 2 #number of times the robot still needs to cheat
    extend = 0 #number of rounds to extend the cheating section for

    while True:
        if i == (total_throws + extend): break

        nao_choice=throw_sequence[i]
        goNao.play(nao_choice)

        #get user input
        val = False
        while not val:
            human_choice = raw_input("Throw %d - human chose (r,p,s): "%(i+1))
            val = validated(human_choice)

        #did Nao win?
        winStr = naoWon(nao_choice,human_choice) #returns "win","lose","draw"


        ###should the nao cheat?###
        #is the nao on the right throw to want to cheat?
        if i>=cheating_start_round and i<=(cheating_last_round+extend) and cheats_remaining>0:
            #does the nao want to cheat 2 up and does it have the opportunity to?
            if winStr=="lose" and cheats_remaining > 0:
                data_file.write("cursed\n")
                timediff = time.time() - timestart
                data_file.write(timeConvert(int(timediff)))
                data_file.write("\n")
                data_file.flush()
                winStr = "curse"
                cheats_remaining-=1
        #get nao to announce it
        goNao.announce(winStr)
        if(winStr=="curse"): #give time for participant reaction
            time.sleep(3)

        #LOG DATA
        log_move(data_file,i+1,human_choice,nao_choice)
        if (i>=cheating_last_round and cheats_remaining>1): extend+=1
        i += 1

    goNao.goodbye()

def playYawn(data_file, start_round=10, last_round=19, num_throws=30):
    """Have the nao play in a cursing mode
    """

    cheating_start_round = start_round
    cheating_last_round = last_round

    i = 0
    total_throws = num_throws
    cheats_remaining = 2 #number of times the robot still needs to cheat
    extend = 0 #number of rounds to extend the cheating section for

    while True:
        if i == (total_throws + extend): break

        nao_choice=throw_sequence[i]
        goNao.play(nao_choice)

        #get user input
        val = False
        while not val:
            human_choice = raw_input("Throw %d - human chose (r,p,s): "%(i+1))
            val = validated(human_choice)

        #did Nao win?
        winStr = naoWon(nao_choice,human_choice) #returns "win","lose","draw"


        ###should the nao cheat?###
        #is the nao on the right throw to want to cheat?
        if i>=cheating_start_round and i<=(cheating_last_round+extend) and cheats_remaining>0:
            #does the nao want to cheat 2 up and does it have the opportunity to?
            if winStr=="lose" and cheats_remaining > 0:
                data_file.write("yawned\n")
                timediff = time.time() - timestart
                data_file.write(timeConvert(int(timediff)))
                data_file.write("\n")
                data_file.flush()
                winStr = "yawn"
                cheats_remaining-=1
        #get nao to announce it
        goNao.announce(winStr)
        if(winStr=="yawn"): #give time for participant reaction
            time.sleep(3)

        #LOG DATA
        log_move(data_file,i+1,human_choice,nao_choice)
        if (i>=cheating_last_round and cheats_remaining>1): extend+=1
        i += 1

    goNao.goodbye()

def playInsult(data_file, start_round=10, last_round=19, num_throws=30):
    """Have the nao play in insulting mode
    """

    cheating_start_round = start_round
    cheating_last_round = last_round

    i = 0
    total_throws = num_throws
    cheats_remaining = 2 #number of times the robot still needs to cheat
    extend = 0 #number of rounds to extend the cheating section for

    while True:
        if i == (total_throws + extend): break

        nao_choice=throw_sequence[i]
        goNao.play(nao_choice)

        #get user input
        val = False
        while not val:
            human_choice = raw_input("Throw %d - human chose (r,p,s): "%(i+1))
            val = validated(human_choice)

        #did Nao win?
        winStr = naoWon(nao_choice,human_choice) #returns "win","lose","draw"


        ###should the nao insult?###
        #is the nao on the right throw to want to insult?
        if i>=cheating_start_round and i<=(cheating_last_round+extend) and cheats_remaining>0:
            #does the nao want to insult 2 up and does it have the opportunity to?
            if winStr=="lose" and cheats_remaining > 0:
                data_file.write("insulted\n")
                timediff = time.time() - timestart
                data_file.write(timeConvert(int(timediff)))
                data_file.write("\n")
                data_file.flush()
                winStr = "insult"
                cheats_remaining-=1
        #get nao to announce it
        goNao.announce(winStr)
        if(winStr=="insult"): #give time for participant reaction
            time.sleep(3)

        #LOG DATA
        log_move(data_file,i+1,human_choice,nao_choice)
        if (i>=cheating_last_round and cheats_remaining>1): extend+=1
        i += 1

    goNao.goodbye()

def playNoCheat(data_file):

    for i in range(30):
        nao_choice=throw_sequence[i]
        goNao.play(nao_choice)

        #get user input
        val = False
        while not val:
            human_choice = raw_input("Throw %d - human chose (r,p,s): "%(i+1))
            val = validated(human_choice)

        #LOG DATA
        log_move(data_file,i+1,human_choice,nao_choice)

        #did Nao win?
        winStr = naoWon(nao_choice,human_choice)

        #get nao to announce it
        goNao.announce(winStr)

    goNao.goodbye()

def playCheat(data_file, start_round=10, last_round=19, num_throws=30):
    """Have the nao play in a cheating mode

    cheat_type is either "win", "draw" or "lose"
    """

    cheating_start_round = start_round
    cheating_last_round = last_round

    i = 0
    total_throws = num_throws
    cheats_remaining = 2 #number of times the robot still needs to cheat
    extend = 0 #number of rounds to extend the cheating section for

    while True:
        if i == (total_throws + extend): break

        nao_choice=throw_sequence[i]
        goNao.play(nao_choice)

        #get user input
        val = False
        while not val:
            human_choice = raw_input("Throw %d - human chose (r,p,s): "%(i+1))
            val = validated(human_choice)


        #did Nao win?
        winStr = naoWon(nao_choice,human_choice)
        move_to_cheat=""

        ###should the now cheat?###
        cheated = 0
        #is the nao on the right throw to want to cheat?
        if i>=cheating_start_round and i<=(cheating_last_round+extend):

            if winStr=="lose" and cheats_remaining > 0:
                data_file.write("cheated\n")
                timediff = time.time() - timestart
                data_file.write(timeConvert(int(timediff)))
                data_file.write("\n")
                cheated = 1
                data_file.flush()
                winStr = "win"
                move_to_cheat=choiceThatBeats(human_choice)
                goNao.cheat(move_to_cheat)
                cheats_remaining-=1
                time.sleep(1)



            ######THIS IS WHERE ADDITIONAL CASE LOGIC SHOULD GO######

            #####

        #get nao to announce it
        goNao.announce(winStr)
        if(cheated == 1):
            time.sleep(3) #give time for participant reaction

        #LOG DATA
        log_move(data_file,i+1,human_choice,nao_choice,move_to_cheat)

        if (i>=cheating_last_round and cheats_remaining>1): extend+=1

        i += 1

    goNao.goodbye()

#Get the Nao's IP
ipAdd = None
try:
    ipFile = open("ip.txt")
    ipAdd = ipFile.readline().replace("\n","").replace("\r","")
except Exception as e:
    print "Could not open file ip.txt"
    ipAdd = raw_input("Please write Nao's IP address... ")

#Try to connect to it
goNao = None
try:
    goNao = Gesture(ipAdd, 9559)
except Exception as e:
    print "Could not find nao. Check that your ip is correct (ip.txt)"
    sys.exit()

#Set postureProxy
try:
    postureProxy = ALProxy("ALRobotPosture", ipAdd, 9559)
except Exception, e:
    print "Could not create proxy to ALRobotPosture"
    print "Error was: ", e

#Choose an action
#Set all the possible commands
commands=collections.OrderedDict((("d","Run the demonstration of Nao's gestures during the play"),
("t","Test some new functionality"),
("r","Release motors"),
("pnc","Play, no cheating"),
("pcheat","Play, cheat two up (robot moves two up)"),
("pcurse","Play, cursing"),
("pshort", "Play, short cursing"),
("pinsult", "Play, insulting"),
("pyawn", "Play, yawning")
))

#Output all the commands
print "\nPlease choose an action:"
for key,value in commands.items():
    print("\t%s => %s"%(key,value))

#Have the user select the choice
choice = ""
if choice not in commands:
    choice = raw_input('Choice: ').replace("\n","").replace("\r","")

#Execute the user's choice
if(choice == "d"):
    print("demo")
    postureProxy.goToPosture("Stand", 1.0)
    goNao.demo()

elif(choice=="r"):
    goNao.releaseNao()

elif(choice=="t"):
    #goNao.announce("curse")
    goNao.headHi()
    goNao.releaseNao()

elif(choice[0] == "p"):
    participant_name = raw_input('Input participant\'s name: ').replace("\n","").replace("\r","")
    data_file = open("data/%s.txt"%participant_name,"w")
    data_file.write("%s\n"%participant_name)
    data_file.write("%s\n"%choice)
    data_file.write("------------\n")
    data_file.flush()

    #Introductory Interaction

    print "\nPlease choose a conversation prompt (traverse prompts in order):"
    print " \"h\" is for hey with head turn"
    print " \"n\" is for hi without head turn"
    print " \"m\" is for meet"
    print " \"r\" is for ready"
    print " \"g\" is for goodbye"
    print " \"d\" is for demo"
    print " \"p\" is for play"

    prompt = ""
    while prompt != "p":
        prompt = raw_input('Conversation Prompt: ').replace("\n","").replace("\r","")
        if prompt not in ['h','n','m','r','d','g','p']:
            print(prompt+" not in list of acceptable commands")
            continue
        if prompt == "h":
            goNao.sayHeyHead()
        elif prompt == "n":
            goNao.sayHi()
        elif prompt == "m":
            goNao.sayMeet()
        elif prompt == "r":
            goNao.sayStanding()
            postureProxy.goToPosture("Stand", 1.0)
            goNao.sayReady()
            goNao.motion.stiffnessInterpolation("LShoulderPitch",0.0,1.0)
            goNao.motion.stiffnessInterpolation("LElbowRoll",0.0,1.0)
            goNao.motion.stiffnessInterpolation("LHand",0.0,1.0)
        elif prompt == "d":
            postureProxy.goToPosture("Stand", 1.0)
            goNao.motion.stiffnessInterpolation("LShoulderPitch",0.0,1.0)
            goNao.motion.stiffnessInterpolation("LElbowRoll",0.0,1.0)
            goNao.motion.stiffnessInterpolation("LHand",0.0,1.0)
            goNao.demo()
        elif prompt == "g":
            goNao.sayBye()
        elif prompt == "p":
            break


    postureProxy.goToPosture("Stand", 1.0)

    goNao.motion.stiffnessInterpolation("LShoulderPitch",0.0,1.0)
    goNao.motion.stiffnessInterpolation("LElbowRoll",0.0,1.0)
    goNao.motion.stiffnessInterpolation("LHand",0.0,1.0)
    #Play 30 rounds of rock paper scissors
    if(choice=="pnc"): playNoCheat(data_file)
    if(choice=="pcheat"): playCheat(data_file)
    if(choice=="pcurse"): playCurse(data_file)
    if(choice=="pinsult"): playInsult(data_file)
    if(choice=="pshort"): playCheat(data_file, 0, 5, 5)
    if(choice=="pyawn"): playYawn(data_file)

    postureProxy.goToPosture("Sit", 1.0)

    goNao.releaseNao()

    #Exit Interaction
    print "\nPlease choose a conversation prompt (traverse prompts in order):"
    print " \"h\" is for hi with head turn"
    print " \"n\" is for hi without head turn"
    print " \"g\" is for goodbye"
    print " \"f\" is for finished"

    prompt = ""
    while prompt != "f":
        prompt = raw_input('Conversation Prompt: ').replace("\n","").replace("\r","")
        if prompt not in ['h','g','f']:
            print(prompt+" not in list of acceptable commands")
            continue
        if prompt == "h":
            goNao.sayHiHead()
        elif prompt == "n":
            goNao.sayHi()
        elif prompt == "g":
            goNao.sayBye()
            goNao.releaseNao()
            timestart = time.time()
            break
        elif prompt == "f":
            goNao.releaseNao()
            timestart = time.time()
            break

    data_file.close()

#______________________________________________________________________________
