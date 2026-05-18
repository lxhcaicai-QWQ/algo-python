class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def query(self) -> int:
        return self.items[-1]

    def pop(self) -> None:
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0

def main():
    n = int(input())
    stack = Stack()
    for i in range(n):
        command = input().split()
        if command[0] == "query":
            print(stack.query())
        elif command[0] == "push":
            stack.push(int(command[1]))
        elif command[0] == "pop":
            stack.pop()
        elif command[0] == "empty":
            print("YES" if stack.is_empty() else "NO")
        else:
            pass

if __name__ == "__main__":
    main()