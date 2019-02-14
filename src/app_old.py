'''
The entry point for the Factorio AI program
'''
import os as os
import subprocess

#FACTORIO_PATH = os.path.abspath("/Applications/factorio.app")
FACTORIO_PATH = os.path.join(r"C:\Users\Ben\Documents\factorio\bin\x64\factorio.exe")

#start the factorio application
def start_factorio():
    subprocess.call(["start", FACTORIO_PATH], shell=True)
    
    #mac os
    #factorio = subprocess.Popen(["/bin/bash","-c","open /Applications/factorio.app"], stdout=subprocess.PIPE)

    #grab screen using win32gui
    hwin = win32gui.GetDesktopWindow()

    return True

#determines how the factorio bot interacts with the windows gui
def start_bot():
    #win32gui


    bot = True
    return bot


def main():
    bot_list = [0, 0] # the list of current bots in the population

    for i in range(0, len(bot_list)):
        bot = bot_list[i]

    start_factorio()



    bot = start_bot(factorio_app) #bind a selected bot to the application

    #while bot has not completed the goal
    #run the bot

    #if bot completes the goal
    #get time to complete the goal
    #store completion time

    #next bot


if __name__ == '__main__':
    main()
    