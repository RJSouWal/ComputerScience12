#12/7/22

import sd 

f1 = open("p41a.txt", 'r')
f2 = open("p41b.txt", 'w')

for l in f1:
	f2.write(' '.join(l.split()))

f1.close()
f2.close()

