'''
The entry point for the Factorio AI program
'''
import os as os
import subprocess
from factorio import load_factorio

FACTORIO_PATH = os.path.abspath("/Applications/factorio.app")

#start the factorio application and pipe its outputs to the bot handler
def start_factorio():
    factorio = subprocess.Popen(["/bin/bash","-c","open /Applications/factorio.app"], stdout=subprocess.PIPE)
    #grab screen using win32gui


    return rc

def start_bot(factorio_app):
    bot = True
    return bot


def main():
    bot_list = [0, 0] # the list of current bots in the population

    for i in range(0, len(bot_list)):
        bot = bot_list[i]

    factorio_app = start_factorio()



    bot = start_bot(factorio_app) #bind a selected bot to the application

    #while bot has not completed the goal
    #run the bot

    #if bot completes the goal
    #get time to complete the goal
    #store completion time

    #next bot


if __name__ == '__main__':
    main()
    