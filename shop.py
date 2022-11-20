import mysql.connector as mys

sql_obj = mys.connect(
    host = 'localhost',
    user = 'root', 
    passwd = 'Edg33988',
    database = 'amazon'
)

cr = sql_obj.cursor()

def shop_scr():
    query = f"SELECT * FROM shop;"
    cr.execute(query)
    print('{:<10}{:<15}{:<10}{:<10}'.format('ProdID', 'Product Name', 'Price', 'Stock'))
    print('='*45)
    shop_table = cr.fetchall()
    for rec in shop_table:
        print('{:<10}{:<15}{:<10}{:<10}'.format(rec[0], rec[1], rec[2], rec[3]))
    cmds()

def purchase():
    prod_id = int(input('Enter Product ID of product to buy\n>>> '))
    stock = int(input("Enter the amount of products\n>>> "))
    cr.execute(f'SELECT * FROM shop WHERE Prod_ID = {prod_id}')
    stats = cr.fetchone()
    name, price = stats[1], stats[2]
    query = f"UPDATE shop SET Stock = Stock-{stock} WHERE Prod_ID = {prod_id}"
    cr.execute(query)
    print(f'The grandtotal for ({stock}) {name} is ${stock*price:,.2f}\n')
    prompt = input("Complete transaction?(y/n)\n>>>")
    if prompt.lower() == 'y':
        sql_obj.commit()
        print('| (i) Transaction successful')
    elif prompt.lower() == 'n':
        sql_obj.rollback()
        print('| (i) Transaction aborted')
    cmds()

def cmds():
    print()
    print('='*40)
    print('\t SHOP MENU')
    print('='*40)
    print('''1. Shop Catalogue
2. Purchase item
3. Quit''')
    print('='*40)

    ch = int(input("\nEnter choice\n>>> "))
    
    if ch == 1:
        shop_scr()
    elif ch == 2:
        purchase()
    elif ch == 3:
        print('| (i) Back to menu')
    else:
        print('| ERROR: Wrong option')
        cmds()
