class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        output = []
        # hashmap = {ord: [list,of,words], ord: [list,of,words]}
        for word in strs:
            sum = ''.join(sorted(word))
            print(sum)
            # for char in word:
            #     sum = sum ^ ord(char)
            if hashmap.get(sum) != None: #if hash(sum) in hashmap:
                # double check for same ordinal
                hashmap.get(sum).append(word)
            else:
                hashmap[sum] = [word]
        output = list(hashmap.values())
        return output