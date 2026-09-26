class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        if (s==t):
            return True # anagram
        for i in range(len(s)):
            # print("s,t:",s,t)
            if s[0] in t: 
                t = t.replace(s[0],'',1)
                s = s.replace(s[0],'',1)
        if len(s) != 0:
            return False

        return True