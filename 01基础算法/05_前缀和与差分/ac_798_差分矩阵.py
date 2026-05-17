
def main():
    n,m,q = map(int,input().split())

    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    subs =[[0] * (m + 2) for _ in range(n + 2)]

    def _insert(x1,y1,x2,y2,c: int):
        subs[x1][y1] += c
        subs[x1][y2 + 1] -=c
        subs[x2 + 1][y1] -=c
        subs[x2 + 1][y2 + 1] += c

    for i in range(1,n + 1):
        for j in range(1,m + 1):
            _insert(i,j,i,j,matrix[i-1][j-1])

    for _ in range(q):
        x1, y1, x2, y2, c = map(int, input().split())
        _insert(x1,y1,x2,y2,c)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            subs[i][j] += subs[i-1][j] + subs[i][j-1] - subs[i-1][j-1]

    for i in range(1, n + 1):
        print(*subs[i][1:m+1])

if __name__ == "__main__":
    main()