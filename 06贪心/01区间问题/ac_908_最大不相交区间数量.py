def main():
    n = int(input())
    lines =  [list(map(int, input().split())) for _ in range(n)]
    lines.sort(key = lambda x: x[1])

    ans = 1
    cur = lines[0][1]
    for (l,r) in lines[1:]:
        if l > cur:
            ans += 1
            cur = r

    print(ans)

if __name__ == "__main__":
    main()