# Python Module 02 - Exception Handling

## Key Concepts

**raise** → stops the function, throws error up the call stack  
**except** → catches the error, program continues  
**as e** → gives you access to the error message  

```python
raise ValueError("too cold")   # throw with message
raise                           # re-throw caught error (keeps traceback)
```

```python
except ValueError as e:
    print(e)          # "too cold"
    print(type(e))    # <class 'ValueError'>
```

**bare `except:` is bad** — catches everything including KeyboardInterrupt. Always be specific.

---

## Exercise 0 - First Exception

`int("abc")` raises `ValueError`. Catch it in `test_temperature`, not in `input_temperature`.

- `input_temperature` → raises
- `test_temperature` → catches and prints

Each input gets its own `try/except` block so the program continues after each error.

---

## Exercise 1 - Range Validation

0 and 40 are valid (limits included) → use `< 0` and `> 40`.

```python
if input < 0:
    raise ValueError(f"{input}°C is too cold for plants (min 0°C)")
elif input > 40:
    raise ValueError(f"{input}°C is too hot for plants (max 40°C)")
```

The `"Caught input_temperature error:"` prefix goes in `test_temperature`'s print, not inside `raise`.