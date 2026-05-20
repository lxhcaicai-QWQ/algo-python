def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    mid = (n - 1) // 2 # 坐标从零开始
    ans = 0
    for x in a:
        ans += abs(x - a[mid])
    print(ans)

if __name__ == "__main__":
    main()