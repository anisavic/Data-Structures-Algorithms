class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # seqs = {}
        # # seqs[nums[0]] = 1
        # for num in nums:
        #     if seqs.get(num) is None and seqs.get(num+1) is None:
        #         seqs[num + 1] = 1
        #     else:
        #         seq_len = seqs.get(num+1, 0)
        #         if (seqs.get(num, 0) + 1 > seq_len):
        #             seqs[num + 1] = seqs[num] + 1 
        #         seqs.pop(num, None)
        
        # # Now iterate thru all sequences to combine and find max
        # seq_arr = list(seqs.keys())
        # max_seq = 0
        # if seq_arr:
        #     max_seq = seq_arr[len(seq_arr)-1]
        # # Backward pass
        # for i in range(len(seq_arr)-1, -1, -1):
        #     seq = seq_arr[i]
        #     # Update max first
        #     if seqs[seq] >= seqs[max_seq]:
        #         s = seq
        #         seq = max_seq
        #         max_seq = s
    
        #     if seq > max_seq and seq - seqs[seq] in range(seq-seqs[seq],max_seq + 1):
        #         overlap = len(range(seq-seqs[seq],max_seq))
        #         seqs[seq] = seqs[seq] + seqs[max_seq] - overlap
        #         seqs.pop(max_seq)
        #         max_seq = seq
        #     elif seq < max_seq and max_seq - seqs[max_seq] in range(max_seq-seqs[max_seq],seq + 1):
        #         overlap = len(range(max_seq-seqs[max_seq],seq))
        #         seqs[max_seq] = seqs[seq] + seqs[max_seq]
        #         seqs.pop(seq)
            
        # # Forward pass
        # seq_arr = list(seqs.keys())
        # max_seq = 0
        # if seq_arr:
        #     max_seq = seq_arr[0]
        # for i in range(len(seq_arr)):
        #     seq = seq_arr[i]
        #     # Update max first
        #     if seqs[seq] >= seqs[max_seq]:
        #         s = seq
        #         seq = max_seq
        #         max_seq = s
    
        #     # if seq > max_seq and seq - seqs[seq] in range(seq-seqs[seq]:seq):
        #     #     seqs[seq] = seqs[seq] + seqs[max_seq]
        #     #     seqs.pop(max_seq)
        #     #     max_seq = seq
        #     # elif seq < max_seq and max_seq - seqs[max_seq] == seq:
        #     #     seqs[max_seq] = seqs[seq] + seqs[max_seq]
        #     #     seqs.pop(seq)
        #     if seq > max_seq and seq - seqs[seq] in range(seq-seqs[seq],max_seq + 1):
        #         overlap = len(range(seq-seqs[seq],max_seq))
        #         seqs[seq] = seqs[seq] + seqs[max_seq] - overlap
        #         seqs.pop(max_seq)
        #         max_seq = seq
        #     elif seq < max_seq and max_seq - seqs[max_seq] in range(max_seq-seqs[max_seq],seq + 1):
        #         overlap = len(range(max_seq-seqs[max_seq],seq))
        #         seqs[max_seq] = seqs[seq] + seqs[max_seq]
        #         seqs.pop(seq)
        # Incorrect approach, could have been correct if I went with storing ranges and combined as I went through, but there is an easier way:
        # And that is to iterate through and only count from the beginning of a sequence plus using sets
            
        max_len = 0 # Longest sequence encountered
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 in nums_set:
                continue # Only interested in counting from the start of a sequence
            else:
                curr = num # Count up the subsequence starting from num till the end and record length
                curr_len = 1
                while curr + 1 in nums_set: # O(1) lookup
                    curr_len += 1
                    curr += 1
                if curr_len > max_len:
                    max_len = curr_len
        return max_len


if __name__ == "__main__":
    s = Solution()
    nums = [2,20,4,10,3,4,5]
    print(s.longestConsecutive(nums))