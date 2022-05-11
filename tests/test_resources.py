from FlowOfDestiny.src.models.char_sheet_classes.character_resources import HitPoints, ManaPoints
from FlowOfDestiny.src.exceptions.custom_exceptions import NotEnoughMP, NotEnoughHP


def test_hp_take_damage():
    hp_obj = HitPoints(100.0)
    hp_obj.take_damage(10.0)
    assert hp_obj.current_hp == 90.0

def test_hp_use():
    hp_obj = HitPoints(100.0)
    hp_obj.use_hp(50.0)
    assert hp_obj.current_hp == 50.0
    try:
        hp_obj.use_hp(60.0) 
    except NotEnoughHP:
        print(f"This should fail.")   
    assert hp_obj.current_hp == 50.0

def test_hp_heal():
    hp_obj = HitPoints(100.0)
    hp_obj.take_damage(10.0)
    hp_obj.heal(15.0)
    assert hp_obj.current_hp == 100.0

def test_mp_use():
    mp_obj = ManaPoints(100.0)
    mp_obj.use_mana(10.0)
    assert mp_obj.current_mp == 90.0
    try:
        mp_obj.use_mana(100.0)
    except NotEnoughMP:
        print(f"This should fail.")
    assert mp_obj.current_mp == 90.0
    mp_obj.use_mana(90)
    assert mp_obj.current_mp == 0

def test_mp_heal():
    mp_obj = ManaPoints(100.0)
    mp_obj.use_mana(50.0)
    mp_obj.heal(60)
    assert mp_obj.current_mp == 100
