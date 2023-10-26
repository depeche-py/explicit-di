import explicit_di as _di


class A:
    pass


def test_inject():
    container = _di.Container()
    container.register(A)

    args = []

    def fn(some_arg: int, a: A):
        args.append((some_arg, a))

    container.inject(fn, some_arg=42)
    assert len(args) == 1
    assert args[0][0] == 42
    assert isinstance(args[0][1], A)
