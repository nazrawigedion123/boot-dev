def does_attack_hit(attack_roll, armor_class):
    if attack_roll==1:
        return False
    if attack_roll==20:
        return True
    if attack_roll>=armor_class:
        return True
    return False
