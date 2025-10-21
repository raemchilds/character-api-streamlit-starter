from dataclasses import dataclass
from typing import List, Optional
import random

@dataclass
class Character:
    name: str
    blind_spot: str
    flaw: str
    attitude: str
    agenda: str
    catchphrases: List[str]

SITUATIONS = [
    "at a funeral",
    "during a peasant uprising",
    "hosting a charity event for the poor",
    "in disguise among the villagers",
    "at a royal ball with foreign dignitaries",
    "judging a pie-eating contest",
    "leading a self-care seminar",
    "giving a motivational speech to rebels",
]

def pick_ironic_situation(c: Character) -> str:
    if c.blind_spot.lower().startswith("oblivious to her own privilege"):
        return "hosting a charity event for the poor"
    if c.agenda.lower() == "maintain power at all costs":
        return "during a peasant uprising"
    if "neurotic" in c.flaw.lower() or "indecisive" in c.flaw.lower():
        return "judging a pie-eating contest"
    return random.choice(SITUATIONS)

def generate_joke(c: Character, seed: Optional[int] = None, force_context: Optional[str] = None) -> dict:
    if seed is not None:
        random.seed(seed)
    situation = force_context or pick_ironic_situation(c)
    p0 = c.catchphrases[0] if c.catchphrases else "Oh dear!"
    p1 = c.catchphrases[1] if len(c.catchphrases) > 1 else p0

    templates = {
        "hosting a charity event for the poor":
            f"{c.name} smiles nervously and says, '{p0}—I do hope they don’t notice the diamond-encrusted donation box!'",
        "during a peasant uprising":
            f"{c.name} clears her throat and declares, '{p1} Can’t we settle this with a tea party instead?'",
        "judging a pie-eating contest":
            f"{c.name} bites her lip and whispers, '{p0}—Are any of these gluten-free?'",
        "at a funeral":
            f"{c.name} whispers, '{p0}—Do you think the casket clashes with the drapes?'",
    }
    line = templates.get(situation, f"{c.name} adjusts her crown and says, '{p0} I wasn’t expecting this at all!'")
    return {"situation": situation, "joke": line}
