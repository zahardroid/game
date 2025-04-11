from abc import ABC, abstractmethod


# Шаг 1: Создание абстрактного класса Weapon
class Weapon(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):
    @property
    def name(self):
        return "меч"

    def attack(self):
        print(f"Боец наносит удар {self.name}ом.")
        return 50  # Урон достаточный для победы


class Bow(Weapon):
    @property
    def name(self):
        return "лук"

    def attack(self):
        print(f"Боец наносит удар из {self.name}а.")
        return 50


# Шаг 3: Модификация класса Fighter
class Fighter:
    def __init__(self):
        self.current_weapon = None

    def change_weapon(self, weapon: Weapon):
        self.current_weapon = weapon
        print(f"Боец выбирает {weapon.name}.")

    def perform_attack(self):
        if self.current_weapon:
            return self.current_weapon.attack()
        else:
            print("Боец без оружия!")
            return 0


# Класс Monster и механизм боя
class Monster:
    def __init__(self, health=50):
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Монстр побежден!\n")


# Шаг 4: Реализация демонстрации боя
def battle_demo():
    fighter = Fighter()

    # Бой с мечом
    monster = Monster()
    fighter.change_weapon(Sword())
    damage = fighter.perform_attack()
    monster.take_damage(damage)

    # Бой с луком
    monster = Monster()
    fighter.change_weapon(Bow())
    damage = fighter.perform_attack()
    monster.take_damage(damage)


if __name__ == "__main__":
    battle_demo()