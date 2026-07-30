def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    # your code here
    if player_power>enemy_defense:
        advantage=True
    elif player_power<enemy_defense:
        disadvantage=True
    else :
        evenly_matched =True
    return advantage, disadvantage, evenly_matched

