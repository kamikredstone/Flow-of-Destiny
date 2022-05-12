from FlowOfDestiny.src.models.char_sheet_classes.stats import Stats

class StatusEffect:

    def __init__(self, name, affected_stats: Stats = 0, special_effects: list = None, level = 1):
        self._name = name
        self._affected_stats = affected_stats
        self._special_effects = special_effects

class PoisonEffect(StatusEffect):

    def __init__(self):
        super().__init__("Poison", Stats(), [])
        #Work in progress

