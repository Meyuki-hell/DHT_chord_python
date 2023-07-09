from dht import *
from random import randint

d = DHT(10)

# Add nodes
for i in range(90):
    r = randint(0, 10240)
    d.join(Node(r))

d.updateAllFingerTables();

# Adding sample data to nodes
for i in range(5, 1024, 10):
    data = "Node " + str(i) + " says hello"
    d.store(d._startNode, i, data)
    print("Adding data (" + data + ") to node: ",  str(i))


# Checking lookups for a given node
id = int(input("Enter node key for lookups: "))
print("Data in node: ", d.lookup(d._startNode, int(id)))
