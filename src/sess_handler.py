import os
import time
import goal_handler
import factorio_screen_handler


def main():
    #if using a mac
    file_path = "/Users/benflanders/Library/Application Support/factorio/script-output/curr_sess.txt"
    if(os.path.exists(file_path)):
        print("Path exists!")

    #start a factorio game
    factorio_screen_handler.begin_game()

    #initialize bot
        
    #initialize the goal for the current session
    goal = goal_handler.goal("copper-ore,5")

    #check to see if the goal was initialized correctly
    goal.print_current_goals()

    while(True):

        #check for goal updates
        goal.check_for_updates()

        #have the bot take action




if __name__ == '__main__':
    main()