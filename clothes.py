
clothes = [("pants",20 ), ("shirt",23), ('jacket',50),('shorts',10),('t-shirt',5)]
dirham = lambda data : (data[0], round(data[1]*9.50))
clothes_MAD =  list(filter( lambda data : data[1] <= 150 , list(map(dirham , clothes))))
# print(clothes_MAD)
fruits = ['orange','apple','bannana'] 
fruit_price = [35 , 12 , 22 ]
fruit_location = ['tangier' , 'marackech','agadir']
print(list(zip(fruits , fruit_price , fruit_location)))

cloth_sorted = sorted(clothes,key=lambda data : data[0])
print(cloth_sorted)