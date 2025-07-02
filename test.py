from typing import Annotated, get_type_hints, get_origin, get_args


def double(x: Annotated[int, (0, 100)]) -> int:
    type_hints = get_type_hints(double, include_extras=True)
    hint = type_hints['x']
    if get_origin(hint) is Annotated:
        hint_type, *hint_args = get_args(hint)
        low, high = hint_args[0]
        print(hint_type)  # int
        print(hint_args)  # value
        print(low)  # 0
        print(high)  # 100
        
        if low <= x <= high:
            return x * 2
        else:
            raise ValueError(f"Value {x} is out of range [{low}, {high}]")


result = double(111)
print(result)
