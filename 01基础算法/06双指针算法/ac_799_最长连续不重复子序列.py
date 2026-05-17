from collections import deque


def main():
    n = int(input())

    ans = 1
    keyset = set()
    que = deque()
    for x in list(map(int, input().split())):
        while x in keyset:
            item = que.popleft()
            keyset.remove(item)

        que.append(x)
        keyset.add(x)
        ans = max(ans, len(que))

    print(ans)

if __name__ == "__main__":
    main()