import sys
import itertools
from py2neo import *

graph = Graph()
query = """
MATCH (p1:Product)-[:WITH]->(p2:Product)
WHERE p1.id = {name}
RETURN p.name AS name, AVG(drink.calories) AS avg_calories
"""

result = %cypher MATCH (hashtag:Hashtag)-[:TAGS]->(tweet:Tweet)         \
                 WHERE hashtag.name <> 'rstats'                         \
                 RETURN hashtag.name AS hashtag, count(tweet) AS tweets \
                 ORDER BY tweets DESC LIMIT 5

data = graph.run(query, name="Nicole")

for d in data:
    print(d)
