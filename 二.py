class Stack():            #二
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    def clear(self):
        del self.items[:]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def top(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
if __name__ == "__main__":
    print("程式開始執行")

    s = Stack()
    print("堆疊是否為空？", s.isEmpty())  # True

    s.push(10)
    s.push(20)
    s.push(30)

    print("目前堆疊數量：", s.size())  # 3
    print("堆疊頂端元素：", s.top())   # 30

    print("彈出頂端元素：", s.pop())   # 30
    print("彈出後的堆疊頂元素：", s.top())  # 20

    s.clear()
    print("清空後堆疊是否為空？", s.isEmpty())  # True


    