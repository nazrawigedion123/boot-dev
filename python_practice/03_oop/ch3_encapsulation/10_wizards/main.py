"""
Encapsulation is the practice of hiding complexity inside 
Simplest form of encapsulation is a function

Public and private
##################
- by default every property and method are public 
- data member is a way to make property or method private
    
    class Wall:
        def __init__(self, armor: int, magic_resistance: int) -> None:
            self.__armor = armor
            self.__magic_resistance = magic_resistance

        def get_defense(self) -> int:
            return self.__armor + self.__magic_resistance



Encapsulation is about organization not security
"""
class Wizard:
    def __init__(self, name: str, stamina: int, intelligence: int) -> None:
        self.name=name
        self.__stamina=stamina
        self.__intelligence=intelligence
        self.health=stamina*100
        self.mana=intelligence*10
