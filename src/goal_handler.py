'''
Load a factorio goal from a json file
'''
class goal:
    def __init__(self, file=""):
        self.completion_percent = 0 #max 100
        temp_file_output = "copper-ore,5;tin-ore,5"

        parsed_goals = self.parse_goal_input(temp_file_output)
        for goal in parsed_goals:
            print(goal)
            print(parsed_goals[goal])


    #convert a json file to a dictionary of goals
    def parse_goal_input(self, raw_goal):
        parsed_goals = {}
        split_goals = raw_goal.split(';') #goals are delimited by semicolons
        for goal in split_goals:
            single_goal = goal.split(',') #split again at each comma
            parsed_goals[single_goal[0]] = single_goal[1] #first part is the target, second is the amount
        return parsed_goals


    def update_progress(self, update_string):
        #TODO
        #if a string is matched 
        return 0
        #return the current progress completion

gl = goal()