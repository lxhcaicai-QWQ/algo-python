def main():
    n,m,q = map(int, input().split())
    martix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        martix.append(row)

    prefix = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            prefix[i + 1][j + 1] = prefix[i + 1][j] + prefix[i][j+1] - prefix[i][j] + martix[i][j]

    def _query(x1,y1,x2,y2: int) -> int:
        return prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1]

    for _ in range(q):
        x1,y1,x2,y2 = map(int, input().split())
        print(_query(x1,y1,x2,y2))

if __name__ == "__main__":
    main()