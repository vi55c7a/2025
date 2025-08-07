class Stack():  #三-1
    
        
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

def divideBy2(decNumber, base):
        remstack = Stack()
        while decNumber > 0:
            rem = decNumber % base
            remstack.push(rem)
            decNumber = decNumber // base
        binString = ""
        while not remstack.isEmpty():
            binString = binString + str(remstack.pop())

        return binString
if __name__ == "__main__":
        print("42 的二進位表示為：",divideBy2(42, 2))

