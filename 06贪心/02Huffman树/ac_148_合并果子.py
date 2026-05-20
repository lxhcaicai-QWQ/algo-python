import heapq

def main():
    n = int(input())
    pq = list(map(int, input().split()))

    # 将普通列表原地转化为最小堆
    heapq.heapify(pq)

    ans = 0
    while len(pq) > 1:
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)
        heapq.heappush(pq, a + b)
        ans += a + b
    print(ans)

if __name__ == "__main__":
    main()