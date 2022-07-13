list_= ['pen','mouse','tv', 'box', 'books']
var= 2
new_list=[0,0,0,0,0]

# for i in range(var):
#     user= input('select item: ')
#     new_list.append(list_)

# print(new_list)

# print( 'choose items')
# print('1 ' 'pen','2 ' 'mouse','3 ' 'tv', '4 ' 'box','5 ' 'books')
# for items in list_:
#     print(items)

# for i in range(var):

#     input_= input('enter items you like ')
#     new_list.append(list_[int(input_)-1])
#     new_list_UPPER= [ lst.lower() for lst in new_list]
# for items in new_list_UPPER:
#     print(items)

# for index, values in enumerate(new_list_UPPER):
#     print(f'{index} {values}')

ans='y'

while ans=='y':
    input_= int(input('enter items you like '))

    user_input= input_ - 1
    new_list[user_input]+=1
    ans=input()

for i in range(len(new_list)):
    c= str(new_list[i])
    v=str(list_[i])
    print('('+c+')' + ' '+v)
