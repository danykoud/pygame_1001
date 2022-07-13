pies = [' Pecan', 'Apple Crisp', ' Bean',  'Banoffee',  'Black Bun', ' Blueberry',' Buko', ' Burek',   'Tamale',  'Steak']

print('-----------------------------------------------------------')
print('Welcome to the House of Pies! Here are our pies:')


list=[]
continue_= 'y'
while continue_=='y':
    print('-------------------------------------------------')

    print('(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak')

    select= input('which pie would you like to order ? ')
    
    list.append(pies[int(select)])
    selection= pies[int(select)-1]
    print('-------------------------------------------------')
    print(f"Great! We'll have that {selection} right out for you.")
    
    continue_= input('would you like  to make another order? yes(y) and No (n) ')
    print('-------------------------------------------------------------------------------')

print(' you have ordered '+ str(len(list))  + ' '+'pie(s)')
print('-------------------------------------------------')
print('This is your list ')
def count_items(items):
    return {k:items.count(k) for k in items}

print(count_items(list))