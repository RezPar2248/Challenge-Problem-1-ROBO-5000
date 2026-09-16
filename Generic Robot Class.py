#Generic Robot Class
import random 

class Robot: 

    def __init__(robot):

        robot.initial_position = random.randint(1,5)

        robot.goal = robot.initial_position
        while(robot.goal == robot.initial_position):
            robot.goal = random.randint(1,5)

        robot.position = robot.initial_position 

    def return_position(robot):
        return robot.position
    
    

class Quadrotor(Robot):
    def return_type(quad):
        return("Quadrotor")

class Humanoid(Robot):
    def return_type(human):
        return("Humanoid")
    
class Differential_Drive(Robot):
    def return_type(diff):
        return("Differential Drive")
