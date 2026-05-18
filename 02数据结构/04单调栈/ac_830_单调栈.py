def main():
    n = int(input())
    nums = list(map(int, input().split()))

    stack = []
    for x in nums:
        while stack and stack[-1] >= x:
            stack.pop()
        if not stack:
            print(-1, end=" ")
        else:
            print(stack[-1], end=" ")
        stack.append(x)

if __name__ == "__main__":
    main()