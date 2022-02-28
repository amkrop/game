from enumirat_items import item_enumeration

fruits = []
while True:
    item = input('name the fruit: ')
    item = item.strip()
    item = item.lower()
    if item == '':
        print("Please name the fruit,empty string is not accepted!!")
    elif item == 'stop':
        break    
    else:
        fruits.append(item)
        continue



item_enumeration(fruits)



