def turn_right():
    for i in range(1,4):
        turn_left()
        
def move_left():
    turn_left()
    move()
    
def move_right_2():
    for i in range(1,3):
        turn_right()
        move()
    
def step():
    move()
    move_left()
    move_right_2()
    turn_left()
    
def step_6():
    for i in range(1,7):
        step()
    
step_6()
    
    




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
