from FlowOfDestiny.src.exceptions.custom_exceptions import NotEnoughMP, NotEnoughHP


class HitPoints:

    def __init__(self, hp: float):
        self.max_hp = hp
        self.current_hp = hp

    
    def heal(self, amount: float):
        if self.current_hp + amount > self.max_hp:
            self.current_hp = self.max_hp
        else:
            self.current_hp += amount


    def take_damage(self, amount: float):
        self.current_hp -= amount

    def use_hp(self, amount: float):
        if self.current_hp <= amount:
            raise NotEnoughHP
        else:
            self.current_hp -= amount


    def regen(self, amount):                            # Need to bind and write test
        if self.current_hp + amount > self.max_hp:
            self.current_hp = self.max_hp
        else:
            self.current_hp += amount


class ManaPoints:


    def __init__(self, mp: float):
        self.max_mp = mp
        self.current_mp = mp

    
    def heal(self, amount: float):
        if self.current_mp + amount > self.max_mp:
            self.current_mp = self.max_mp
        else:
            self.current_mp += amount


    def use_mana(self, amount: float):
        if amount > self.current_mp:
            raise NotEnoughMP
        self.current_mp -= amount
        

    def regen(self, amount):  
        if self.current_mp + amount > self.max_mp:
            self.current_mp = self.max_mp
        else:                                        # Need to bind and write test
            self.current_mp += amount
