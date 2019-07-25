from operator import itemgetter

m = [('12:01','12:30'),('1:12','2:12')]
m = [('12:37','12:59'),('12:23','12:35')]


for st,et in m:
    print(st+'->'+et)

def timecmp(t):
    s,e = t[0],t[1]
    h,m = s.split(':')
    return h,m

sm = sorted(m,key=timecmp)
print('*'*20)
for st,et in sm:
    print(st+'->'+et)
