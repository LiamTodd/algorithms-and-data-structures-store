from typing import List


class Solution:
    OPERATORS = ["+", "-", "*", "/"]

    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []
        while len(tokens) > 0:
            top = tokens.pop(0)
            if top in Solution.OPERATORS:
                # do operation
                right = int(operand_stack.pop())
                left = int(operand_stack.pop())
                if top == "+":
                    operand_stack.append(left + right)
                elif top == "-":
                    operand_stack.append(left - right)
                elif top == "*":
                    operand_stack.append(left * right)
                else:
                    operand_stack.append(left / right)
            else:
                # push operand to stack
                operand_stack.append(int(top))

        return int(operand_stack[0])
