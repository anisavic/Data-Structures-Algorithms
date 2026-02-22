"""
o(n) time and o(m) space - m is num unique chars
given all upercase engl chars, and k value, return longest substr with
repeated chars
XYYX

Sliding window approach: instead of where are the gaps, look at if window is valid
hold freq count of characters
continuously expand sliding window if valid
start with left = 0, right = 0, expand right based on the k and mostfrequent char
num chars to replace = window length - count of most common char
need char_count{} c: count
most_common_char = int
left ptr, right ptr
XYYX, k=2
window xy, valid
window xyy, valid 
window xyyx, valid
return window length
aaababb
a, valid
aa, valid
aaa, 3-3 = 0<=k
aaab, valid
aaaba, valid
aaabab, 6-4=2>k, so not valid, move window up

aababba, 1

for range:
    update frequencies, find most common char, 
    now check if valid window:if yes, expand, if not, shrink
finally, return window siz
ababb, 2
babba, 2
abba

aababba
ababba

aababba 1 2 2 3 2 

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = {}
        left = 0
        max_window = 0
        for right in range(len(s)):
            window_length = (right - left) + 1
            #update frequencies
            current_char = s[right]
            if current_char not in char_freq:
                char_freq[current_char] = 1
            else:
                char_freq[current_char] += 1
            
            #find count of most common char
            highest_count = max(char_freq[key] for key in char_freq.keys())
            
            # number of chars to replace is window size - count of most frequent char in window
            num_to_replace = window_length - highest_count

            if num_to_replace > k: # window not valid, shrink window
                char_freq[s[left]] -= 1
                left += 1
            else: # else valid, update max
                if window_length > max_window:
                    max_window = window_length
            print(f"numreplace {num_to_replace},highcount {highest_count} windowlen{window_length}, max {max_window}")
        return max_window
        

