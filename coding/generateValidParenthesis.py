def generateValidParenthesis(N):
    left = 0
    right = 0
    result = []
    def gen(out, left, right, result, N):
        if len(out) == 2 * N:
          result.append(out)
          return
        else:
          if left < N:
            gen(out+'(', left+1, right, result, N)
          
          if right < left:
            gen(out+')', left, right+1, result, N)
        
    gen('',left,right,result,N)
    return result
    
output = generateValidParenthesis(4)
print(output)
print(len(output))

#Time complexity follows catalan number series
