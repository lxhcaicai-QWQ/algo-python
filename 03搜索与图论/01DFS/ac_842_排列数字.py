def main():
    n = int(input())
    nums = [0] * n
    vis =[False] * n

    def _dfs(d: int):
        if d == n:
            print(*nums)
        for i in range(n):
            if vis[i]:
                continue
            nums[d] = i + 1
            vis[i] = True
            _dfs(d + 1)
            vis[i] = False

    _dfs(0)
if __name__ == "__main__":
    main()