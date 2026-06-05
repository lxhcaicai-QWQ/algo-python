def main():
    n,m = map(int, input().split())

    p = list(map(int, input().split()))

    ans = 0
    for i in range(1, 1<<m):
        res = 1
        count = 0
        check = True
        for j in range(m):
            if i >> j & 1 == 1:
                if res * p[j] > n:
                    check = False
                    break
                res *= p[j]
                count += 1

        if check:
            if count % 2 == 1:
                ans += n // res
            else:
                ans -= n // res
    print(ans)

if __name__ == "__main__":
    main()