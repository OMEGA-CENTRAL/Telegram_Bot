import os
from threading import Thread
import WorkBot.workBotMain as workBotMain
import UserBot.userBotMain as userBotMain
import timeAlgorithm

basedir = os.path.dirname(__file__)


def workBot(basedir):
    workBotMain.workBot(basedir)

def userBot(basedir):
    userBotMain.userBot(basedir)

def timeAlgorith():
    timeAlgorithm.startTimeWaiting()

function = Thread(target = workBot, args = (basedir,))
function_2 = Thread(target = userBot, args = (basedir,))
function_3 = Thread(target = timeAlgorith)
            
function.start()
function_2.start()
function_3.start()


