
def contains(a, b):
    if b.lower() in a:
        return True
    else:
        return False

cities = ["stockholm", "new nork", "tokyo", "berlin"]

print(contains(cities, "Tokyo"))

