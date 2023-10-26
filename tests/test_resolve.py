import explicit_di as _di


class A:
    pass


class B:
    def __init__(self, a: A):
        self.a = a


class C:
    def __init__(self, b: B):
        self.b = b


def test_resolve():
    container = _di.Container()
    container.register(A)
    container.register(B)
    container.register(C)

    b = container.resolve(B)
    assert isinstance(b, B)
    assert isinstance(b.a, A)

    c = container.resolve(C)
    assert isinstance(c, C)
    assert isinstance(c.b, B)
    assert isinstance(c.b.a, A)
