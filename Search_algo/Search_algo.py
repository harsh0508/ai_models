import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import heapq





def UniformCostSearch(graph , start , end):
    
    # store visted here
    visited = []
    priority_queue = []

    visited.append(start)
    print(start)
    for node in graph[start]:
        if(node[0] not in visited):
            heapq.heappush(priority_queue , (node[1],node[0])) # priotity , task
            # handle initial visited here # ***

    while len(priority_queue) != 0:
        newNode = heapq.heappop(priority_queue)
        if(newNode[1] not in visited):
            print(newNode[1])
            visited.append(newNode[1])
        cost = newNode[0]
        for node in graph[newNode[1]]:
            if(node[0] not in visited):
                heapq.heappush(priority_queue , (node[1]+cost , node[0]))
            

    # print(heapq.heappop(priority_queue))





datafile = pd.read_csv('../Dataset/indian-cities-dataset.csv')
G = nx.Graph()

# create a graph form csv to make digestable for algorithm
networkGraph = {}

for _,row in datafile.iterrows():
    G.add_edge(row["Origin"],row["Destination"],weight =row["Distance"])
    if row["Origin"] in  networkGraph:
        networkGraph[row["Origin"]].append((row["Destination"], row["Distance"]))
    else:
        networkGraph[row["Origin"]] = [(row["Destination"], row["Distance"])]

# setting figure size
plt.figure(figsize=(14,10))

#position nodes
pos = nx.spring_layout(G,k=0.3,seed=42)

# draw nodes
nx.draw_networkx_nodes(G,pos,node_size=500, node_color='skyblue')

# draw edges
nx.draw_networkx_edges(G,pos,width=1.5)

# draw nodes labes
nx.draw_networkx_labels(G,pos,font_size=10,font_color='black',font_weight='bold')

# Draw edge labels (distance in km)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# display
# plt.axis("off")
# plt.tight_layout()
# plt.show(block=False)
# # show plot for 10 sec and then close 
# plt.pause(10)
# plt.close()




# now network graph is ready we can send the data to Uniform cost search

DummyGraph = {
    "A": [("B", 2), ("C", 5), ("D", 1)],
    "B": [("E", 3), ("F", 4)],
    "C": [("F", 2), ("G", 6)],
    "D": [("C", 2), ("G", 7)],
    "E": [("H", 1)],
    "F": [("H", 3)],
    "G": [("H", 2)],
    "H": []
}

UniformCostSearch(DummyGraph, "A" , "F")
