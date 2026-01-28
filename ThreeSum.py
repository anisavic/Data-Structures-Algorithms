class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = set() #Store dict for triplets

        for i, t_one in enumerate(nums, 0):
            for j, t_two in enumerate(nums[i + 1:], i + 1):
                for k, t_three in enumerate(nums[j + 1:], j + 1):
                    if t_one + t_two + t_three == 0:
                        triplet = tuple(sorted([t_one, t_two, t_three]))
                        triplets.add(triplet)
                    
        

        return list(list(elem) for elem in triplets)


if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    sort = sorted(nums)
    print(sort)
    print(s.threeSum(nums))

        