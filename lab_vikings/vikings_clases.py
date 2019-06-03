# Project lab-data-vikings
import random as rd


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
        saxon_soldier=rd.choice(self.saxon_army)
        viking_soldier=rd.choice(self.viking_army)
        damage=viking_soldier.strength
        msg=saxon_soldier.receive_damage(damage)
        if msg=="A Saxon has died in combat":
            self.saxon_army.pop(0)
        return msg
    def saxon_attack(self):
        saxon_soldier = rd.choice(self.saxon_army)
        viking_soldier = rd.choice(self.viking_army)
        damage = saxon_soldier.strength
        msg = viking_soldier.receive_damage(damage)
        if msg == f'{viking_soldier.name} has died in combat':
            self.viking_army.pop(0)
        return msg
    def show_status(self):
        resultado=""
        if len(self.viking_army)==0:
            result="Saxons have fought for their lives and survive another day..."
        elif len(self.saxon_army)==0 :
            result="Vikings have won the war of the century!"
        else :
            result= "Vikings and Saxons are still in the thick of battle."
        return result

