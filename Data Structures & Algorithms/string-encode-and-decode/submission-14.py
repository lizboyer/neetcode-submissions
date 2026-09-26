class Solution:

    def encode(self, strs: List[str]) -> str:
        big_string = ""
        for i in strs:
            len_str = str(len(i))
            i = len_str + "x" + i
            big_string += i
        return big_string # 3xcat5xhorse
    def decode(self, s: str) -> List[str]:
        count = ""
        countdown = 0
        charF = False
        output = []
        for char in s:
            if charF == False and char != "x":
                count += char
            elif charF == False and char == "x":
                output.append("")
                charF = True
                countdown = int(count)
            elif charF and countdown != 0:
                countdown -= 1
                output[-1] += char
            if countdown == 0 and charF:
                count = ""
                charF = False
        return output