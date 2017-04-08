import sys
import itertools
from py2neo import *

graph = Graph()

with open('amazon0302.txt') as f:
    for line in itertools.islice(f, 4, None):  # start=5, stop=None
    	for line in f:
    		arr = line.split()
    		if (len(arr) < 2):
    			sys.exit(0)
    		print("length of array len(arr)", len(arr))
    		first_ID = arr[0]
    		second_ID = arr[1]
    		#Creating the nodes
    		print("first element", first_ID)
    		first = Node("Product", id=first_ID)
    		print("second element", second_ID)
    		second = Node("Product", id=second_ID)

    		#graph
    		graph.create(first|second)

    		#create a relationship
    		graph.create(Relationship(first, "WITH", second))



