def display_current_value():
    print(f'Current Value: {current_value}')

def add (to_add):
    global current_value, last
    last = current_value
    current_value += to_add

def sub (to_sub):
    global current_value, last
    last = current_value
    current_value -= to_sub

def mul (to_mul):
    global current_value, last
    last = current_value
    current_value *= to_mul

def div (to_div):
    global current_value, last
    if to_div == 0:
        raise ZeroDivisionError('Dividing by 0.')
    last = current_value
    current_value /= to_div

def store():
    global memory
    memory = current_value

def recall():
    global current_value
    current_value = memory

def undo():
    global current_value, last
    last = current_value ^ last
    current_value = last ^ current_value
    last = last ^ current_value

if __name__ == '__main__':
    current_value = 0
    memory = 0
    last = 0
    print('Welcome to the calculator program.')
    display_current_value()
    add(5)
    display_current_value()
    mul(5)
    div(5)
    display_current_value()
    store()
    add(5)
    display_current_value()
    recall()
    display_current_value()
    # display_current_value() # 0
    # add(5) # 5
    # sub(2) 
    # display_current_value() # 3
    # undo() 
    # display_current_value() # 5
    # undo() 
    # display_current_value() # 3
    # mul(10)
    # display_current_value() # 30
    # undo() 
    # undo() 
    # display_current_value() # 30
    # undo() 
    # undo() 
    # undo() 
    # display_current_value() # 3