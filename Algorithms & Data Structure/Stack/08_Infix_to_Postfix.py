'''
the order of operators may change, 
but the order of operands occur will not change 
(operands: from left to right)

1. <operand> or <operator>
    operand -> simply put it in the postfix expression
    operator: can be put when all the operands came out (both left and right)
            -> keep it in a seperate list or colletion for later use
    
    If there's anythin on the stack, compare the precedence b/w the operators
    -> if later one has higher precedence, push it in the stack
    -> else(lower or same precedence), the top of the stack should be popped off and go to the expression

    how to find the end of right operand for an operator
    A. getting an operator of lesser precedence
    B. if we reach the end of the expression -> pop all elements from the stack
'''

'''
<pseudocode>
def InfixToPostfix(exp)
1. create a stack
2. create an empty string (rlt) to store the result
3. for i <- 0 to length(exp)-1: looking at each chars to see whether it's an operand or operator
4. if exp[i] is operand
    rlt += exp[i]
5. else
    compare the priority
        while stack & stack[top] has higher precedence
            && not isopeningparentheses(stack.top())
            rlt += stack.pop(top)
        push exp[i]

        elif exp[i] == '('
            push exp[i]
        elif exp[i] == ')'
            while stack && not isopeningparentheses(stack.top())
                rlt += stack.pop(top)
            stack.pop()  # pop '(' cuz it's done
6. after for loop, if there's any left on the stack
    while stack:
        rlt += stack.pop(top)
7. return rlt
'''
'''
Need of Postfix Notations:
 - can be evaluate faster that the infix notation
 - easier to parse for a machine (infix for humans)
 - no issue of operator precedence and left-right associativity
 - fewer overheads of parenthesis than prefix (less time for parsing)
'''


operators = set(['+', '-', '*', '/', '(', ')', '^'])
precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
# higher precedence == should be evaluated first

def infixToPostfix(expression):
    stack = []
    rlt = ''

    for character in expression:
        if character not in operators:
            rlt += character
        elif character == '(':
            stack.append(character)
        elif character == ')':
            while stack and stack[-1] != '(':
                rlt += stack.pop()
            stack.pop()  # deleting the opening parentheses
        else:
            while stack and stack[-1] != '(' and precedence[character] <= precedence[stack[-1]]:
                rlt += stack.pop()
            stack.append(character)

    while stack:
        rlt += stack.pop()

    return rlt

expression = input('Enter infix expression: ')

print('infix notation:', expression)
print('postfix notation:', infixToPostfix(expression))