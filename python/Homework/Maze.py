def move_right():
    repeat 3 :
        turn_left()
    move()


while not at_goal():
    if right_is_clear():
        move_right()
    elif front_is_clear():
        move()
        while right_is_clear() and not at_goal():
            move_right()
    if wall_in_front():
        turn_left()
            
                
            
        
        
        
        
        
        
        
    


    
    




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
