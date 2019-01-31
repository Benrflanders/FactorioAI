import os
import time
import goal_handler
import bot_handler



#check for changes in the number of lines in the file
def poll_file(curr_num_lines, fp="/Users/benflanders/Library/Application Support/factorio/script-output/curr_sess.txt"):
    with open(fp, 'r') as f:
        num_lines = 0
        for line in f:
            num_lines += 1
            if num_lines > curr_num_lines:
                print(curr_num_lines, ": ", line)
                curr_num_lines = num_lines
                return curr_num_lines, line

        #if there weren't any lines in the file
        if num_lines == 0:
            curr_num_lines = 0 #reset the number of lines tracker to 0

    return curr_num_lines, ""

    #check the number of lines in the curr-sess file


def main():
    #if using a mac
    file_path = "/Users/benflanders/Library/Application Support/factorio/script-output/curr_sess.txt"
    if(os.path.exists(file_path)):
        print("Path exists!")

    #start factorio

    #initialize bot and bind bot to screen

    #bind bot to screen

    #initialize the goal for the current session
    goal = goal_handler.goal("copper-ore-touch,1")

    #check to see if the goal was initialized correctly
    goal.print_current_goals()

    curr_num_lines = 0   
    #get the most recently appended line that has not been read before
    while(True):

        #check for goal updates
        curr_num_lines, line = poll_file(curr_num_lines)
        if line is not None and line is not "":
            goal.update_progress(line)
            line = ""

        #have the bot take action




if __name__ == '__main__':
    main()