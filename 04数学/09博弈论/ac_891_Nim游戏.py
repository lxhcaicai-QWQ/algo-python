def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for x in a:
        ans ^= x

    if ans == 0:
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    main()