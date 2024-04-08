import copy
#Прототип — це породжувальний патерн проектування,
# що дає змогу копіювати об’єкти, не вдаючись у подробиці їхньої реалізації.
class Prototype:
    def clone(self):
        """Створює копію цього об'єкта."""
        return copy.deepcopy(self)

class BerryCompote(Prototype):
    def __init__(self, berries):
        self.berries = berries

    def add_berry(self, berry):
        self.berries.append(berry)

    def __str__(self):
        berry_types = ", ".join(self.berries)
        return f"Compot with: {berry_types}"


original_compote = BerryCompote(["blueberry", "raspberry"])
print(f"Original compot: {original_compote}")

cloned_compote = original_compote.clone()
cloned_compote.add_berry("cherry")
print(f"Clone and modify compot: {cloned_compote}")

# Переконуємось, що оригінал не змінився
print(f"Original compot after cloning: {original_compote}")

