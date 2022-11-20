import mysql.connector as mys

sql_obj = mys.connect(
    host = 'localhost',
    user = 'root', 
    passwd = 'Edg33988',
    database = 'amazon'
)

cr = sql_obj.cursor()

def login():

    username = input('Enter the username\n>>> ')
    password = int(input('Enter password\n>>> '))
    query = f"SELECT * FROM accounts WHERE Username = '{username}' && Password = '{password}';"
    cr.execute(query)
    details = cr.fetchall()
    
    if details == []:
        print('| ERROR: Invalid username or password')
    else:
        for i in details:
            for j in i:
                print(j,end = '\t')
            print()
        return True

def register_acc():

    try:
        username = input('Enter the username\n>>> ')
        password = int(input('Enter password\n>>> '))
        first_n = input("Enter first name\n>>> ")
        last_n = input('Enter last name\n>>> ')
        email = input('Enter email address\n>>> ')
        phone_no = input("Enter phone number\n>>> ")
    except TypeError:
        print('Wrong datatype for password try again\n')
        register_acc()

    query = f"INSERT INTO accounts values('{username}', '{password}', '{first_n}', '{last_n}', '{email}', '{phone_no}')"
    cr.execute(query)
    confirm = input(f"Are you sure this is accurate\n{query}\n>>> ") # To be deleted

    if confirm.upper() == 'Y':
        sql_obj.commit()
        print('| (i) Account created')
    else:
        sql_obj.rollback()
        print('| (i) Sign in process terminated')

def admin_login():
    adm_pass = input('Enter admin password\n>>> ')
    query = f"SELECT * FROM accounts WHERE Password = '{adm_pass}';"
    # print(query) 
    cr.execute(query)
    outp = cr.fetchall()
    if outp == []:
        print('| ERROR: Invalid Admin login')
        return False
    else:
        print('| (i) Successfully logged into admin')
        return True

def database_scr():
    query = f"SELECT * FROM shop;"
    cr.execute(query)
    print('{:<10}{:<15}{:<10}{:<10}'.format('ProdID', 'Product Name', 'Price', 'Stock'))
    print('='*45)
    shop_table = cr.fetchall()
    for rec in shop_table:
        print('{:<10}{:<15}{:<10}{:<10}'.format(rec[0], rec[1], rec[2], rec[3]))

def accounts_scr():
    query = f"SELECT * FROM accounts;"
    cr.execute(query)
    print('{:<10}{:<8}{:<12}{:<15}{:<20}{:<10}'.format('Username', 'Passwd', 'First name', 'Last name', 'Email ID', 'Phone number'))
    print('='*75)
    acc_list = cr.fetchall()
    for rec in acc_list:
        print('{:<10}{:<8}{:<12}{:<15}{:<20}{:<10}'.format(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5]))

def item_entry():
    query = f"SELECT * FROM shop;"
    cr.execute(query)
    info = cr.fetchall()
    L = [i[0] for i in info]
    last_val = max(L)
    print(last_val)
    prod = input('Enter new product name\n>>> ');
    price = int(input("Enter the new product price\n>>> "))
    stock = int(input("Enter the amount of products in stock\n>>> "))
    entry = f"INSERT INTO shop values({last_val+1}, '{prod}', {price}, {stock})"
    print(entry) # To be commented out
    cr.execute(entry)
    tf = input("Are you sure the values of the entry are correct?(y/n)\n>>> ")
    if tf.lower() == 'n':
        print('| (i) Entry aborted')
        sql_obj.rollback()
    elif tf.lower() == 'y':
        print('| (i) Entry has been entered')
        sql_obj.commit()

def admin():
    print('| (i) Admin mode activated\n\n\tADMIN LOGIN ')
    print('-'*30)
    verify = admin_login()

    if verify == True:
        print()
        print('='*40)
        print('\t    ADMIN COMMANDS')
        print('='*40)
        print('''1. Database display
2. Accounts screen
3. Stock change
4. New item entry
5. Quit''')
        print('='*40)

        ch = int(input("Enter the choice\n>>> "))

        if ch == 1:
            database_scr()
            admin()

        elif ch == 2:
            accounts_scr()
            admin()

        elif ch == 4:
            item_entry()
            admin()

        elif ch == 5:
            print('| (i) Quitting admin terminal')

        else:
            print('| ERROR: Invalid option please try again')
            admin()


