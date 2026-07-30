def player_status(health):
    if health<=0:
        return "dead"
    if health<=5:
        return "injured"
    return "healthy"
