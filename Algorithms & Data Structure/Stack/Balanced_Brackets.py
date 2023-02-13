# Check for Balanced Brackets in an expression (well-formedness)

exp = '[()]{}{[()()]()}'  # input

startingB = ['(', '{', '[']
# closingB = [')', '}', ']']

stack = []  # initializing a stack and top
top = -1

for b in exp:
    if b in startingB:
        top += 1
        stack.append(b)
    else:  # b in closingB
        top -= 1
        if not stack:  # stack should have at least 1 elem
            rlt = 0
            break
        if b == ')':
            if stack.pop() != '(':
                rlt = 0
                break
        if b == '}':
            if stack.pop() != '{':
                rlt = 0
                break
        if b == ']':
            if stack.pop() != '[':
                rlt = 0
                break

else:
    rlt = 1

if rlt and top == -1:
    print('Balanced')
else:
    print('Not Balanced')
