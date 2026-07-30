# Classes
Classes are special types in oop lanugages like python
It defines properties and methods
``` python 
class Soldier:
    def __init__(self, health:int)
        self.health=health

    # This is a method that reduces the
    # health of the soldier
    def take_damage(self, damage: int) -> None:
        self.health -= damage
```
## Methods 
Methods are functions that are directly tied to a class
### Constructor
It is a specific method called ``` ___init__```  that is called when you create a new instance of a class.
## Class Variables vs Instance Variables
``` python 
class Soldier:
    base_salary : int=5   # class variable 
    def __init__(self, health:int)
        self.health=health  # instance variable

    # This is a method that reduces the
    # health of the soldier
    def take_damage(self, damage: int) -> None:
        self.health -= damage
```

### Instance Variables
Instance Variables are declared in the constructor.
### Class Variables
Class Variables are shared between the objects of the same class

# Object
Object is an instance of a class

``` python
class Soldier:
    health: int = 5

    # This is a method that reduces the
    # health of the soldier
    def take_damage(self, damage: int) -> None:
        self.health -= damage

```

these below are an example of objects.


``` python
wall_maria = Wall(1, 2, 3)
wall_rose = Wall(4, 5, 6)
wall_sina = Wall(9, 8, 7)
```
