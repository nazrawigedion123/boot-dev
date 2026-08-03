# Polymorphism
'poly'='many'
'morph'='form'


### Polymorphism is the ability of variable, function or an object to take multiple form.

``` python
class Creature:
    def move(self) -> None:
        print("the creature moves")


class Dragon(Creature):
    def move(self) -> None:
        print("the dragon flies")


class Kraken(Creature):
    def move(self) -> None:
        print("the kraken swims")


creatures: list[Creature] = [Creature(), Dragon(), Kraken()]
for creature in creatures:
    creature.move()
# prints:
# the creature moves
# the dragon flies
# the kraken swims
```


we can put every instances of the classes in a list and call move on them.

### Operator overloading
Operator overloading is a kind of built in polymorphism in python to override operators for custome classes or types.
for example the operator '+' acts diffrently for int and str.

``` python
print(3 + 4)
# 7

print("three " + "four")
# three four
```
Custom classes on the other hand don't have any built-in support for those operators:
``` python
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Point") -> "Point":
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# p3 is (6, 8)
```
|Operation |Operator| Mehtod|
|:---|:---|:---|
|Addition|+| __add__|
|Substration|-|__sub__|
|Multiplication|*|__mul__|
|Power|**|__pow__|
|Division |	/ |	__truediv__|
|Floor Division 	|// |	__floordiv__ |
|Remainder | (modulo) |	% |	__mod__ |
|Bitwise Left Shift |	<< |	__lshift__ |
|Bitwise Right Shift 	|>> |	__rshift__ |
|Bitwise |AND 	|& |	__and__ |
|Bitwise |OR 	| 	__or__ |
|Bitwise |XOR 	|^ |	__xor__ |
|Bitwise |NOT 	|~ 	|__invert__ |

## Overriding built-in methods

for example we can instruct our class how its instance should be printed using an __str__ method.


``` python 

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


p1 = Point(4, 5)
print(p1)
# <Point object at 0xa0acf8>
```

``` python

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"


p1 = Point(4, 5)
print(p1)
# prints "(4,5)"
```
