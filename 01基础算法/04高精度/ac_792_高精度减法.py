
def compare(a, b:str) -> bool:
    if len(a) != len(b):
        return len(a) > len(b)

    for i in range(len(a)):
        if a[i] != b[i]:
            return a[i] > b[i]
    return True

def sub(a,b:str) -> str:
    a = a[::-1]
    b = b[::-1]
    alen = len(a)
    blen = len(b)

    result = []
    t = 0
    for i in range(alen):
        t = int(a[i]) - t
        if i < blen:
            t -= int(b[i])
        result.append((t + 10) % 10)
        if t < 0:
            t = 1
        else:
            t = 0
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return ''.join(map(str, result[::-1]))

def main() -> None:
    a = str(input())
    b = str(input())
    if compare(a,b):
        print(sub(a,b))
    else:
        print(f"-{sub(b,a)}")

if __name__ == "__main__":
    main()