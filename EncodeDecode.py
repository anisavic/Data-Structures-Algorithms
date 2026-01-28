class Solution:

    def encode(self, strs: list[str]) -> str:
        # if not strs:
        #     return '~'.join(strs) + "`"
        # else:
        #     return '~'.join(strs)
        # Better solution is using encoding such as (lenof word)|#|(word)...
        # encoded_str = ""
        # for s in strs:
        #     encoded_str += str(len(s)) + '#' + s
        # return encoded_str # Good but you can do this instead!
        return "".join(f"{len(s)}#{s}" for s in strs)
        


    def decode(self, s: str) -> list[str]:
        # if s.endswith("`"):
        #     return []
        # else:
        #     return s.split('~')
        # Better solution is to 

        # curr_index = 0
        # len_of_str = len(s)
        # decoded = []
        # while curr_index != len_of_str:
        #     length_index = curr_index
        #     while s[length_index] != '#':
        #         length_index += 1
        #     length_word = int(s[curr_index:length_index])
        #     word = s[length_index+1:length_index+length_word+1]
        #     decoded.append(word)
        #     curr_index = length_index + length_word + 1
        # return decoded
        i = 0
        decoded = []
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]

            decoded.append(word)

            i = j + 1 + length
        return decoded

        
if __name__ == "__main__":
    s = Solution()
    # strs = ["we","say",":","yes","!@#$%^&*()"]
    # encoded = s.encode(strs)
    # print(encoded)
    # print(s.decode(encoded))