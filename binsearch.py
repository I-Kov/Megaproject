def bin_search:
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    del l2[0]
    for j in l2:
        l = 1
        r = l1[0]
        while l < r:
            mid = (l + r) // 2
            if l1[mid] == j:
                l = mid
                r = mid
            elif l1[mid] > j:
                r = mid - 1
            else:
                l = mid + 1
        if l1[l] == j:
            print(l, end=' ')
        else:
            print(-1, end=' ')
