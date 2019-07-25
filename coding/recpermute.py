def rec_permute(sofar, rest):
	if len(rest) == 0:
		print(sofar)
	else:
		for i in range(len(rest)):
			next = sofar + rest[i]
			rem = rest[:i] + rest[i+1:]
			rec_permute(next, rem)
	

rec_permute('', 'abcdl')
