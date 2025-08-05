class Stack():
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


class Stack():
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
    print(divideBy2(42, 2))



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
        node = self.top
        self.top = node.next
        return node.value

s = Stack()
s.push(3)
s.push('ac')
s.push('er')
s.push(3)
s.push(5)



from __future__ import division
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
        node = self.top
        self.top = node.next
        return node.value

def compute_exec(opt, ov1, ov2):
    def add(ov1, ov2):
        return ov1 + ov2
    def sub(ov1, ov2):
        return ov1 - ov2
    def mul(ov1, ov2):
        return ov1 * ov2
    def div(ov1, ov2):
        return ov1 / ov2

    ops = {'+': add, '-': sub, '*': mul, '/': div}
    for k, v in ops.items():
        if v == opt:
            ret = k(ov1, ov2)
            stack1.push(ret)
            break

def prefix_reverse(string):  # reverse
    tmp = ''
    for s in string[::-1]:
        if s == '(':
            tmp += ')'
        elif s == ')':
            tmp += '('
        else:
            tmp += s
    return tmp

def infix_to_prefix(string):
    opt = ''
    string_tmp = prefix_reverse(string)
    for i in string_tmp:  # 前序表達式
        if i.isdigit():
            stack1.push(i)
        elif i == ')':
            stack1.push(i)
        elif i == '(':
            opt = stack1.pop()
            stack1.pop()
            stack1.push(opt)
        elif i in '+-*/':
            while True:
                if stack1.top is None:
                    break
                s = stack1.pop()
                if s == ')':
                    stack1.push(s)
                    break
                opt = s
                ov2 = stack1.pop()
                ov1 = stack1.pop()
                compute_exec(opt, int(ov1), int(ov2))  # compute result
                continue
            stack1.push(i)

    return stack1.pop()

if __name__ == '__main__':
    stack1 = StackNode()  # 建立堆疊
    infix = ['1+(3+4)*2', '((3+4*2)-1)', '(5*(1+2))']
    for i, v in enumerate(infix):
        print(infix[i], "==>", infix_to_prefix(v))



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
        node = self.top
        self.top = node.next
        return node.value

def compute_exec(op, ov1, ov2):
    def add(ov1, ov2):
        return ov1 + ov2
    def sub(ov1, ov2):
        return ov1 - ov2
    def mul(ov1, ov2):
        return ov1 * ov2
    def div(ov1, ov2):
        return ov1 / ov2

    ops = {'add': add, 'sub': sub, 'mul': mul, 'div': div}
    for k, v in ops.items():
        if v == op:
            ret = v(ov1, ov2)
            stack1.push(ret)
            break

def postfix(expr):
    for s in expr:
        if s.isdigit():
            stack1.push(s)
        elif s == '(':
            stack1.push(s)
        elif s == ')':
            snext = stack1.pop()
            top = stack1.pop()
            stack1.pop()
            stack1.push(f'{" ".join([snext, top, stack1.pop()])}')
        else:
            post_expr = stack1.pop()
            for i in post_expr:
                if i != ' ':
                    stack1.push(i)
            opt = s
            top = stack1.pop()
            snext = stack1.pop()
            compute_exec(opt, int(snext), int(top))
    return stack1.pop()

if __name__ == '__main__':
    stack1 = StackNode()  # 建立堆疊
    exprs = [['1', '+', '(', '3', '+', '4', ')', '*', '2'],
             ['(', '(', '3', '+', '4', '*', '2', ')', '-', '1', ')']]
    for e in exprs:
        print(e, "==>", postfix(e))