def letterCasePermutation(S):
        """
        :type S: str
        :rtype: List[str]
        """
	import pdb
	pdb.set_trace()
        if not S: return [S]
        rest = letterCasePermutation(S[1:])
        if S[0].isalpha():
            return [S[0].lower() + s for s in rest] + [S[0].upper() + s for s in rest]
        return [S[0] + s for s in rest]

letterCasePermutation('a1b2')
