import sys
import numpy as np
import os

if len(sys.argv)!=2:
    print ('Usage: %s <ratio>' % sys.argv[0])
    exit(0)

np.random.seed(1234)
ratio = float(sys.argv[1])
outdir = 'yelp_%s' % (sys.argv[1])

cmd = 'mkdir -p %s' % outdir
print (cmd)
os.system(cmd)
    
d1 = []
with open('yelp/sentiment.train.0', 'r') as f:
    for line in f:
        d1.append(line.strip())

d2 = []
with open('yelp/sentiment.train.1', 'r') as f:
    for line in f:
        d2.append(line.strip())
        
N1 = len(d1)

perm = np.random.permutation(N1)
n = int(N1 * ratio)
idx = set(perm[:n])

N2 = len(d2)

with open('%s/sentiment.train.0' % outdir, 'w') as w:
    for i in range(N1):
        if i in idx: # write text from another style
            w.write(d2[i])
        else:
            w.write(d1[i])

with open('%s/sentiment.train.1' % outdir, 'w') as w:
    for i in range(N2):
        if i in idx: # write text from another style
            w.write(d1[i])
        else:
            w.write(d2[i])
            

# copy dev and test
print ('directly copy dev and test')
cmd = 'cp -p yelp/sentiment.dev* %s' % outdir
os.system(cmd)

cmd = 'cp -p yelp/sentiment.test* %s' % outdir
os.system(cmd)

