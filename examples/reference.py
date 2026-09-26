"""Reference implementation for John Brajer's Path Expansion mechanism."""
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class FutureState:
    name: str
    desirability: float
    probability: float = 1.0


def path_expansion_value(states: Iterable[FutureState]) -> float:
    """Score the desirable future state-space unlocked by an action.

    This is a reference metric, not a universal formula.
    """
    return sum(
        max(0.0, s.desirability) * min(1.0, max(0.0, s.probability))
        for s in states
    )


if __name__ == "__main__":
    print(path_expansion_value([
        FutureState("new collaborator", 0.8, 0.5),
        FutureState("reusable infrastructure", 0.9, 0.8),
    ]))
