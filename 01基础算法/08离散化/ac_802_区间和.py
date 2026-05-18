def main():
    n,m = map(int, input().split())

    adds = [list(map(int, input().split())) for _ in range(n)]
    query = [list(map(int, input().split())) for _ in range(m)]

    mergelist = [i[0] for i in adds]
    mergelist.extend(item for row in query for item in row)

    uniquelist = sorted(list(set(mergelist)))

    def _find(x: int) -> int:
        pos = -1
        l, r = 0, len(uniquelist)-1
        while l <= r:
            mid = (l + r) // 2
            if (uniquelist[mid] >= x):
                r = mid - 1
                pos = mid
            else:
                l = mid + 1
        # 映射 1 ~ n
        return pos + 1

    # 前面一位为0
    sums = [0] * (len(uniquelist) + 1)
    for (a,b) in adds:
        x = _find(a)
        sums[x] += b

    for i in range(1, len(sums)):
        sums[i] += sums[i-1]

    for (a, b) in query:
        l = _find(a)
        r = _find(b)
        print(sums[r] - sums[l - 1])

if __name__ == "__main__":
    main()