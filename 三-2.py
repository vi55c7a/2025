class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None  # 堆疊為空
        node = self.top
        self.top = node.next
        return node.value

    def print_stack(self):
        # 額外函數：印出整個堆疊內容（從 top 開始）
        current = self.top
        print("Stack (top -> bottom): ", end="")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# 建立堆疊並推入資料
s = Stack()
s.push(3)
s.push('ac')
s.push('er')
s.push(3)
s.push(5)

# 印出堆疊內容
s.print_stack()

# 執行幾次 pop 並印出結果
print("\nPop values:")
print(s.pop())  # 預期為 5
print(s.pop())  # 預期為 3

# 再印出堆疊內容
print("\nAfter popping 2 elements:")
s.print_stack()
