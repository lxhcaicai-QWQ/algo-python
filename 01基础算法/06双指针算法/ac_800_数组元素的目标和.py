def main():
    n,m,x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i, j = 0, len(b) - 1
    while i < len(a):
        while j >=0 and a[i] + b[j] > x:
            j -=1
        if j >= 0 and a[i] + b[j] == x:
            print(i, j)
        i += 1

if __name__ == "__main__":
    main()