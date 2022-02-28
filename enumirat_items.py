def item_enumeration(item):
    enum_item = enumerate(item , 1)
    for i in enum_item:
        print(f"{i[0]} - {i[1]}")