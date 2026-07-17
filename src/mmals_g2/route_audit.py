from typing import Iterable

def route_regret(selected_loss: float, admissible_losses: Iterable[float]) -> float:
    losses = list(admissible_losses)
    if not losses:
        raise ValueError("at least one admissible route is required")
    return float(selected_loss - min(losses))
