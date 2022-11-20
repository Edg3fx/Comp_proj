from sqlconnec import login, register_acc, admin
from shop import cmds

def start_menu():

    print()
    print('='*40)
    print('\t\tMENU')
    print('='*40)
    print('''1. Register New account
2. Login to account
3. Quit''')
    print('='*40)

    ch = int(input("\nEnter choice\n>>> "))

    if ch == 1:
        register_acc()
        start_menu()
    elif ch == 2:
        logged_in = login()
        if logged_in:
            print('User successfully logged in')
            cmds()
            start_menu()
        else:
            start_menu()
    elif ch == 3:
        print('| (i) Program terminated')
    
    elif ch == 1000:
        x = admin()
        start_menu()
        if x == False:
            start_menu()

    else:
        print('| ERROR: Invalid user input please try again')
        start_menu()
    
start_menu()