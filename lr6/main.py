import math
class Character:
    def __init__(self,hp,sp,dmg):
        self.hp = hp
        self.sp = sp
        self.dmg = dmg
    def strikes(self):
        return self.sp//(self.dmg/4)
    def death(self, damage):
        return math.ceil(self.hp/damage)
    def stat(self):
        print(f'HP: {self.hp}')
        print(f'SP: {self.sp}')
        print(f'DMG: {self.dmg}')
    def __eq__(self,other):
        return type(self) == type(other)
    def __add__(self, other):
        if self != other:
            raise TypeError("Only fuse single type!")
        else:
            return(Character(self.hp + other.hp, self.sp + other.sp, self.dmg + other.dmg))

class Boss(Character):
    def __init__(self,hp,sp,dmg,perk):
        super().__init__(hp,sp,dmg)
        self.perk = perk
    def stat(self):
        print(f'PERK: {self.perk}')
        super().stat()
    def __add__(self,other):
        if self != other:
            raise TypeError("Only fuse single type!")
        else:
            return(Boss(self.hp + other.hp, self.sp + other.sp, self.dmg + other.dmg,self.perk + other.perk))
    def death(self, damage):
        return super().death(damage)*2 # ...
    
class Weak(Character):
    def __init__(self,hp,sp,dmg,weak):
        super().__init__(hp,sp,dmg)
        self.weak = weak
    def stat(self):
        print(f'WEAK: {self.weak}')
        super().stat()
    def __add__(self,other):
        if self != other:
            raise TypeError("Only fuse single type!")
        else:
            return(Weak(self.hp + other.hp, self.sp + other.sp, self.dmg + other.dmg,self.weak + other.weak))
    def death(self, damage):
        return math.ceil(super().death(damage)/2) # ...

hero = Character(100,50,10)   # потребляет очков в 4 раза меньше урона
hero1 = Character(200,20,50)
hero.stat()
print(hero.strikes())

boss = Boss(1000,500,100,'Flame')
print(boss.death(hero.dmg))  # 1000 ХП Игрок наносит за 100 ударов но усиление делает босса в 2 раза крепче

print('--------------------------------------------------------------------')
# доп задание
print((hero + hero1).stat())
print(hero + boss)
