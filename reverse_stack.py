stack = [0, 1, 2, 3]

def insert(stack, element, depth=-1):
    if depth == 0 or not stack:
        stack.append(element)
        return depth
    current = stack.pop()
    depth = insert(stack, element, depth-1)
    stack.append(current)
    return depth

def reverse(stack):
    n = insert(stack, stack.pop(), depth=-1)
    n = abs(n) - 1
    for depth in range(n-1, -1, -1):
        insert(stack, stack.pop(), depth)
    return stack

def _reverse(stack):
    if not stack: return
    tmp = stack.pop()
    _reverse(stack)
    insert(stack, tmp)
    return stack
print(stack)
print(_reverse(stack))