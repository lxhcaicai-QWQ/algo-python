tot = 0
def main():

    trie = [[0] * 32]

    def _insert(x: int) -> None:
        global tot
        p = 0
        for i in range(31, -1, -1):
            j = x >> i & 1
            if trie[p][j] == 0:
                trie.append([0] * 32)
                tot += 1
                trie[p][j] = tot
            p = trie[p][j]

    def _query(x: int) -> int:
        res = 0
        p = 0
        for i in range(31, -1, -1):
            j = x >> i & 1
            if trie[p][j ^ 1] != 0:
                res |= 1 << i
                p = trie[p][j ^ 1]
            else:
                p = trie[p][j]

        return res

    n = int(input())
    ans = 0
    for x in list(map(int, input().split())):
        _insert(x)
        ans = max(ans, _query(x))

    print(ans)

if __name__ == "__main__":
    main()