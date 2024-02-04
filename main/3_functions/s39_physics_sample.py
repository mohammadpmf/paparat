def calculate_time(distance: float, velocity:float) -> str:
    return f"{round(distance/velocity, 2)} hour"

def maximum_height(v0: float, g:float=9.8) -> float:
    max_height = v0**2/(2*g)
    return round(max_height, 2)

print(maximum_height(10, 2.5))

# print(calculate_time(2500, 700))