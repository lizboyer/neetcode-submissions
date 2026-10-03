class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        polish = []
        if len(tokens) == 1:
            return(int(tokens[0]))
        while(len(tokens) > 0):
            polish.append(tokens.pop(0))
            if polish[-1].isdigit() == False:
                if polish[-1] == '+':
                    plus = polish.pop()
                    op1 = polish.pop()
                    op2 = polish.pop()
                    polish.append(int(op1) + int(op2))

                elif polish[-1] == '-':
                    plus = polish.pop()
                    op1 = polish.pop()
                    op2 = polish.pop()
                    polish.append(int(op2) - int(op1))

                elif polish[-1] == '*':
                    plus = polish.pop()
                    op1 = polish.pop()
                    op2 = polish.pop()

                    polish.append(int(op1) * int(op2))
                elif polish[-1] == '/':
                    plus = polish.pop()
                    op1 = polish.pop()
                    op2 = polish.pop()
                    polish.append(int(op2) / int(op1))

        return int(polish[0])
