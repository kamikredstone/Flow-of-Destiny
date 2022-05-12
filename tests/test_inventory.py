from FlowOfDestiny.src.models.items.item import Misc
from FlowOfDestiny.src.models.char_sheet_classes.inventory import Inventory
from FlowOfDestiny.src.exceptions.custom_exceptions import ItemNotInInventory, NotEnoughSpace
import unittest


class TestInventory(unittest.TestCase):


    def test_addition(self):
        char_inventory = Inventory()
        beetle_husk = Misc("Beetle Husk", "Common")
        char_inventory += beetle_husk
        assert char_inventory._space[0] == beetle_husk

        another_husk = Misc("Beetle Husk", "Common")
        char_inventory += another_husk
        assert char_inventory._space[0].get_amount() == 2

        limited_inv = Inventory(max_size = 0)
        with self.assertRaises(NotEnoughSpace):
            limited_inv += beetle_husk

    def test_subtraction(self):
        char_inventory = Inventory()
        beetle_husk = Misc("Beetle Husk", "Common")
        another_husk = Misc("Beetle Husk", "Common")
        char_inventory += beetle_husk
        char_inventory += another_husk
        char_inventory -= beetle_husk
        assert char_inventory._space[0].get_amount() == 1

        char_inventory -= another_husk
        assert len(char_inventory._space) == 0
        
        with self.assertRaises(ItemNotInInventory):
            char_inventory -= another_husk



