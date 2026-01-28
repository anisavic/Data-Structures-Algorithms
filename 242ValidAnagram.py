class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #Hash method
        alphabet = {chr(x): 0 for x in range(97, 123)}


        #iterate through s, count up occurences of letters
        for char in s:
            alphabet[char] += 1

        #then go through t, decrementing the count.
        for char in t:
            if alphabet[char] == 0: #If already 0, means char is not used in s, not an anagram!
                return False
            else:
                alphabet[char] -= 1

        #finally, check if all vals in the hash are back to 0! If so, True! Else, false
        for vals in alphabet.values():
            if vals > 0:
                return False

        return True

        print(alphabet)

def main():
    s = Solution()
    print(s.isAnagram('hi', 'ih'))
    print(s.isAnagram('anagram', 'nagaram'))
    print(s.isAnagram('rat', 'car'))


if __name__ == '__main__':
    main()


