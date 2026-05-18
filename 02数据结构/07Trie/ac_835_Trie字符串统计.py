N = 100005
tot = 0

def main():
    n = int(input())

    trie = [[0] * 26]
    cnt = [0]

    def _insert(ss: str):
        global tot
        p = 0
        for c in ss:
            ch: int = ord(c) - ord('a')
            if trie[p][ch] == 0:
                trie.append([0] * 26)
                cnt.append(0)
                tot += 1
                trie[p][ch] = tot
            p = trie[p][ch]

        cnt[p] += 1

    def _query(ss: str) -> int:
        p = 0
        for c in ss:
            ch: int = ord(c) - ord('a')
            p = trie[p][ch]
            if p == 0:
                return 0
        return cnt[p]

    for _ in range(n):
        command, ss = input().split()
        if command == "Q":
            print(_query(ss))
        elif command == "I":
            _insert(ss)

if __name__ == "__main__":
    main()