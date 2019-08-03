#Rock Paper Scissors Game
you=''
comp=''
you_dash=0
comp_dash=0
tie=0
def start():
     while True:
        global you
        you=input('r,p or s:\n')
        if you=='r' or you=='p' or you=='s':
            print(f'your choice is: {you}')
            computer()
            break
        else:
            print('please select r,p or s please')

def computer():
    from random import randint
    lis=['r','p','s']
    global comp
    comp=lis[randint(0,2)]
    print(f'the computer choice is: {comp}')
    result()

def result():
    print('calculating....')
    global you
    global comp
    global you_dash
    global comp_dash
    global tie
    import time
    time.sleep(2)
    'r'<'p'
    'p'<'s'
    's'<'r'
    if you==comp:
        print('there is no win')
        tie+=1
        again()
    elif you>comp:
        print('you WIN')
        you_dash+=1
        again()
    elif you<comp:
        print('you lose')
        comp_dash+=1
        again()

def again():
    while True: 
        again=input('do yu want to play again? y or n...:\n')
        if again=='y':
            return start()
        elif again=='n':
            print(f'The Game is Over\nDash Board is:\nWin={you_dash}\nLose={comp_dash}\nTie={tie}')
            break
        elif again!='y' or again!='n':
            print('please select r,p or s please')

print('welcome')

start()
