
def combosum2(cand, target):
    def compute(out, combo, cand, target,i):
      if len(cand) == i:
          return
        
      if target == 0:
        if combo not in out:
          out.append(combo)
        return
      else:
          if cand[i] <= target:
            compute(out, combo+[cand[i]], cand, target-cand[i],i+1)
    out = []
    compute(out, [], sorted(cand), target,0)
    return out

print(combosum2([10,1,2,7,6,1,5],8))
