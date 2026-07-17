from mmals_g2 import ConstraintResiduals, project_halfspace, route_regret

def test_admissible():
    assert ConstraintResiduals(-1, 0, -0.2, -3).admissible()
    assert not ConstraintResiduals(-1, 0.1, -0.2, -3).admissible()

def test_projection():
    out = project_halfspace([2.0, 0.0], [1.0, 0.0], 0.0)
    assert abs(out[0]) < 1e-9

def test_route_regret():
    assert abs(route_regret(0.6, [0.4, 0.7]) - 0.2) < 1e-12
