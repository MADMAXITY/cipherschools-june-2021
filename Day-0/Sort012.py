def sortColors(arr):
    n = len(arr)
    l = 0
    m = 0
    h = n - 1
    while m <= h:
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            m += 1
            l += 1
        elif arr[m] == 2:
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1
        else:
            m += 1
    return arr


if __name__ == "__main__":
    arr = [int(x) for x in input("Enter Array : ").split()]
    print(" ".join([str(x) for x in sortColors(arr)]))
