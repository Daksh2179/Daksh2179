import math
import logic
from logic import x

if __name__ == '__main__':

    mat = logic.start_game()
    
    while(True):
        if(x=='W' or x == 'W'):
            mat, flag = logic.move_up(mat)
            status = logic.get_current_state(mat)
        print(status)
        
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
            break
            
elif(x=='S' or x=='s'):
        mat, flag = logic.move_down(mat)
        status = logic.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
             breakpoint            
        
elif(x == 'A' or x == 'a'):
        mat, flag = logic.move_left(math)
        status = logic.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
        else:
             breakpoint
        
elif(x == 'D' or x == 'd'):
        mat, flag = logic.move_right(mat)
        status = logic.get_current_state(mat)
        print(status)
        if(status == 'GAME NOT OVER'):
            logic.add_new_2(mat)
            
        else:
            breakpoint
            
else:
        print("Invalid Key Pressed")
        
        print(mat)