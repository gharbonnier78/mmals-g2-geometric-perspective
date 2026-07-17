from dataclasses import dataclass
from typing import Sequence
import math

@dataclass(frozen=True)
class ConstraintResiduals:
    retention: float
    risk: float
    cost: float
    audit_visibility: float

    def admissible(self) -> bool:
        """Residual convention: all values must be <= 0."""
        return all(v <= 0.0 for v in (
            self.retention, self.risk, self.cost, self.audit_visibility
        ))

def project_halfspace(vector: Sequence[float], normal: Sequence[float], offset: float = 0.0) -> list[float]:
    """Project a vector onto {x: normal.x + offset <= 0}."""
    if len(vector) != len(normal):
        raise ValueError("vector and normal must have the same dimension")
    norm_sq = sum(n*n for n in normal)
    if norm_sq <= 0.0 or not math.isfinite(norm_sq):
        raise ValueError("normal must have finite non-zero norm")
    violation = sum(n*x for n, x in zip(normal, vector)) + offset
    if violation <= 0.0:
        return [float(x) for x in vector]
    scale = violation / norm_sq
    return [float(x - scale*n) for x, n in zip(vector, normal)]
