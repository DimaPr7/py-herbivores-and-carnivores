class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        if self.health >= 0:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return f"{{Name: {self.name}," \
               f" Health: {self.health}," \
               f" Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> None:
        if isinstance(herbivore, Herbivore) and herbivore.hidden is False:
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)
