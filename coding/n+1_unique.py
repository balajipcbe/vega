class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A)//2
        
        if N == 1:
            return None
        
        item_count = {}
        for item in A:
            if item_count.get(item):
                item_count[item] += 1
            else:
                item_count[item] = 1

                                
        for key,value in item_count.items():
            if value == N:
                return key
