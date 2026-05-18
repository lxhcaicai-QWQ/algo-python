class Queue:
    def __init__(self, n: int):
        self.items = [0] * n
        self.lpos = 0
        self.rpos = 0

    def push(self, item: int):
        self.items[self.rpos] = item
        self.rpos += 1

    def pop(self):
        self.lpos += 1

    def query(self) -> int:
        return self.items[self.lpos]

    def is_empty(self) -> bool:
        return self.lpos == self.rpos

def main():
    n = int(input())
    que = Queue(n)
    for _ in range(n):
        command = input().split()
        if command[0] == "push":
            que.push(int(command[1]))
        elif command[0] == "pop":
            que.pop()
        elif command[0] == "query":
            print(que.query())
        elif command[0] == "empty":
            print("YES" if que.is_empty() else "NO")
        else:
            pass

if __name__ == "__main__":
    main()