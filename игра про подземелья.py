import time
from random import choice
from random import randint


class character(object):
    def __init__(self, name, hp, atk):
        self.hp = hp
        self.atk = atk
        self.name = name


class Enemy(character):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)

    def attack(self, victim):
        victim.hp -= self.atk
        print(self.name, "нанёс удар:-%s" % self.atk)
        if victim.hp <= 0:
            print(victim.name, "повержен. Конец игры.")
            time.sleep(1)
            quit()
        else:
            print(victim.name, "теперь имеет", victim.hp, "очков здоровья")


class player(character):
    def __init__(self, hp, atk, name):
        super().__init__(hp, atk, name)
        self.exp = 0
        self.lvl = 0

    def attack(self, victim):
        victim.hp -= self.atk
        print(self.name, "нанёс удар:-%s" % self.atk)
        if victim.hp <= 0:
            print(victim.name, "повержен.")
            rnd_item()
            self.exp += 10
            if self.exp >= 100:
                self.level_up()
            return False
        else:
            print(victim.name, "теперь имеет %s очков здоровья" % victim.hp)
            return True

    def level_up(self):
        self.exp = 0
        self.lvl += 1
        print("Ваш уровень повышен! Ваш уровень:%s" % self.lvl)
        self.hp += 5
        self.atk += 3
        if self.lvl == 100:
            print(
                "Поздравляю! Вы достигли 100 уровня! Игра заканчивается. Пока!"
            )
            quit()


class_list = ["лучник", "рыцарь"]


def create_person(name, class_type):
    hp = 0
    atk = 0
    if class_type == class_list[0]:
        hp += 8
        atk += 5
        return player(name, hp, atk)
    elif class_type == class_list[1]:
        hp += 10
        atk += 4
        return player(name, hp, atk)
    else:
        print("Выберите пожалуйста существующего героя!")
        time.sleep(1)
        quit()


person = []
print("Введите имя:")
person.append(input())
print("Введите класс игрока. Доступные классы:", end=" ")
for x in class_list:
    print(x, end=" ")
print()
person.append(input().lower())
player2 = create_person(person[0], person[1])
print(person)
person.clear()
print("Главный герой:%s. Здоровье:%s. Урон:%s. Опыт:%s. Уровень:%s." %
      (player2.name, player2.hp, player2.atk, player2.exp, player2.lvl))
print("Приветствую тебя герой!")

monstername_list = ["Гоблин", "Тролль", "Огр"]


def create_monster():
    rnd_name = monstername_list[randint(0, len(monstername_list) - 1)]
    rnd_hp = randint(10, 20) + player2.lvl * 5
    rnd_atk = randint(2, 5) + player2.lvl * 2
    return Enemy(rnd_name, rnd_hp, rnd_atk)


def fight_choice():
    answer = input("[Атаковать] [Бежать]").lower()
    if answer == "атаковать":
        attack_fight = player2.attack(monster)
        if attack_fight:
            time.sleep(1)
            monster.attack(player2)
            fight_choice()
    elif answer == "бежать":
        print("Функция не реализована!")
        fight_choice()
    elif answer == "убить":
        monster.hp = 1
        print('''Здоровье противника теперь на 1!
    Пропишите команду Атаковать чтобы убить его!''')
        fight_choice()
    else:
        print("Выбирайте из того что есть!")
        fight_choice()


def create_weapon():
    weapon_type_list = ["меч", "лук", "топор", "копьё", "меч богов"]
    weapon_rare_dict = {
        1: "обычный",
        2: "редкий",
        3: "эпический",
        4: "легендарный",
        5: "божественный"
    }
    rnd_type = weapon_type_list[randint(0, len(weapon_type_list) - 1)]
    rnd_rare = choice(list(weapon_rare_dict.keys()))
    if rnd_type == weapon_type_list[0]:
        player2.atk = player2.atk + 5 * rnd_rare
    elif rnd_type == weapon_type_list[1]:
        player2.atk += 4 * rnd_rare
    elif rnd_type == weapon_type_list[2]:
        player2.atk += 8 * rnd_rare
    elif rnd_type == weapon_type_list[3]:
        player2.atk += 6 * rnd_rare
    elif rnd_type == weapon_type_list[4]:
        player2.atk += 10 * rnd_rare
    return rnd_type, weapon_rare_dict[rnd_rare]


def create_heal():
    heal_sizedict = {
        5: "Малая хилка",
        10: "Средняя хилка",
        15: "Большая хилка",
        20: "Огромная хилка"
    }
    rnd_heal_size = choice(list(heal_sizedict.keys()))
    player2.hp += rnd_heal_size
    return heal_sizedict[rnd_heal_size]


def rnd_item():
    choice_list = ("weapon", "heal", 1, 2, 3, 4, 5, 6, 7)
    heal_weapon_choice = choice(list(choice_list))
    if heal_weapon_choice == "weapon":
        weapon = create_weapon()
        print("Вам выпало новое оружие! %s %s" % (weapon[0], weapon[1]))
    elif heal_weapon_choice == "heal":
        heal = create_heal()
        print("Вам выпала хилка! %s" % heal)
    else:
        print("Вам ничего не выпало! :(")


while True:
    event = randint(0, 1)
    if event == 0:
        print("Вам никто не попался на вашем пути.")
        time.sleep(1)
    elif event == 1:
        print("Вам встретился монстр!")
        monster = create_monster()
        print("Имя:%s. Здоровье:%s. Урон:%s." %
              (monster.name, monster.hp, monster.atk))
        print(
            "Главный герой:%s. Здоровье:%s. Урон:%s. Опыт:%s. Уровень:%s." %
            (player2.name, player2.hp, player2.atk, player2.exp, player2.lvl))
        fight_choice()
        time.sleep(1)
