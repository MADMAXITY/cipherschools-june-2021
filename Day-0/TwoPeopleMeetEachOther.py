def ifmeet(x1, x2, v1, v2):
    if x1 > x2 and v1 > v2:
        return False
    if x2 > x1 and v2 > v1:
        return False
    if abs(x1 - x2) / abs(v1 - v2) == int(abs(x1 - x2) / abs(v1 - v2)):
        return True
    return False
    pass


if __name__ == "__main__":
    x1 = int(input("Person 1 starting point : "))
    v1 = int(input("Person 1 speed : "))

    x2 = int(input("Person 2 starting point : "))
    v2 = int(input("Person 2 speed : "))
    if ifmeet(x1, x2, v1, v2):
        print("They Meet!")
    else:
        print("They do not meet!")
