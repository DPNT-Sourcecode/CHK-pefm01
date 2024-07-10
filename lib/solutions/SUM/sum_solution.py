# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int) -> int:
    if 0 <= x <= 100 and 0 <= y <= 100:
        print("Both values are correct")
        return x+y
    else:
        raise ValueError('Both values needs to be in range 0-100')

