N = 10 ** 5 + 1
INF = 10**10
def main():

    hsh = [INF] * N
    def _find(x: int) -> int:
        t = (x + N) % N
        while hsh[t] != INF and hsh[t] != x:
            t += 1
            if t == N:
                t = 0
        return t

    n = int(input())
    for _ in range(n):
        command = input().split()
        if command[0] == "I":
            x = int(command[1])
            hsh[_find(x)] = x
        elif command[0] == "Q":
            x = int(command[1])
            print("No" if hsh[_find(x)] == INF else "Yes")

if __name__ == "__main__":
    main()