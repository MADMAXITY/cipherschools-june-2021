def print_alternative(arr):
    low, high = 0, len(arr) - 1
    while high > low:
        print(arr[high], arr[low], end=" ")
        high -= 1
        low += 1
    if high == low:
        print(arr[high])


if __name__ == "__main__":
    arr = [int(x) for x in input("Enter array : ").split()]
    arr.sort()
    print_alternative(arr)
