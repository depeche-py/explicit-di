from typing import Optional

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


class WithNoneUnion:
    def __init__(self, a: A | None):
        self.a = a


def test_resolve_none_union():
    container = _di.Container()
    container.register(A)
    container.register(WithNoneUnion)
    obj = container.resolve(WithNoneUnion)
    assert isinstance(obj, WithNoneUnion)
    assert isinstance(obj.a, A)


class WithOptional:
    def __init__(self, a: Optional[A]):
        self.a = a


def test_resolve_optional():
    container = _di.Container()
    container.register(A)
    container.register(WithOptional)
    obj = container.resolve(WithOptional)
    assert isinstance(obj, WithOptional)
    assert isinstance(obj.a, A)
