n = 5
r = 0
s = 0
p = 0
q = 0
for i in xrange(1,n+1):
    q = q + 1
    for j in xrange(1,n+1):
        s = s + 1
        for k in xrange(1, n+1):
            p = p + 1
            for l in xrange(1, n+1):
                r = r + 1
print q,s,p,r
