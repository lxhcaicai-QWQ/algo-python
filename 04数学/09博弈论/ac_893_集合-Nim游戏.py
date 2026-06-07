def main():
    N = 10 ** 4 + 10
    m = int(input())
    s = list(map(int, input().split()))

    n = int(input())
    f = [-1] * N
    def _sg(x: int) -> int:
        if f[x] != -1:
            return f[x]
        st = set()
        for a in s:
            if x >= a:
                st.add(_sg(x - a))
        i = 0
        while True:
            if i not in st:
                f[x] = i
                return f[x]
            i += 1

    ans = 0
    h = list(map(int, input().split()))
    for x in h:
        ans ^= _sg(x)

    if ans != 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()