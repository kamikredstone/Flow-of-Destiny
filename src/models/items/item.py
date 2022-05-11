from FlowOfDestiny.src.models.char_sheet_classes.stats import Stats
from uuid import uuid4
from FlowOfDestiny.src.excetions.custom_exceptions import ItemNotStackable, ItemAmountZero

class Item():

    def __init__(self, name: str, stackable: bool, placement: str, level_req: int, rarity: str, affected_stats: Stats, amount: int = 1):
        self._name = name
        self._ID = uuid4()
        self._stackable = stackable
        self._placement = placement
        self._level_req = level_req
        self._rarity = rarity
        self._affected_stats = affected_stats
        if (amount > 1 and stackable) or amount == 1:
            self._amount = amount
        elif amount == 0:
            raise ItemAmountZero("An item cannot exist with amount of zero.")
        else:
            raise ItemNotStackable("Unstackable items cannot have more than amount = 1.")

    def __str__(self):
        return self._name

    def isStackable(self):
        return self._stackable

    def get_affected_stats(self):
        return self._affected_stats

    def get_placement(self):
        return self._placement

    def get_id(self):
        return str(self._ID)

    def get_amount(self):
        return self._amount

    def change_amount(self, n):
        if self.isStackable():
            if n > self._amount and n < 0:
                self._amount = 0
            elif n < self._amount and n < 0:
                self._amount -= n
            elif n > 0:
                self._amount += n
        else:
            raise ItemNotStackable
            


    
class Weapon(Item):
    
    def __init__(self, name: str, stackable: bool = False, placement: str, level_req: int, rarity: str, affected_stats: Stats, damage, amount: int = 1):
        super().__init__(name, stackable, placement, level_req, rarity, affected_stats, amount)
        self._damage = damage


class Armor(Item):
    
    def __init__(self, name: str, stackable: bool = False, placement: str, level_req: int, rarity: str, affected_stats: Stats, armor, amount: int = 1):
        super().__init__(name, stackable, placement, level_req, rarity, affected_stats, amount)
        self._armor = armor


class Ring(Item):

    def __init__(self, name: str, stackable: bool = False, placement: str, level_req: int, rarity: str, affected_stats: Stats, effects: dict, amount: int = 1):
        super().__init__(name, stackable, placement, level_req, rarity, affected_stats, amount)
        self._effects = effects

class Amulet(Item):

    def __init__(self, name: str, stackable: bool = False, placement: str = "Neck", level_req: int, rarity: str, affected_stats: Stats, effects: dict, amount: int = 1):
        super().__init__(name, stackable, placement, level_req, rarity, affected_stats, amount)
        self._effects = effects

class Misc(Item):

    def __init__(self, name: str, stackable: bool = True, placement: str, level_req: int, rarity: str, affected_stats: Stats, amount: int = 1):
        super().__init__(name, stackable, placement, level_req, rarity, affected_stats, amount)
    

