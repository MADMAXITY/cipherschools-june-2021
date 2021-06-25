def merge(a, n, b, m):

    s = []
    count = 0
    i = 0
    j = 0
    while count < n:
        if i == n:
            s.append(b[j])
            j += 1
        elif j == m:
            s.append(a[i])
            i += 1

        else:

            if a[i] < b[j]:
                s.append(a[i])
                i += 1
            else:
                s.append(b[j])
                j += 1
        count += 1

    g = []

    while i < n and j < m:
        if a[i] < b[j]:
            g.append(a[i])
            i += 1
        else:
            g.append(b[j])
            j += 1
    if i == n:
        for y in range(j, m):
            g.append(b[y])
    elif j == m:
        for y in range(i, n):
            g.append(a[y])

    for i in range(n):
        a[i] = s[i]
    for i in range(m):
        b[i] = g[i]
    return