def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    ans = 0
    cur = 1
    for x in a:
        ans += (n - cur) * x
        cur += 1
    print(ans)

if __name__ == "__main__":
    main()