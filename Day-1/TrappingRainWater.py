def trap(height):
    if len(height) == 0:
        return 0
    leftmax = [height[0]]
    for i in height[1::]:
        leftmax.append(max([leftmax[-1], i]))

    tot_water = 0
    rmax = 0
    for i in range(len(height) - 1, -1, -1):
        rmax = max(rmax, height[i])
        tot_water += min(rmax, leftmax[i]) - height[i]
    return tot_water


if __name__ == "__main__":
    arr = [int(x) for x in input("Enter heights : ").split()]
    print(trap[arr])
