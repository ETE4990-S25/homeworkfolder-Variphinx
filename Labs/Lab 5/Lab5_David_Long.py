## My own Code to Test
## David Long


class Animals(object):

    def __init__(self,name,age,health):
        self.name = name 
        self.age = age
        self._health = health

    def get_health(self):
        return self._health


Products = {}

class Production(Animals):

    def __init__(self,name,age,health,product):
        super().__init__(name,age,health)
        self.product = product 

    def Make(self):
        if self.product in Products:
            Products[self.product] += 1
        else:
            Products[self.product] = 1
        return print(f"{self.name} made {self.product}!")


class Helping(Animals):

    def __init__(self,name,age,health,role,damage):
        super().__init__(name,age,health)
        self.role = role
        self.damage = damage ## To fend off wild animals

    def WhatRole(self):
        return print(f"{self.name} helps {self.role} on the farm")

    def DefendFarm(self, attacker):
        attacker._health = attacker._health - self.damage

        if attacker._health > 0:
            return print(f"{attacker.name} took {self.damage} damage from {self.name} and now has {attacker.get_health()} health")
        else:
            if attacker.__class__ == Dead:
                return print(f"{attacker.name} is already dead")
            else:
                attacker.__class__ = Dead  # Changes the object's class
                attacker.__init__(attacker.name, attacker.age)  # Reinitialize with Dead class constructor    ##Chatgpt was used to figure this out
                return print(f"{attacker.name} died and {self.name} saved the farm")
        
        
class Wild(Animals):

    def __init__(self,name,age,health,damage):
        super().__init__(name,age,health)
        self.damage = damage  ## Animals do damage to farm? 1-100

    def AttackFarm(self, Prey):
        Prey._health = Prey._health - self.damage

        if Prey._health > 0:
            return print(f"{Prey.name} took {self.damage} damage from {self.name} and now has {Prey.get_health()} health ")
        else:
            if Prey.__class__ == Dead:
                return print(f"{Prey.name} is already dead")
            else:
                Prey.__class__ = Dead  # Changes the object's class
                Prey.__init__(Prey.name, Prey.age)  # Reinitialize with Dead class constructor    ##Chatgpt was used to figure this out
                return print(f"{Prey.name} died at the hands of {self.name}")
        

class Dead(Animals):

    def __init__(self, name, age, product=None):
        super().__init__(name, age, 0)

    def DefendFarm(self, attacker):          ##Override functions so dead animals cannot do certain things
        return print(f"{self.name} has died at the age of {self.age} and can no longer defend the farm")
    
    def AttackFarm(self, Prey):
        return print(f"{self.name} was already killed at the age of {self.age} and can't attack the farm")
        
    def Make(self):
        return print(f"{self.name} has died at the age of {self.age} and can't make any more {self.product}")
    



##TEST LAB 5
