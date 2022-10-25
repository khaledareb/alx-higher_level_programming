def random_func(name: str, age: int, weight: float) -> str:
    print("Name :", name)
    print("Age :", age)
    print("Weight :", weight)

    return "{} is {} years old and weighs {}".format(name, age, weight)

print(random_func("Derek", 89, 165.5))

print(random_func(89, "Derek", "Turtler"))

print(random_func.__annotations__)