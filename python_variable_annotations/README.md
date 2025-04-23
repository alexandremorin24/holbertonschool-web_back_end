# Python - Variable Annotations

## 🚀 Learning Objectives

- Understand and use type annotations in Python
- Annotate function parameters and return types
- Use complex types like `List`, `Tuple`, `Union`, `Callable`, etc.
- Understand and apply duck typing
- Check type safety using `mypy`

---

## ✅ Requirements

- Python 3.9
- Code must follow `pycodestyle` (v2.5)
- All files are executable and start with `#!/usr/bin/env python3`
- Each file, class, and function includes a docstring
- Type checks are validated using `mypy`

---

## 📁 Files and What They Do

| File                    | What It Does                                                  |
|-------------------------|----------------------------------------------------------------|
| `0-add.py`              | Adds two floats                                               |
| `1-concat.py`           | Concatenates two strings                                      |
| `2-floor.py`            | Returns the floor (int) of a float                            |
| `3-to_str.py`           | Converts a float to a string                                  |
| `4-define_variables.py` | Defines annotated variables                                   |
| `5-sum_list.py`         | Returns the sum of a list of floats                          |
| `6-sum_mixed_list.py`   | Returns the sum of a mixed list (ints and floats)            |
| `7-to_kv.py`            | Returns a tuple with a string and the square of a number     |
| `8-make_multiplier.py`  | Returns a closure function that multiplies by a float        |
| `9-element_length.py`   | Uses duck typing to return (element, length) pairs           |

---

## 🧪 Examples

Here are some examples of type-annotated functions I implemented:

```python
from typing import List, Tuple, Union, Callable

def add(a: float, b: float) -> float:
    return a + b

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v ** 2))

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
```

---

## 🛠 Using `mypy`

To check that everything is correctly annotated:

```bash
pip install mypy
mypy 0-add.py
```
