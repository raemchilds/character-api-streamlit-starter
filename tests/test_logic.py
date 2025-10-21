from character_logic import Character, pick_ironic_situation

def test_pick_irony_rule():
    c = Character("Q", "Oblivious to her own privilege", "Neurotic", "Polite", "Maintain power at all costs", ["Oh dear!"])
    assert pick_ironic_situation(c) in {
        "hosting a charity event for the poor",
        "during a peasant uprising",
        "judging a pie-eating contest",
    }
