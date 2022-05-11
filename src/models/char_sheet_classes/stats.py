class Stats:
    """A class representing stats that can be on an item, or a character."""

    def __init__(self, stats: dict = {'STR': 0, 'INT': 0, 'VIT': 0, 'WIS': 0, 'DEX': 0, 'CHA': 0}):
        self._stats = stats


    def get_stats(self) -> dict:
        return self._stats

    
    def change_stats(self, stats):
        affected_stats = stats.get_stats()
        for stat in affected_stats:
            self._stats[stat] += affected_stats[stat]
