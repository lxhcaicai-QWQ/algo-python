def main():
    n = int(input())
    lines =[list(map(int,input().split())) for _ in range(n)]
    # 对需要降序的列加 - 取反，升序的列保持不变。
    lines.sort(key = lambda x: (x[0], -x[1]))

    ans = 1  # 只要 n > 0，至少有一个区间
    now = lines[0][1]  # 初始化为第一个区间的右边界
    for (l, r) in lines:
        if l <= now:
            now = max(r, now)
        else:
            ans += 1
            now = r

    print(ans)

if __name__ == "__main__":
    main()