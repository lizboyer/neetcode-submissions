class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = []
        max_chars = 0
        for i in range(len(s)):
            if s[i] in chars and len(chars) > 0: # repeated char
                max_chars = max(max_chars, len(chars)) # is the previous larger than our dict to this point?
                chars = chars[chars.index(s[i])+1:]
            chars.append(s[i]) # push the value to queue
            if i == len(s) - 1: max_chars = max(max_chars, len(chars))
        return(max_chars)