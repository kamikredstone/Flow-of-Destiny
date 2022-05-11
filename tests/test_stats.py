from FlowOfDestiny.src.models.char_sheet_classes.stats import Stats

def test_stats_change():
    stat_obj = Stats()
    stats_to_change = Stats({'DEX': 3, 'STR': 4, 'INT': -2})
    stat_obj.change_stats(stats_to_change)
    assert stat_obj.get_stats() == {'STR': 4, 'INT': -2, 'VIT': 0, 'WIS': 0, 'DEX': 3, 'CHA': 0}
