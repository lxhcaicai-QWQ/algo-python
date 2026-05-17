def main():
    n = int(input())

    def _calculate(num: int) -> int:
        count = 0
        while num > 0:
            num -= num&-num
            count += 1
        return count

    for x in list(map(int, input().split())):
        print(_calculate(x), end=" ")

if __name__ == "__main__":
    main()