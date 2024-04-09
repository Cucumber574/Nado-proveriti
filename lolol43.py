'''
Игрок:
    деньги
    инвертарь
    уровень
    опыт
    защита

Таверна:
    покупка
    продажа

Предмет:
    оружие
    зелья
    броня
'''
import os


class Weapon:
    '''Оружие'''
    def __init__(self, name: str, attack_power: int) -> None:
        self.name = name
        self.attack_power = attack_power

    def __str__(self) -> str:
        return f'{self.name} ({self.attack_power})'



class Player:
    '''Игрок'''
    def __init__(self, name: str, hp: int, weapon=None, level=1, xp=0) -> None:
        self.name = name
        self.hp = hp
        self.power = 1
        self.defautl_weapon = Weapon('Кулаки', 1)
        if weapon:
            self.weapon = weapon
        else:
            self.weapon = self.defautl_weapon
        self.level = level
        self.xp = xp


    def show(self) -> None:
        '''Строковое представление экземплра'''
        print(self.name.center(20, '-'))
        print('жизни: ', self.hp)
        print('сила: ', self.power)
        print('оружие: ', self.weapon)
        print('уровень: ' self.level)
        print('опыт: ' self.xp)
        print('-' * 20)

    def attack(self, enemy) -> None:
        '''Игрок атакует противника'''
        if self.hp <= 0:
            return
        damage = self.power
        enemy.hp -= damage
        print(self.name, 'атаковал', enemy.name)

    def get.award(self, enemy) -> None:
    os.system('cls')
    self.xp += enemy.level
    while self.xp > self.level * 10
        self.level += 1
    self.show()
    print(self.name, 'победил')
    print(self.name, 'получил', self.level, 'опыта')

class Game:
    '''Игра'''
    def __init__(self) -> None:
        self.player = Player('Вася', 100, Weapon('Меч Кладенец', 5))
        self.enemy = Player('Упырь', 100, None, 10, 0)
        self.is_fighting = False
        self.fight()


    def fight(self) -> None:
        '''Сражение'''
        self.is_fighting = True
        while self.is_fighting:
            os.system('cls')
            self.player.show()
            self.enemy.show()
            self.player.attack(self.enemy)
            self.enemy.attack(self.player)
            self.check_winner()
            input('ENTER')

    def check_winner(self) -> None:
        '''Завершает игру победой'''
        if self.player.hp <= 0:
            print(self.enemy.name, 'победил')
            self.is_fighting = False
        elif self.enemy.hp <= 0:
            print(self.player.name, 'победил')
            self.is_fighting = False
            self.player.get_award(get.award)

Game()
