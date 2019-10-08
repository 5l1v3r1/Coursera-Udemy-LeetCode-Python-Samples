import time

username_list={'name':'password'}

def start():
    print('Hello there! This is my lovely homepage')
    time.sleep(1) # Wait for 1 seconds
    while True:
        start_answer=input('Do you have an account? Yes or no?\n').lower()
        time.sleep(1) # Wait for 1 seconds
        if start_answer == "yes" or start_answer == "y":
            print("That's good!. Please sign in your account")
            sign_in()
            break
        if start_answer == "no" or start_answer == "n":
            print("You need to create an account")
            sign_up()
            break
        else:
            print("Please only enter yes or no")
                       
def sign_up():
    print('WELCOME TO SIGN UP PAGE')
    time.sleep(1) # Wait for 1 seconds
    while True:
        username=input('Please enter a username.\nUsernames should be unique.').lower()
        if ' ' in username:
            print('Usernames should not include space. Please set it correctly!')
        elif username in username_list.keys():
            print('Sorry, this username has already taken. Please select another username.')
        else:
            print('Great! You can use {} as a username'.format(username))
            break
        continue
    while True:
        password=input('Please set your password:')
        password2=input('Please confirm your password:')
        if password != password2:
            print('Passwords didnt match. Please Try again.')
        else:
            print('Your account succesfully created!\nYou are redirecting to sign-in page.')
            username_list[username] = password
            sign_in()
            break
                       
def sign_in():
    print('WELCOME TO SIGN IN PAGE')
    time.sleep(1) # Wait for 1 seconds
    while True:
        username_check=input('What is your username?').strip()
        password_check=input('What is your password?')
        if username_check in username_list.keys() and username_list[username_check]==password_check:
            time.sleep(1) # Wait for 1 seconds
            print('*********\nWELCOME TO HOMEPAGE, {}!'.format(username_check))
            break
        else:
            print('Sorry your username-password didnt match. Please Try again.')
start()          