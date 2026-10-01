class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        last = ""
        for i in range(len(s)):
            print(last)
            match s[i]:
                case "(":
                    queue.append(s[i])
                    last = s[i]
                case "{":
                    queue.append(s[i])
                    last = s[i]
                case "[":
                    queue.append(s[i])
                    last = s[i]
                case ")":
                    if last != "(" or len(queue) == 0: return False
                    queue.pop()
                    if len(queue) > 0: last = queue[-1]
                case "}":
                    if last != "{" or len(queue) == 0: return False
                    queue.pop()
                    if len(queue) > 0: last = queue[-1]

                case "]":
                    if last != "[" or len(queue) == 0: return False
                    queue.pop()
                    if len(queue) > 0: last = queue[-1]

            print(queue)
        if len(queue) > 0: return False
        return True