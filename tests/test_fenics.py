import fenics as pde


def test_create_function_space():
    mesh = pde.UnitIntervalMesh(32)
    V = pde.FunctionSpace(mesh, 'CG', 2)
    assert False
