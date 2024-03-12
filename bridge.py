# Абстракція
class Compote:
    def __init__(self, berries_source):
        self.berries_source = berries_source

    def make_compote(self):
        berries = self.berries_source.get_berrires()
        print(f"Making compote with {', '.join(berries)}.")

# Реалізація
class BerriesSource:
    def get_berrires(self):
        pass

# Конкретна реалізація
class FreshBerries(BerriesSource):
    def get_berrires(self):
        return ["Strawberry", "Blueberry"]

class FrozenBerries(BerriesSource):
    def get_berrires(self):
        return ["Raspberry", "Blackberry"]

# Використання паттерну Bridge
fresh_compote = Compote(FreshBerries())
fresh_compote.make_compote()

frozen_compote = Compote(FrozenBerries())
frozen_compote.make_compote()
