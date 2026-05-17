
def div(a: str, num: int) -> tuple[str, int]:
    t = 0
    result = []
    for i in range(len(a)):
        t = t * 10 + int(a[i])
        result.append(t // num)
        t %= num

    result = result[::-1]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return ''.join(map(str, result[::-1])), t

def main():
    a = str(input())
    num = int(input())
    result, remainer = div(a, num)
    print(result)
    print(remainer)

if __name__ == "__main__":
    main()