import collections
import sys


def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())

    deque = collections.deque()
    a = list(map(int, input().split()))
    for i in range(len(a)):
        while deque and i - deque[0] >= k:
            deque.popleft()
        while deque and a[deque[-1]] >= a[i]:
            deque.pop()
        deque.append(i)
        if i >= k - 1:
            print(a[deque[0]], end=" ")

    print()
    deque.clear()
    for i in range(len(a)):
        while deque and i - deque[0] >= k:
            deque.popleft()
        while deque and a[deque[-1]] <= a[i]:
            deque.pop()
        deque.append(i)
        if i >= k - 1:
            print(a[deque[0]], end=" ")

if __name__ == "__main__":
    main()