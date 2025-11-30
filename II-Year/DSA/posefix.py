def postfix_evaluation(s):
    s = s.split()
    stack = []

    for token in s:
        if token.isdigit(): # Check if the token is a number
            stack.append(int(token)) # Push the number onto the stack
        else:
            # Pop the two topmost numbers from the stack
            b = stack.pop()
            a = stack.pop()
            # Perform the appropriate operation
        if token == "+":
            stack.append(a + b) 
            
        elif token == "-":
            stack.append(a - b)
            
        elif token == "*":
            stack.append(a * b)
            
        elif token == "/":
            if b != 0: # Avoid division by zero
                stack.append(a / b)
            else:
                raise ValueError("Division by zero is not allowed.")
    return stack.pop() # The final result is the last element in the stack

# Space-separated input for postfix evaluation
s = "10 2 8 * + 3 -"
val = postfix_evaluation(s)
print(val)