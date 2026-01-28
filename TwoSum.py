class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # O(n^2) sol
        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if i == j:
        #             continue
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        differences = {} # Difference = target - nums[i]
        for i in range(len(nums)):
            if differences.get(nums[i]) is None: # haven't yet found index pair, but store difference for future
                diff = target - nums[i]
                differences[diff] = i
            else:
                j = differences.get(nums[i])
                result = [i, j] if j > i else [j, i]
                return result



       
    
if __name__ == "__main__":
    s = Solution()
    nums=[2,5,5,11]
    target=10
    print(s.twoSum(nums, target))