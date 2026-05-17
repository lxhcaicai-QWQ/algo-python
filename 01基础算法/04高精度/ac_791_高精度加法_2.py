
def add(a, b: str) -> str:
    if len(a) < len(b):
        return add(b,a)

    # 反转字符串
    a = a[::-1]
    b = b[::-1]

    alen = len(a)
    blen = len(b)

    t: int = 0
    result = []
    for i in range(alen):
        t += int(a[i])
        if i < blen:
            t += int(b[i])

        result.append(t % 10)
        t //= 10

    while t!=0:
        result.append(t % 10)
        t //= 10

    return ''.join(map(str,result[::-1]))

def main() -> None:
    a = str(input())
    b = str(input())

    print(add(a,b))

if __name__ == "__main__":
    main()