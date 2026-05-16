
def solve(nums: list[int]) -> int:

    def _merge_sort(l, r: int):
        if l == r:
            return 0
        mid: int = (l + r) // 2
        left_count = _merge_sort(l, mid)
        right_count = _merge_sort(mid + 1, r)

        temp = []
        i, j = l, mid + 1
        count: int = 0
        for k in range(l, r + 1):
            if j > r or (i <= mid and nums[i] <= nums[j]):
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                count += mid - i + 1
                j += 1

        idx: int = l
        for item in temp:
            nums[idx] = item
            idx += 1

        return left_count + right_count + count

    return _merge_sort(0, len(nums) - 1)


def main():
    n = map(int, input())
    nums = list(map(int, input().split()))
    print(solve(nums))

if __name__ == "__main__":
    main()