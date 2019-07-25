def combinationSum3(k, n):    
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    inp = [x for x in range(1,n+1)]
    out = []
    dst = []
    def subset(out, dst, inp, k, n):
        if len(inp) == 0: 
            if len(dst) == k and sum(dst) == n:
              out.append(dst)
            return
        else:
            if sum(dst) <= n:
                subset(out, dst+[inp[0]], inp[1:], k, n)
                subset(out, dst, inp[1:], k, n)
    subset(out, dst, inp, k, n)
    return out
    
print(combinationSum3(3,9))
 
