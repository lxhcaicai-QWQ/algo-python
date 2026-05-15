
def quick_sort(nums: list[int]):

    def _quick_sort(items: list[int], l, r:int):
        mid: int = items[(l+r)//2]
        i, j = l, r
        while i < j:
            while items[i] < mid:
                i += 1
            while items[j] > mid:
                j -= 1
            if i <= j:
                items[i], items[j] = items[j], items[i]
                i += 1
                j -= 1

        if i < r:
            _quick_sort(items, i, r)
        if j > l:
            _quick_sort(items, l, j)

    _quick_sort(nums, 0, len(nums) - 1)

def main() -> None:
    n = int(input())
    nums = list(map(int, input().split()))
    quick_sort(nums)
    print(*nums)

if __name__ == "__main__":
    main()