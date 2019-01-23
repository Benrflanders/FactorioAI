'''
Load a factorio goal from a json file
'''
class goal:
    def __init__(self, file=""):
        self.completion_percent = 0 #max 100
        temp_file_output = "copper-ore,5;tin-ore,5"

        self.curr_goals = self.parse_goal_input(temp_file_output) #parse the provided goals into a dictionary


    #convert a json file to a dictionary of goals
    def parse_goal_input(self, raw_goal):
        parsed_goals = {}
        split_goals = raw_goal.split(';') #goals are delimited by semicolons
        for goal in split_goals:
            single_goal = goal.split(',') #split again at each comma
            parsed_goals[single_goal[0]] = int(single_goal[1]) #first part is the target, second is the amount
        return parsed_goals


    def update_progress(self, update_string):
        #prepare the input string
        update_string = update_string.strip()
        update_string = update_string.replace(" ", "")

        try:
            x = self.curr_goals[update_string]
            x = x-1
            self.curr_goals[update_string] = x
            self.print_current_goals()
        except:
            print(update_string, " is not an accepted value")


        #x = x-1
        #self.curr_goals[update_string] = x
        
        #if a string is matched then decrement amount of that goal required
        return 0
        #return the current progress completion
    
    #print out the goals and their values
    def print_current_goals(self):

        for goal in self.curr_goals:
            print(goal)
            print(self.curr_goals[goal])


gl = goal()
gl.print_current_goals()
print(gl.update_progress('tin-ore'))