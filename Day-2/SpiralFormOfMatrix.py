def spirallyTraverse(r, c, a):
    top = 0
    right = c - 1
    bottom = r - 1
    left = 0

    while top <= bottom and left <= right:

        for i in range(left, right + 1):
            print(a[top][i], end=" ")
        top += 1

        for i in range(top, bottom + 1):
            print(a[i][right], end=" ")
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                print(a[bottom][i], end=" ")
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(a[i][left], end=" ")
            left += 1


if __name__ == "__main__":
    m, n = 4, 4
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    spirallyTraverse(m, n, a)
