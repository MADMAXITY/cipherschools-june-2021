def firstposition(num, low, high, arr):
    mid = (low + high) // 2
    if low == len(arr) or high < 0 or low > high:
        return None
    if arr[mid] == num:
        res = firstposition(num, low, mid - 1, arr)
        if res == None:
            return mid
        else:
            return res
    if arr[mid] < num:
        return firstposition(num, mid + 1, high, arr)
    if arr[mid] > num:
        return firstposition(num, low, mid - 1, arr)


def lastposition(num, low, high, arr):
    # print(low, high)
    mid = (low + high) // 2
    if low == len(arr) or high < 0 or low > high:
        return None
    if arr[mid] == num:
        res = lastposition(num, mid + 1, high, arr)
        if res == None:
            return mid
        else:
            return res
    if arr[mid] < num:
        return lastposition(num, mid + 1, high, arr)
    if arr[mid] > num:
        return lastposition(num, low, mid - 1, arr)


if __name__ == "__main__":
    arr = [int(x) for x in input("Enter array :").split()]
    n = int(input("Enter the number : "))
    firstpos = firstposition(n, 0, len(arr) - 1, arr)
    lastpos = lastposition(n, 0, len(arr) - 1, arr)
    print(firstpos, lastpos)
