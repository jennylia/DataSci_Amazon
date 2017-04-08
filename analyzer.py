import sys
import itertools
from py2neo import *
import cypher

graph = Graph()
query = """
MATCH r = (p1:Product)-[:WITH]->(p2:Product)
WHERE p1.id = '1'
RETURN count(r)
"""


results = cypher.run(query)


# df = results.get_dataframe()
# df.head()

for d in results:
    print(d)
