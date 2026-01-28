class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {} #Initially empty\

        # for str in strs:
        #     sorted_s = "".join(sorted(str))
        #     if sorted_s not in anagram_map:
        #         anagram_map[sorted_s] = []
        #     anagram_map[sorted_s].append(str)
        # return list(anagram_map.values())

        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord('a')] += 1
            
            if tuple(count) not in anagram_map:
                anagram_map[tuple(count)] = []
            
            anagram_map[tuple(count)].append(str)
        return list(anagram_map.values())


        

    
if __name__ == "__main__":
    s = Solution()
    strs = ["act","pots","tops","cat","stop","hat"]
    print(s.groupAnagrams(strs))