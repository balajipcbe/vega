class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = [ x for x in range(1, N+1) ]
        return self.count_helper(nums, 0, 0)
    
    def count_helper(self, nums, cur_index=0, count=0):
        if cur_index == len(nums):
            count += 1
        else:
            for i in range(cur_index, len(nums)):
                nums[cur_index], nums[i] = nums[i], nums[cur_index]
                if (nums[cur_index] % (cur_index+1) == 0) or ((cur_index+1) % nums[cur_index] == 0):
                    count = self.count_helper(nums, cur_index+1, count)
                nums[cur_index], nums[i] = nums[i], nums[cur_index]
        return count
    

s = Solution()
print(s.countArrangement(15))   
