def findpeak(low, high, arr):

    mid = (low + high) // 2
    if mid == 0 or mid == len(arr) - 1:
        return "No peak element found"
    if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
        return arr[mid]
    elif arr[mid + 1] > arr[mid]:
        return findpeak(mid + 1, high, arr)
    else:
        return findpeak(low, mid - 1, arr)


if __name__ == "__main__":

    print("Enter the array : ", end=" ")
    arr = [int(x) for x in input().split()]

    peakel = findpeak(0, len(arr) - 1, arr)
    print(peakel)