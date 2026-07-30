# Encapsulation

Encapsulation is the practice of hiding complexity inside an object or a component. The simplest form of encapsulation is a **function**.

## Public and Private Members
* By default, every property and method in Python is **public**.
* Double underscores (`__`) are used to make a property or method **private** via name mangling.

### Code Example
```python
class Wall:
    def __init__(self, armor: int, magic_resistance: int) -> None:
        # Private properties
        self.__armor = armor
        self.__magic_resistance = magic_resistance

    def get_defense(self) -> int:
        # Public method accessing private data
        return self.__armor + self.__magic_resistance
```

> [!IMPORTANT]  
> Encapsulation is about **organization**, not security.


