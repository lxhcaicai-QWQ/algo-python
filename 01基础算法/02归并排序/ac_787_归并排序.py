
def mergesort(nums: list[int]):

    def _merge_sort(l, r: int):
        if l == r:
            return
        mid = (l + r) // 2
        _merge_sort(l, mid)
        _merge_sort(mid + 1, r)

        i, j = l, mid + 1
        temp = []
        for k in range(l, r + 1):
            if j > r or (i <= mid and nums[i] <= nums[j]):
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        idx: int = l
        for item in temp:
            nums[idx] = item
            idx += 1

    _merge_sort(0, len(nums) - 1)


def main():
    n = map(int, input())
    nums = list(map(int, input().split()))
    mergesort(nums)
    print(*nums)

if __name__ == "__main__":
    main()