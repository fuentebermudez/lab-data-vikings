# Project lab-data-vikings
import random


# Soldier (constructor, ataque y daño)
class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def attack(self):
        return self.strength
    def receive_damage(self,damage):
        self.health=self.health-damage
        

# Viking
class Viking(Soldier):
    def __init__(self,name,health,strength):
        super().__init__(health,strength)
        self.name=name
    def receive_damage(self,damage):
        self.health=int(self.health)-int(damage)
        if self.health>0:
            return f'{str(self.name)} has received {str(damage)} points of damage'
        else:
            return f'{str(self.name)} has died in act of combat'
    def battle_cry(self):
        return("Odin Owns You All!")
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    def receive_damage(self,damage):
        self.health = int(self.health) - int(damage)
        if self.health > 0:
            return f'A Saxon has received {str(damage)} points of damage'
        else:
            return f'A Saxon has died in combat'


# War
class War:
    def __init__(self):
        self.viking_army=[]
        self.saxon_army=[]
    def add_viking(self,viking):
        self.viking_army.append(viking)
    def add_saxon(self,saxon):
        self.saxon_army.append(saxon)
    def viking_attack(self):
        pass
    def saxon_attack(self):
        pass
    def show_status(self):
        pass

