class Mediator:
    def add_berries(self, compote, berries):
        pass

#Component1
class Compote:
    def __init__(self, mediator):
        self.berries = []
        self.mediator = mediator

    def add_berries(self, berries):
        self.berries.extend(berries)
        print("Berries added to the compote.")
        self.mediator.add_berries(self, berries)

#Component2
class BerryPicker:
    def __init__(self, mediator):
        self.berries = []
        self.mediator = mediator

    def pick_berries(self, count):
        self.berries = ["Berry"] * count
        print(f"Picked {count} berries.")
        self.mediator.add_berries(self, self.berries)

#ConcreteMediator
class BerryMediator(Mediator): #посередник який координує між Compote та BerryPicker
    def add_berries(self, sender, berries):
        if isinstance(sender, Compote):
            print(f"Compote received {len(berries)} berries.")
        elif isinstance(sender, BerryPicker):
            print(f"BerryPicker sent {len(berries)} berries to the mediator.")
"""           
коли Compote додає ягідки або BerryPicker забирає, то вони викликають метод add_berries посередника
який визначає як реагувати на цю подію
"""
# Використання паттерну Mediator
mediator = BerryMediator()

compote = Compote(mediator)
berry_picker = BerryPicker(mediator)

compote.add_berries(["Strawberry", "Blueberry"])
berry_picker.pick_berries(3)
