def main():
    n = int(input())
    nums = list(map(int, input().split()))

    que = []

    for x in nums:
        if len(que) == 0 or que[-1] < x:
            que.append(x)

        l, r = 0, len(que) - 1
        pos = 0
        while l <= r:
            mid = (l + r) // 2
            if que[mid] >= x:
                r = mid - 1
                pos = mid
            else:
                l = mid + 1
        que[pos] = x

    print(len(que))

if __name__ == "__main__":
    main()