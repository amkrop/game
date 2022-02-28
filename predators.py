from typing_extensions import Self
from animals import Animals
from random import *
class Predators(Animals) :
    def __init__(self,name,gender,height,weight,speed,preys):
        super().__init__(name,gender,height,weight,)
        self.speed = speed
        self.preys = preys

    def hunt(self):
        list_of_preys = self.preys
        listingThePreys = list(list_of_preys.split(","))
        prey = choice(listingThePreys)
        article = "a"
        vowels = ("a","o","u","i","e")
        preyFirstLetter = prey.startswith(vowels)
        if preyFirstLetter : 
            article = "an"
        print( f"{self.name} is hunting {article} {prey}")
        return self
    
sba3 = Predators("lion","male",3,250,80,"zebra,wildebeest,buffalo,antelope")

sba3.hunt().eat(Predators(self.preys))