import mysql.connector as mys

sql_obj = mys.connect(
    host = 'localhost',
    user = 'root', 
    passwd = 'Edg33988',
    database = 'amazon'
)

cr = sql_obj.cursor()

query = f"SELECT * FROM shop;"
cr.execute(query)

def shop_scr():
    print('{:<10}{:<15}{:<10}{:<10}'.format('ProdID', 'Product Name', 'Price', 'Stock'))
    print('='*45)
    shop_table = cr.fetchall()
    for rec in shop_table:
        print('{:<10}{:<15}{:<10}{:<10}'.format(rec[0], rec[1], rec[2], rec[3]))
    cmds()

def purchase():
    pass
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