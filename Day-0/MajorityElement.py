def findone(arr):
    count = 1
    element = arr[0]

    for i in range(1, len(arr)):
        if arr[i] == element:
            count += 1
        else:
            count -= 1
        if count == 0:
            element = arr[i]
            count = 1
    return element


def findcount(arr, element):
    count = 0
    for i in arr:
        if i == element:
            count += 1
    if len(arr) // 2 < count:
        return True
    return False


if __name__ == "__main__":
    print("Enter Array : ", end=" ")
    arr = [int(x) for x in input().split()]

    possibleelement = findone(arr)
    if findcount(arr, possibleelement):
        print(possibleelement)
    else:
        print("No majority element.")
