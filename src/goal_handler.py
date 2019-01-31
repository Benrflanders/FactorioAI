'''
Load a factorio goal from a text file

@params:
    goal_text : a string of goal parameters, separate key of goal from value required with a comma,
        separate individual goals using a semicolon

'''
class goal:
    def __init__(self, goal_text):
        self.completion_percent = 0.00 #max 100
        if goal_text is not None and not "":
            temp_file_output = goal_text
        else:
            temp_file_output = "copper-ore-touch,1"
        print("Goal text:", goal_text)
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
    def update_progress(self, update_string):
        #if update string is a list
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
        except:     #otherwise let the console know that the completed goal is not in the goal list
            print(update_string, " is not an accepted value")
        
        #if a string is matched then decrement amount of that goal required


        return True
        #return the current progress completion

    #completion progress = sum of (percent complete of each individual goal) / number of goals    
    def get_goal_progress(self):
        sum_of_goal_completion_progress = 0.0
        num_goals = len(self.initial_goals) #get the total number of goals

        for goal in self.initial_goals:
            difference = self.initial_goals[goal] - self.curr_goals[goal] #difference between complete and required
            sum_of_goal_completion_progress += (difference*1.0/(self.initial_goals[goal]*1.0))

        self.completion_percent = sum_of_goal_completion_progress/num_goals
        return self.completion_percent

    #print out the goals and their values
    def print_current_goals(self):

        for goal in self.curr_goals:
            print(goal)
            print(self.curr_goals[goal])

    def print_initial_goals(self):
        for goal in self.initial_goals:
            print(goal)
            print(self.curr_goals[goal])

    #if the goal log file has any inputs send them to the goal updater
    def check_for_updates(self):
        fp="C:/Users/Ben/AppData/Roaming/Factorio/script-output/curr_sess.txt"
        with open(fp, 'r+') as f:
            for line in f:
                self.update_progress(line)
            f.truncate(0) # empty out the contents of the file

    #check if goal progress is 100% complete
    def is_complete(self):
        if(self.get_goal_progress() == 1.00):
            return True
        else:
            print("Completion Percent: ", self.completion_percent)
            return False


'''sample goal call structure
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
'''