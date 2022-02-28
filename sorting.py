numbers = []
range_of_numbers = int(input("rang of numbers "))
condition = True
while condition :
    input_number = int(input(''))
    numbers.append(input_number)
    numbers.sort()
    if len(numbers) == range_of_numbers and  input_number <= 32000 and range_of_numbers <= 100 :
        [print(i) for i in  numbers]
        print("________________")
        break
    
    
    
    


 

         
        
    