Soldier = dict[str, int]


def get_soldier_dps(soldier: Soldier)->int:
    return soldier["damage"]*soldier["attacks_per_second"]


def fight_soldiers(soldier_one: Soldier, soldier_two: Soldier) -> str:
    soldier_one_dps = get_soldier_dps(soldier_one) #soldier_one["damage"] * soldier_one["attacks_per_second"]
    soldier_two_dps = get_soldier_dps(soldier_two) # soldier_two["damage"] * soldier_two["attacks_per_second"]
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"
