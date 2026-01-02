def create_stack():
    stack = []
    return stack

def check_empty(stack):
    if (len(stack) == 0):
        print("stack is empty")
    else:
        print("no, stack is not empty")

def is_empty(Stack):
    return (len(stack)==0)

def push(stack, item):
    stack.append(item)
    return print(f"Item appended to stack: {item}")

def pop(stack):
    if (is_empty(stack)):
        print("stack is empty")
        return None

    removed = stack.pop()
    print(f"popped item is : {removed}")
    return removed

stack = create_stack()
push(stack, 3)
push(stack, 5)
pop(stack)
check_empty(stack)
pop(stack)
check_empty(stack)
pop(stack)