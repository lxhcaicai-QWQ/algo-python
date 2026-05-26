INF = 10**10

def main():
    n,m,q = map(int,input().split())
    dis = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dis[i][i] = 0

    for _ in range(m):
        a,b,c = map(int, input().split())
        dis[a][b] = min(dis[a][b],c)

    for k in range(1,n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dis[i][j] = min(dis[i][j],dis[i][k] + dis[k][j])

    for _ in range(q):
        x, y = map(int, input().split())
        if dis[x][y] >= INF // 2:
            print("impossible")
        else:
            print(dis[x][y])


if __name__ == "__main__":
    main()