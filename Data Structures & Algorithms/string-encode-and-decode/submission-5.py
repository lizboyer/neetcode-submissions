class Solution:

    def encode(self, strs: List[str]) -> str:
        big_string = ""
        for i in strs:
            len_str = str(len(i))
            i = len_str + "x" + i
            big_string += i
        print("big_string:",big_string)
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
                print("number_list",number_list)
                letter_count = int("".join(number_list)) 
                number_list = [] # clear number list
                print("letter count:", letter_count)
                string_list.append(s[i+1:(i+1+letter_count)])
                print("i before:", i)
                i += letter_count
                print("i after:", i)
                # s.split(string_list[-1])


                char_flag = False
            i += 1
        return string_list