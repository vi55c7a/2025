class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackNode:
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
        self.top = self.top.next
        return node.value

    def peek(self):
        if self.top is None:
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None
# 優先順序
precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
# 轉換中序為後序
def infix_to_postfix(expression):
    output = []
    stack = StackNode()
    for token in expression:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # 丟棄 '('
        elif token in precedence:
            while not stack.is_empty() and stack.peek() in precedence and precedence[token] <= precedence[stack.peek()]:
                output.append(stack.pop())
            stack.push(token)
    while not stack.is_empty():
        output.append(stack.pop())
    return output


# 計算後序表示式
def evaluate_postfix(postfix_expr):
    stack = StackNode()

    for token in postfix_expr:
        if token.isdigit():
            stack.push(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)

    return stack.pop()


# 主程式
if __name__ == '__main__':
    expressions = [
        ['1', '+', '(', '3', '+', '4', ')', '*', '2'],
        ['(', '(', '3', '+', '4', '*', '2', ')', '-', '1', ')'],
        ['(', '5', '*', '(', '1', '+', '2', ')', ')']
    ]

    for exp in expressions:
        postfix = infix_to_postfix(exp)
        result = evaluate_postfix(postfix)
        print(f"Infix: {''.join(exp)}")
        print(f"Postfix: {' '.join(postfix)}")
        print(f"Result: {result}")
        print('---')
