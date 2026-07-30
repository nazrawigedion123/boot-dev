def destroy_walls(wall_health: list[int]) -> list[int]:
    healths: list[int] = []
    for w in wall_health:
        if w > 0:
            healths.append(w)
    return healths

