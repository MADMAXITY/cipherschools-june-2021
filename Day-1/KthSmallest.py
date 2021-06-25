def kthsmallest(arr, k):
    arr.sort()
    return arr[k - 1]


if __name__ == "__main__":
    arr = [int(x) for x in input("Enter Array : ").split()]
    k = int(input("Enter K : "))
    print(kthsmallest(arr, k))