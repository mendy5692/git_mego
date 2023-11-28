def turn_right():
    for i in range(3):
        turn_left()
        
def move_left():
    turn_left()
    move()
    
def move_right_2():
    for i in range(2):
        turn_right()
        move()
  
def go():
    while not at_goal():
        if wall_in_front():
            move_left()
            move_right_2()
            turn_left()
        else:
            move()
go()
        


        
        
        
        
    


    
    




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
