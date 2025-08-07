class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class StackNode():
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = node.next
        return node.value

    def peek(self):
        if self.top is None:
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None

# 優先順序表
precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

# 中序 ➜ 前序（不計算，只轉換）
def infix_to_prefix(expression):
    def is_operator(c):
        return c in "+-*/"

    def not_greater(op, top):
        return precedence.get(op, 0) <= precedence.get(top, 0)

    # 反轉並處理括號
    expression = expression[::-1]
    expression = ''.join(['(' if c == ')' else ')' if c == '(' else c for c in expression])

    stack = StackNode()
    result = []
    for c in expression:
        if c.isdigit():
            result.append(c)
        elif c == '(':
            stack.push(c)
        elif c == ')':
            while not stack.is_empty() and stack.peek() != '(':
                result.append(stack.pop())
            stack.pop()  # 移除 '('
        elif is_operator(c):
            while not stack.is_empty() and is_operator(stack.peek()) and not_greater(c, stack.peek()):
                result.append(stack.pop())
            stack.push(c)
    while not stack.is_empty():
        result.append(stack.pop())

    return ''.join(result[::-1])  # 最後再反轉變成前序
# 測試範例
if __name__ == '__main__':
    expressions = ['1+(3+4)*2', '((3+4*2)-1)', '(5*(1+2))']
    for exp in expressions:
        print(f"Infix: {exp}  =>  Prefix: {infix_to_prefix(exp)}")
