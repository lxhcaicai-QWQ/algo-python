
def main():
    n = int(input())

    def _check(x: int) -> bool:
        if x < 2:
            return False
        i = 2
        while i*i <= x:
            if x % i == 0:
                return False
            i += 1
        return True

    for _ in range(n):
        a = int(input())
        if _check(a):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()