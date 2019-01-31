'''
Load a factorio goal from a text file

@params:
    goal_text : a string of goal parameters, separate key of goal from value required with a comma,
        separate individual goals using a semicolon

'''
class goal:
    def __init__(self, goal_text=""):
        self.completion_percent = 0.00 #max 100
        if goal_text is not None:
            temp_file_output = goal_text
        else:
            temp_file_output = "copper-ore-touch,1"

        self.initial_goals = self.parse_goal_input(temp_file_output) #parse the provided goals into a dictionary
        self.curr_goals = self.initial_goals.copy()
        self.curr_num_lines = 0 #current number of lines in the log output file

    #convert a json file to a dictionary of goals
    def parse_goal_input(self, raw_goal):
        parsed_goals = {}
        split_goals = raw_goal.split(';') #goals are delimited by semicolons
        for goal in split_goals:
            single_goal = goal.split(',') #split again at each comma
            parsed_goals[single_goal[0]] = int(single_goal[1]) #first part is the target, second is the amount
        return parsed_goals

    #update the progress made towards the goal by providing a single string of the mined item
    def update_progress(self, update_string_list):
        #if update string is a list
        for update_string in update_string_list:
            #prepare the input string
            update_string = update_string.strip()
            update_string = update_string.replace(" ", "")

            try:    #if a string is matched then decrement amount of that goal required
                x = self.curr_goals[update_string]
                x = x-1
                
                if x < 0:   
                    x = 0

                self.curr_goals[update_string] = x
                self.print_current_goals()
            except:
                print(update_string, " is not an accepted value")
        
        #if a string is matched then decrement amount of that goal required


        return True
        #return the current progress completion
    
    def get_goal_progress(self):
        difference = 0.0
        total = 0.0

        for goal in self.initial_goals:
            difference = self.initial_goals[goal] - self.curr_goals[goal]
            total = self.initial_goals[goal]

        self.completion_percent = difference/total
        return (difference/total)

    #print out the goals and their values
    def print_current_goals(self):

        for goal in self.curr_goals:
            print(goal)
            print(self.curr_goals[goal])

    def print_initial_goals(self):
        for goal in self.initial_goals:
            print(goal)
            print(self.curr_goals[goal])

    #check for changes in the number of lines in the file
    def poll_file(self, fp="/Users/benflanders/Library/Application Support/factorio/script-output/curr_sess.txt"):

        with open(fp, 'r') as f:
            num_lines = 0
            for line in f:
                updates = []
                num_lines += 1
                if num_lines > curr_num_lines:
                    print(curr_num_lines, ": ", line)
                    curr_num_lines = num_lines
                return curr_num_lines, line

            #if there weren't any lines in the file
            if num_lines == 0:
                curr_num_lines = 0 #reset the number of lines tracker to 0

        return curr_num_lines, ""

    #if the goal log file has changed then update the goals
    def check_for_updates(self):
        curr_num_lines, updates = self.poll_file(self.curr_num_lines)
        if line is not None and line is not "":
            self.update_progress(line)
            line = "" #delete out the line since the progress was tracked

        #check the number of lines in the curr-sess file

gl = goal()

print("Initial: ")
gl.print_initial_goals()
print("Current: ")
gl.print_current_goals()

print("Update..")
print(gl.update_progress('tin-ore'))
print("Goal completino progress: ")
print(gl.get_goal_progress())

print("Initial: ")
gl.print_initial_goals()
print("Current: ")
gl.print_current_goals()