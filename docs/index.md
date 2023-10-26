
Explicit DI is modern Python library for explicit Dependency Injection

## Requirements

Python 3.9+


## Installation

```bash
pip install explicit-di
# OR
poetry add explicit-di
```

## Example

```python
import explicit_di as _di


class A:
    pass


class B:
    def __init__(self, a: A, config : str):
        self.config = config
        self.a = a


class C:
    def __init__(self, b: B):
        self.b = b


def create_b(a: A):
    return B(a=a, config="foo")


def function_with_dependencies(one : int, two : str, my_c : C):
    print(my_c)


def main():
    container = _di.Container()
    container.register(A)
    container.register(B, create_b)
    container.register(C)

    b = container.resolve(B)
    assert isinstance(b, B)

    container.inject(function_with_dependencies, one=1, two="two")
```
