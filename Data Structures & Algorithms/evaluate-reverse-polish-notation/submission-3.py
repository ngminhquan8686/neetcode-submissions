class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].lstrip("-").isdigit():
                stack.append(int(tokens[i]))
            elif tokens[i] == "+":
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                stack.append(operand_1 + operand_2)
                
            elif tokens[i] == "-":
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                stack.append(operand_1 - operand_2)
                
            elif tokens[i] == "*":
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                stack.append(operand_1 * operand_2)
            else:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                stack.append(int(operand_1 / operand_2)) 

        return stack.pop()       
        