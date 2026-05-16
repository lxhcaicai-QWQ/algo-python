
def main():
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))


    def _query(item: int) -> tuple[int, int]:
        l, r = 0, len(nums) - 1
        lpos = -1
        while l<=r:
            mid = (l + r) // 2
            if nums[mid] >= k:
                r = mid - 1
                lpos = mid
            else:
                l = mid + 1

        if lpos == -1 or nums[lpos] != item:
            return -1, -1

        l, r = 0, len(nums) - 1
        rpos = -1
        while l<=r:
            mid = (l + r) // 2
            if nums[mid] <= k:
                l = mid + 1
                rpos = mid
            else:
                r = mid - 1

        if rpos == -1 or nums[rpos] != item:
            return -1, -1
        return lpos, rpos

    for _ in range(q):
        k = int(input())
        print(*_query(k))


if __name__ == "__main__":
    main()