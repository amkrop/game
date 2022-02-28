

class Vehicles:

    def characteristics (self,doors,wheels,engine) :
        self.doors = doors
        self.wheels = wheels
        self.engine = engine
        
    def owner(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city


class Cars(Vehicles):
    def __init__(name,age,city):
        pass
        

suzuki = Vehicles(4,'hqsd1',5)

print(suzuki.engine)
                
        
        
