def mul(a: str, b: int) -> str:
    a = a[::-1]
    alen = len(a)

    t = 0
    result = []
    for i in range(alen):
        t += int(a[i]) * b
        result.append(t%10)
        t //= 10

    while t != 0:
        result.append(t%10)
        t //= 10

    # 避免乘0的情况
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return ''.join(map(str, result[::-1]))

def main():
    a = str(input())
    num = int(input())
    print(mul(a, num))

if __name__ == "__main__":
    main()