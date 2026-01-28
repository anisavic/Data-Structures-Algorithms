class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''CHAT Solution: two pointer technique'''
        if not nums:
            return 0
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
        # entries = {} #dict
        # k = 0
        #
        # i = 0
        # while i < len(nums):
        #     try:
        #         if nums[i] == '_':
        #             break
        #         val = entries[nums[i]]
        #         nums.pop(i)
        #         nums.append('_')
        #     except KeyError:
        #         entries[nums[i]] = True
        #         k += 1
        #         i += 1
        #
        #
        # #print(nums)
        # return k

def main():
    s = Solution()
    #print(s.removeDuplicates([1, 1, 2]))
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

if __name__ == '__main__':
    main()