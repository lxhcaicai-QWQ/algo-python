
def find_k(nums: list[int], ktop: int) -> int:

    def _find_k(l, r, k: int) -> int:
        if l >= r:
            return nums[l]
        mid: int = nums[(l + r) //2]
        i, j = l - 1, r + 1
        while i < j:
            while True:
                i += 1
                if not (nums[i] < mid):
                    break

            while True:
                j -= 1
                if not (nums[j] > mid):
                    break

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        left_length = j - l + 1
        if  left_length >= k:
            return _find_k(l, j, k)
        else:
            return _find_k(j + 1, r, k - left_length)


    return _find_k( 0, len(nums) - 1, ktop)

def main() -> None:
    n,k = map(int, input().split())
    nums = list(map(int, input().split()))
    result = find_k(nums, k)
    print(result)

if __name__ == "__main__":
    main()