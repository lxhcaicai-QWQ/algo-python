import heapq

def main():
    n = int(input())
    lines =  [list(map(int, input().split())) for _ in range(n)]
    lines.sort(key = lambda x: x[0])

    pq = [lines[0][1]]
    for (l, r) in lines[1:]:
        if pq[0] < l:
            heapq.heappop(pq)
            heapq.heappush(pq, r)
        else:
            heapq.heappush(pq, r)

    print(len(pq))

if __name__ == "__main__":
    main()