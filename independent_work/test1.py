class Hero:
    def __init__(self,name , health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def attack_h (self, enemy):
        enemy.health = enemy.health - self.power
        print(f'{self.name} вдарив {enemy.name} на {self.power}')
        print(f'у {enemy.name} залишилось здоров\'я: {enemy.health}')
        

    def informaition_h(self):
        print(f'Герой: {self.name}, здоров\'я: {self.health}, сила :{self.power}')

class Monster:
    def __init__(self,name , health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack_m (self, enemy):
        enemy.health = enemy.health - self.power
        print(f'{self.name} вдарив {enemy.name} на {self.power}')
        print(f'у {enemy.name} залишилось здоров\'я: {enemy.health}')


    def informaition_m(self):
        print(f'Монстер: {self.name}, здоров\'я: {self.health}, сила :{self.power}')

class Battle:
    def __init__(self,fight):
        self.fight = fight
    

hero1 = Hero('Тор', 600, 80)
hero1.informaition_h()


monster1 = Monster('Гоблин', 200, 20)
monster1.informaition_m()

# hero1.attack_h(monster1)
# monster1.attack_m(hero1)

while hero1.health > 0 and monster1.health>0:
    hero1.attack_h(monster1)
    if monster1.health <= 0 :
        print(f'Перміг Герой {hero1.name} ')
        break
    monster1.attack_m(hero1)
    if hero1.health <= 0:
        print(f'Перміг Монстер {monster1.name}')
        break
    print('------------Наступний Раунд------------')