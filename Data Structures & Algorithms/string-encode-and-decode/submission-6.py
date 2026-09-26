class Solution:

    def encode(self, strs: List[str]) -> str:
        big_string = ""
        for i in strs:
            len_str = str(len(i))
            i = len_str + "x" + i
            big_string += i
        return big_string # 3xcat5xhorse
    def decode(self, s: str) -> List[str]:
        string_list = []
        number_list = []
        char_flag = False
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                number_list.append(char)
                char_flag = True
            if char_flag == True and char == 'x':
                letter_count = int("".join(number_list)) 
                number_list = [] # clear number list
                string_list.append(s[i+1:(i+1+letter_count)])
                i += letter_count
                char_flag = False
            i += 1
        return string_list