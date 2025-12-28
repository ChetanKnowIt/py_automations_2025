# Automations

A simple Python CLI experiment that demonstrates:

- Reading command-line arguments
- Enforcing a fixed “magic number” of arguments
- Passing arguments to a controller
- Printing the current Python runtime version

This project is intentionally minimal and educational.

---

## 📦 Installation

Install the package using pip (wheel or source):

```bash
pip install automations
```

## 🚀 Usage

```
python -m automations.main <arg1> <arg2> <arg3>
```

Now Architecture is growing into something like  - 

automations/
├── cli.py          # input/output only
├── controller.py   # orchestration (rules)
├── domain.py       # pure logic (testable)
├── system.py       # OS / sys interactions
└── __init__.py

How testing can proceed?

```python
def test_magic_number_met():
    assert is_magic_number_met(3) is True
    assert is_magic_number_met(2) is False

def test_controller_success(monkeypatch):
    monkeypatch.setattr(
        "automations.system.get_python_version",
        lambda: "TEST"
    )

    result = run(["a", "b", "c"])
    assert result.python_version == "TEST"


```

FOR DEVELOPMENT USE UTILS BELOW WITH UV: 
===============================================

Check cache location:

uv cache dir


Clear cache:

uv cache clean


⚠️ This is optional — uv is designed to keep this cache.

Check cache location:

uv cache dir


Clear cache:

uv cache clean


⚠️ This is optional — uv is designed to keep this cache.




## License
MIT License
