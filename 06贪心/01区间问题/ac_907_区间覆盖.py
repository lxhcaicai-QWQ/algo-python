def main():
    st, ed = map(int, input().split())
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    lines.sort(key=lambda x: x[0])

    # 特判：目标区间退化为一个点
    if st == ed:
        for l, r in lines:
            if l <= st <= r:
                print(1)
                return
        print(-1)
        return

    cur = st
    i = 0
    ans = 0

    while cur < ed:
        max_r = cur
        while i < n and lines[i][0] <= cur:
            max_r = max(max_r, lines[i][1])
            i += 1

        if cur == max_r:
            print(-1)
            return

        ans += 1
        cur = max_r

    print(ans)

if __name__ == "__main__":
    main()
