class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {} # Holds index of last occurence of char
        left = 0
        longest = 0

        for right in range(len(s)):
            char = s[right] # Get the character
            if char in char_map and char_map[char] >= left: # If encountered, and it's in our window
                left = char_map[char] + 1 #move window one right of the old occurence
            
            char_map[char] = right

            current_length = right - left + 1
            if current_length > longest:
                longest = current_length
        return longest

            



            

if __name__ == "__main__":
    s = Solution()
    str = "dvdf"
    print(s.lengthOfLongestSubstring(str))