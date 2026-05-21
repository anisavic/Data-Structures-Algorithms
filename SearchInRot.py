class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        search for target in a rotated sorted array
        given nums and target, find index of target

        we know how to find the lowest point, which is what we just did, that index will tell us 
        how many times it has been rotated. Then we can use that index and some modular arithmetic 
        to find the target. We can basically offset everything
        456123
        index 0 is 0 + (#times rotated) mod n = 0+3mod6=0+3=3

        so starting with left 0, right len-1, but then we do this offset calculation
        set left, right
        while left <= right
        define mid

        make a virtual space searching, but translate it into physical with the offset
        mid is what should be translated
        """

        # code to find lowest point
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2


        while left < right:
            if nums[mid] > nums[right]: #inflection point must be to right
                left = mid + 1
            else:
                right = mid
            
            mid = (left + right) // 2
        
        # now mid should hold inflection point
        inflection_point = mid

        #basic binary search code, make into virtual addressing, but use modulo and shifting
        # to find real target
        # so left and right are the virtual sorted array, but mid holds the index of the rotated arrayt
        left = 0
        right = len(nums) - 1

        while left <= right:
            virtual_mid = (left + right) // 2
            mid = (virtual_mid + inflection_point) % len(nums)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = virtual_mid + 1
            else:
                right = virtual_mid - 1
        
        return None


if __name__ == "__main__":
    t = Solution()
    test = [5,6,7,8,1,2,3,4]
    print(t.search(test, 3))