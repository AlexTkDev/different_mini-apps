# Documentation for the `Immutable` project

## Description
The `Immutable` project is designed to create immutable objects in Python. It includes the
`immutable` decorator and the `Immutable` class, which allows you to create an object whose value cannot be changed
after initialization.

## Main components

### 1. The `immutable` decorator
```python
def immutable(func):
    def wrapper(*args, **kwargs):
        raise AttributeError("Attempted to modify immutable object")

    return wrapper
```

- **Description**: The `immutable` decorator prevents the value of an object attribute from being changed.

Attempts to change the value of an attribute marked with this decorator raise an
`AttributeError` exception with the message "Attempted to modify immutable object". - **Usage**: 
This decorator is applied to setter methods in a class to prevent attribute values from being changed.

### 2. The `Immutable` class

```python
class Immutable:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    @immutable
    def value(self, value):
        pass
```

- **Attributes**:
- `__value`: A private property that stores the object's value. It cannot be directly modified.

- **Methods**:
- `value`: A property that can be used to get the value of the `__value` attribute.
- `value.setter`: A setter for the `value` property that is marked with the `immutable` decorator,
preventing the value from being changed.

## Usage example
```python
if __name__ == "__main__":
    immutable_obj = Immutable(42)
    print(immutable_obj.value + 5)  # Output: 47
    print(immutable_obj.value)  # Output: 42
    immutable_obj.value += 5  # Calls AttributeError
```

### Explanation:

- The example creates an object `immutable_obj` of the class `Immutable` with the initial value `42`.
- Attempting to change the value of the attribute `value` will raise an exception `AttributeError`, which confirms

that the object is immutable.

## Conclusion

The `Immutable` project demonstrates a simple way to implement immutable objects in Python
using decorators and properties.
This approach is useful in situations where you want to keep data immutable after it is created.
зменяемость данных после их создания.
