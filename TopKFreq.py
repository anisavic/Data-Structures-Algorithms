import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # nums_frequencies = {}
        # # Count up frequencies
        # for num in nums:
        #     if num not in nums_frequencies:
        #         nums_frequencies[num] = 0
        #     nums_frequencies[num] += 1
        
        # list_tuples = []
        # for num in nums_frequencies.keys():
        #     list_tuples.append(tuple((num, nums_frequencies[num])))
        
        # frequencies_sorted = list(sorted(list_tuples, key=lambda x: x[1]))


        # return list(t[0] for t in frequencies_sorted[-k:])
        
        # New solution, use buckets and Counter
        nums_frequencies = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        # index of each bucket holds the values which holds the corresponding freq
        for num, freq in nums_frequencies.items():
            buckets[freq].append(num)
        res = []
        # print k most frequent elements
        for f in range(len(buckets)-1, 0, -1):
            for num in buckets[f]:
                res.append(num)
                if(len(res)) == k:
                    return res[::-1]
        return res[::-1]


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,2,3,3,3]
    k = 2
    print(s.topKFrequent(nums, k))