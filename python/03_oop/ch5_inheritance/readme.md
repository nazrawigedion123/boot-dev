# Inheritance 
Inheritance allows a "child" class, to inherit properties and methods from a "parent" class. It's a way to share code between classes. For example, say we have this Aircraft class:

``` python
class Aircraft:
    def __init__(self, height: int, speed: int) -> None:
        self.height = height
        self.speed = speed

    def fly_up(self) -> None:
        self.height += self.speed

""" here we are duplicating each definition for aircraft and then add unique properties for helicopter"""
class Helicopter:
    def __init__(self, height: int, speed: int) -> None:
        self.height = height
        self.speed = speed
        self.direction = 0

    def fly_up(self) -> None:
        self.height += self.speed

    def rotate(self) -> None:
        self.direction += 90

```


instead of duplicating code we can do 

```python


class Helicopter(Aircraft):
    def __init__(self, height: int, speed: int) -> None:
        super().__init__(height, speed)
        self.direction = 0

    def rotate(self) -> None:
        self.direction += 90

class Jet(Aircraft):
    def __init__(self, speed: int) -> None:
        # Jets always start on the ground
        super().__init__(0, speed)

    def go_supersonic(self) -> None:
        self.speed *= 2

```

The super() method returns a proxy of the parent class, meaning we can use it to call the parent class's constructor and other methods. So the Helicopter's constructor says "first, call the Aircraft constructor, and then additionally set the direction property".


### When using inheritance make sure child classes are a superset of the parent class. A good child class is a more specific type of its parent class
