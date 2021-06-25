def findmissing(n, arr):
    arr.append(0)
    for i in arr:
        num = i % (n + 1)
        arr[num - 1] += n + 1
    for i in range(n + 1):
        if arr[i] < n + 1:
            return i + 1


if __name__ == "__main__":
    n = int(input("Enter n : "))
    arr = [int(x) for x in input("Enter Array : ").split()]
    print(findmissing(n, arr))
