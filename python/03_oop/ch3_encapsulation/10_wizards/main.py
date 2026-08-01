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
        self.health=self.__stamina*100
        self.mana=self.__intelligence*10
 
    def get_fireballed(self, fireball_damage: int) -> None:
        fireball_damage-=self.__stamina
        self.health-=fireball_damage

    def drink_mana_potion(self, potion_mana: int) -> None:
        potion_mana+=self.__intelligence
        self.mana+=potion_mana
    def cast_fireball(
        self, target: "Wizard", fireball_cost: int, fireball_damage: int
    ) -> None:
        if self.mana<fireball_cost:
            raise ValueError(f"{self.name} can not cast fireball")
        self.mana-=fireball_cost
        target.get_fireballed(fireball_damage)

    def is_alive(self) -> bool:
        return self.health>0

