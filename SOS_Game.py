#SOS Game
def question(): 
    while True:
        question=input('\nDo you want to the play? Please type Y or N: ')
        if question=='N':
            print('OK.Goodbye')
            break
        elif question=='Y':
            game()
        else:
            print('Opps!, Please write Y or N')
            continue
    
def game():
    print('OK. Lets start the game!\nInput your choice by one bye\nFirstly, User1:\n')
    board=['#','X','O','O','O','X','O',' ',' ',' ']
    print('|', board[7],'|', board[8],'|',board[9],'|','\n-------------','\n|', board[4],'|', board[5],'|',board[6],'|','\n-------------','\n|',board[1],'|', board[2],'|',board[3],'|')
    user_1=0
    user_2=0
    while True:
        board_position = int(input('Please enter a number between 1-9 for the board position: '))
        if board_position<1 or board_position>9:
            print('Opps!, It is out of  1-9')
            continue
        elif board[board_position]=='X' or board[board_position]=='O':
            print(f'Opps!, the {board_position} is not suitable.\nChoice another position')
            continue
        else:
            if user_1<=user_2:
                from IPython.display import clear_output
                clear_output()
                user_1 +=1
                board[board_position]='X'
                print('|', board[7],'|', board[8],'|',board[9],'|','\n-------------','\n|', board[4],'|', board[5],'|',board[6],'|','\n-------------','\n|',board[1],'|', board[2],'|',board[3],'|')
                if board[1]==board[2]==board[3]=='X' or board[4]==board[5]==board[6]=='X' or board[7]==board[8]==board[9]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[3]==board[6]==board[9]=='X' or board[1]==board[5]==board[9]=='X' or board[3]==board[5]==board[7]=='X':
                    print('Congratulations...\nUser1 WIN THE GAME')
                    break
                    question()
                elif ' ' not in board:
                    print('The result is TIE. No one is win!')
                    break
                    question()               
                else:
                    print('Now User2 will select..')
                    continue
            elif user_1>user_2:
                from IPython.display import clear_output
                clear_output()
                user_2 +=1
                board[board_position]='O'
                print('|', board[7],'|', board[8],'|',board[9],'|','\n-------------','\n|', board[4],'|', board[5],'|',board[6],'|','\n-------------','\n|',board[1],'|', board[2],'|',board[3],'|')
                if board[1]==board[2]==board[3]=='O' or board[4]==board[5]==board[6]=='O' or board[7]==board[8]==board[9]=='O' or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[3]==board[6]==board[9]=='O' or board[1]==board[5]==board[9]=='O' or board[3]==board[5]==board[7]=='O':
                    print('Congratulations...\nUser2 WIN THE GAME')
                    break
                    question()
                elif ' ' not in board:
                    print('The result is TIE. No one is win!')
                    break
                    question()  
                else:
                    print('Now User1 will select..')
                    continue
                    

print('Welcome to Tic Tac Toe game')
question()