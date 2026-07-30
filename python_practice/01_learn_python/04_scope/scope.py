def get_max_health(modifier, level):
    return modifier * level


modifier = 5
level = 10

# don't touch above this line

max_health = get_max_health(modifier, level)

# don't touch below this line

print(f"max_health is: {max_health}")
