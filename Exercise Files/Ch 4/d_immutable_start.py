# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen = True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, newval):
        self.value2 = newval

obj = ImmutableClass()
print(obj.value1)

# TODO: attempting to change the value of an immutable class throws an exception
obj.value1 = "Another Value"
print(obj.value1)
### Error: dataclasses.FrozenInstanceError: cannot assign to field 'value1'

# TODO: even functions within the class can't change anything
obj.some_func(16)
print(obj.value2)

### Error: dataclasses.FrozenInstanceError: cannot assign to field 'value2'