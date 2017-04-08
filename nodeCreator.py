# f = open("amazon0302.txt",'r')
# with open('amazon0302.txt','r') as f:
# 	for _ in xrange(17):
#     	next(f)

#     for line in f:
#         for word in line.split():
#            print(word)      

import sys
import itertools
with open('amazon0302.txt') as f:
    for line in itertools.islice(f, 4, None):  # start=5, stop=None
    	for line in f:
    		arr = line.split()
    		if (len(arr) < 2):
    			sys.exit(0)
    		print("length of array len(arr)", len(arr))
    		print("first element", arr[0])
