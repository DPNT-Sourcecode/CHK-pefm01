# noinspection PyShadowingBuiltins,PyUnusedLocal
def sum(x: int, y: int) -> int:
    if 0 <= x <= 100 and 0 <= y <= 100:
        print("Both values are correct")
    else:
        raise ValueError('Both values needs to be in range 0-100')
except ValueError as e:
    print(e)



