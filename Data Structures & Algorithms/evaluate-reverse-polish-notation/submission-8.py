class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        polish = []
        print("len", len(tokens))
        if len(tokens) == 1:
            return(int(tokens[0]))
        while(len(tokens) > 0):
            # print(polish)
            polish.append(tokens.pop(0))
            if polish[-1] == '+':
                # print("add")
                plus = polish.pop()
                op1 = polish.pop()
                op2 = polish.pop()
                # print(plus, op1,op2)
                polish.append(int(op1) + int(op2))

            elif polish[-1] == '-':
                # print("subtract")
                plus = polish.pop()
                op1 = polish.pop()
                op2 = polish.pop()
                # print(plus, op1,op2)
                polish.append(int(op2) - int(op1))

            elif polish[-1] == '*':
                # print("multiply")
                plus = polish.pop()
                op1 = polish.pop()
                op2 = polish.pop()
                # print(plus, op1,op2)
                polish.append(int(op1) * int(op2))
            elif polish[-1] == '/':
                # print("divide")
                plus = polish.pop()
                op1 = polish.pop()
                op2 = polish.pop()
                # print(plus, op1,op2)
                polish.append(int(op2) / int(op1))
                #do the thing
        return int(polish[0])

        # length = ((len(tokens) - 1)//2)
        # register = int(tokens.pop(0))
        # for i in range(length):
        #     reg_2 = int(tokens.pop(0))
        #     operator = tokens.pop(0)
        #     print("reg,reg2,op:", register, reg_2, operator)
        #     if operator == "+":
        #         register += reg_2
        #     if operator == "-":
        #         register -= reg_2
        #     if operator == "*":
        #         register *= reg_2
        #     if operator == "/":
        #         register = register // reg_2
        # return register