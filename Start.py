import os
from threading import Thread
import WorkBot.workBotMain as workBotMain
import UserBot.userBotMain as userBotMain

basedir = os.path.dirname(__file__)

<<<<<<< HEAD
def workBot(basedir):
    workBotMain.workBot(basedir)

def userBot(basedir):
    userBotMain.userBot(basedir)

function = Thread(target = workBot, args = (basedir,))
function_2 = Thread(target = userBot, args = (basedir,))
            
function.start()
function_2.start()
=======
workBotMain.workBot(basedir)
>>>>>>> 5c559efa46e1bedebacd7c3c6917db5c8667eee2
