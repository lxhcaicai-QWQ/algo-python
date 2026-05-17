
def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i = 0
    for x in b:
        if a[i] == x:
            i += 1
        if i == n:
            break

    print("Yes" if i == n else "No")

if __name__ == "__main__":
    main()