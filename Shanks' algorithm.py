def shanks_no_sort(n, g, h):
    m = int(pow(n, 0.5)) + 1
    l1 = []
    for i in range(m+1):
        l1.append(pow(g, i*m, n))
    for j in range(m+1):
        temp = pow(g, -1*j, n) * h % n
        try:
            x = l1.index(temp) * m + j
            print('[+] Find DLP solution:', x)
            return x
        except:
            continue

def shanks_sort(n, g, h):
    order = n - 1
    m = int(pow(order, 0.5)) + 1
    l1 = []
    l2 = []
    for i in range(m+1):
        l1.append((i, pow(g, i*m, n)))
        l2.append((i, pow(g, -1*i, n) * h % n))
    l1.sort(key = lambda pair:pair[1])
    l2.sort(key = lambda pair:pair[1])
    i, j = 0, 0
    while(i < len(l1) and j < len(l2)):
        if l1[i][1] == l2[j][1]:
            x = l1[i][0] * m + l2[j][0]
            print('[+] Find DLP solution:', x)
            return x
        elif l1[i][1] > l2[j][1]:
            j += 1
        else:
            i += 1

n = 24691
g = 106
h = 12375
shanks_no_sort(n, g, h)
shanks_sort(n, g, h)