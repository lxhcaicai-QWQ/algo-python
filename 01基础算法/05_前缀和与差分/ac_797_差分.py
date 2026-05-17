def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    subs =[0] * (n + 2)
    for i in range(n):
        if i == 0:
            subs[i + 1] = nums[i]
        else:
            subs[i + 1] = nums[i] - nums[i - 1]

    for _ in range(m):
        l, r, c = map(int, input().split())
        subs[l] += c
        subs[r + 1] -= c

    for i in range(n):
        subs[i + 1] += subs[i]
        print(subs[i + 1],end=" ")


if __name__ == "__main__":
    main()