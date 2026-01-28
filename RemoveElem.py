class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #find k is easy! it workss
        k = 0
        for elem in nums:
            if elem != val:
                k += 1

        #in-place rearrangement
        swapIndex = 0
        for currIndex in range(k):
            if nums[currIndex] != val: #if no need to be swapped, continue
                continue
            else: #else we need to swap
                #iterate to find element we can swap in that isn't val
                swapIndex = currIndex
                while nums[swapIndex] == val:
                    swapIndex += 1
                #swap it!
                nums[currIndex], nums[swapIndex] = nums[swapIndex], nums[currIndex]

        #now fill in the rest with junk!
        for currIndex in range(k, len(nums)):
            nums[currIndex] = '_'
        #print(f"array swapped {nums}")




        #replace leftovers after k with junk: '_'

        return k





def main():
    s = Solution()
    sol = s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    #sol = s.removeElement([, 2, 2, 3], 2)
    print(f'Solution: {sol}')

if __name__ == '__main__':
    main()