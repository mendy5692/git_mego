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
        if wall_in_front() and wall_on_right():
            turn_left()
            if wall_on_right() and wall_in_front():
                turn_left()
            elif wall_on_right():
                move()
            else:
                move_right_2()
                turn_left()
        elif not wall_on_right():
            move_right_2()
        else:
            move()
go()
        


        
        
        
        
    


    
    




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
