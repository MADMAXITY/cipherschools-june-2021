def minimumPlatform(n, arr, dep):

    arr.sort()
    dep.sort()

    plat_needed = 1
    result = 1
    i = 1
    j = 0

    while i < n and j < n:

        if arr[i] <= dep[j]:

            plat_needed += 1
            i += 1

        elif arr[i] > dep[j]:

            plat_needed -= 1
            j += 1

        if plat_needed > result:
            result = plat_needed

    return result


if __name__ == "__main__":
    arr = [9.00, 9.40, 9, 50, 11.00, 15.00, 18.00]
    dep = [9.10, 12.00, 11, 20, 11.30, 19.00, 20.00]
    n = len(arr)
    print(minimumPlatform(n, arr, dep))
