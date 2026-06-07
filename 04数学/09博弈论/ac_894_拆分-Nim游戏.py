def main():

    N = 1010
    f = [-1] * N
    def _sg(x: int) -> int:
        if f[x] != -1:
            return f[x]
        st = set()
        for i in range(x):
            for j in range(0, i + 1):
                st.add(_sg(i) ^ _sg(j))
        i = 0
        while True:
            if i not in st:
                f[x] = i
                return f[x]
            i += 1

    n = int(input())
    h = list(map(int, input().split()))

    ans = 0
    for x in h:
        ans ^= _sg(x)

    if ans != 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()