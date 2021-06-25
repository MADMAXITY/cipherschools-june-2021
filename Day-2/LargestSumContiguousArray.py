def kedane(a):
    max_s = -(10 ** 5)
    for i in range(len(a)):
        if i != 0:
            a[i] = max(a[i], a[i] + a[i - 1])
        max_s = max(max_s, a[i])
    return max_s


if __name__ == "__main__":
    a = [int(x) for x in input("Enter Array : ").split()]
    print(kedane(a))
