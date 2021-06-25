def search(num, col, row, mat):
    if col >= len(mat[0]) or row >= len(mat):
        return None
    if col < 0 or row < 0:
        return None
    if num == mat[row][col]:
        return [row, col]
    if num > mat[row][col]:
        return search(num, col, row + 1, mat)
    if num < mat[row][col]:
        return search(num, col - 1, row, mat)


if __name__ == "__main__":
    row, col = 4, 4  # map(int, input("Enter Dimensions : ").split())
    # mat = []
    # for i in range(row):
    #     print("Enter row : ")
    #     row = [int(x) for x in input().split()]
    #     mat.append(row)
    mat = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50],
    ]

    num = int(input("Enter number to be searched : "))
    f = search(num, col - 1, 0, mat)
    if f == None:
        print("Not found!")
    else:
        print(f"Found at {f[0]},{f[1]}")
