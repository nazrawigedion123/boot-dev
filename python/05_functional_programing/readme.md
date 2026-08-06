# Functional programing
Functional programing is a style of programing where we compse functions instead of mutating functions
- Declears how things happen.

``` python

return clean_windows(add_gas(create_car()))
```
## Core pillars

### 1. Pure functions 
#### Functions given the same input give out the same out puts, no random variables invloved.

### 2. Immutablility
#### Data cannot be modified after creation

##### Tuples vs lists

Both tuples and lists are ordered collections of values but tuples are immutable and list are mutable.

###### Lists are mutable
``` python

ages : list[int]=[16,21,30]


ages.append(80)
#[16,21,30,80]
```
###### Tuples are immutable

``` python 

ages: tuple[int, ...] = (16, 21, 30)
# note the comma after 80! It's required for a single-element tuple
more_ages: tuple[int, ...] = (80,)
# 'all_ages' is a brand new tuple
all_ages: tuple[int, ...] = ages + more_ages
# (16, 21, 30, 80)

# or we can even reassign the same variable to point to a new tuple:
ages = ages + more_ages
# (16, 21, 30, 80)
```
![oop vs fp](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/mnrQXGV-653x543.png)
