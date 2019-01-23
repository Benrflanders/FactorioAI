import os
import time

#if using a mac
file_path = "/Users/benflanders/Library/Application Support/factorio/script-output/curr_sess.txt"
if(os.path.exists(file_path)):
    print("Path exists!")


curr_num_lines = 0

#get the most recently appended line that has not beed read before
while(True):
    with open(file_path, 'r') as f:
        num_lines = 0
        for line in f:
            num_lines += 1
            if num_lines > curr_num_lines:
                print(curr_num_lines, ": ", line)
                curr_num_lines = num_lines

        #if there weren't any lines in the file
        if num_lines == 0:
            curr_num_lines = 0 #reset the number of lines tracker to 0

    #check the number of lines in the curr-sess file