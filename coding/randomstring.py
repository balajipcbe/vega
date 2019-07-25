import string
import random

s = ''
print(len(string.ascii_lowercase)

for i in range(501):
	j = random.randint(0,26)
	s += string.ascii_lowercase[j]

print(s)
