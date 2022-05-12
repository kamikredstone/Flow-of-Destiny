from FlowOfDestiny.src.models.items.item import Item
from FlowOfDestiny.src.exceptions.custom_exceptions import NotEnoughSpace, ItemNotInInventory

class Inventory:

    def __init__(self, max_size: int = 25):
        self._space = []
        self._max_size = max_size
    
    def __iadd__(self, item: Item):
        if len(self._space)+1 < self._max_size:
            #item_uuid = item.get_id()
            if item.isStackable():
                for element in self._space:
                    if str(element) == str(item):
                        element.change_amount(1)
                        return self
                self._space.append(item)
                return self
            else:
                self._space.append(item)
                return self
        else:
            raise NotEnoughSpace
    
    def __isub__(self, item: Item):
        item_uuid = item.get_id()
        if item.isStackable():
            for element in self._space:
                if str(element) == str(item):
                    element.change_amount(-1)
                    if element.get_amount() == 0:
                        self._space.remove(element)
                        return self
                    return self
            raise ItemNotInInventory
        else:
            for element in self._space:
                if element.get_id() == item_uuid:
                    self._space.remove(element)
                    return self
            raise ItemNotInInventory


    def increase_size(self, n):
        self._max_size += n
