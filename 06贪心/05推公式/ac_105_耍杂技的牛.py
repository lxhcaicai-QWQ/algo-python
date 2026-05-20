def main():
    n = int(input())
    cows = [list(map(int, input().split())) for _ in  range(n)]
    cows.sort(key = lambda x: x[0] + x[1])
    ans = - (10 ** 10)
    res = 0
    for (w,s) in cows:
        ans = max(ans, res - s)
        res += w
    print(ans)

if __name__ == "__main__":
    main()