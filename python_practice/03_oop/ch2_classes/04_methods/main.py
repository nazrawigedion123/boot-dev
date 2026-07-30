class Wall:
    armor: int = 10
    height: int = 5

    def get_cost(self) -> int:
        return self.armor * self.height

    def fortify(self) -> None:
        self.armor*=2
