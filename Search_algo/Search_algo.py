from collections import deque
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import time





def UniformCostSearch(graph , start , end):
    
    start_time = time.perf_counter()
    #handle edge case
    if(start == end):
        print([start],0)
        return
    
    # store visted here
    visited = []
    priority_queue = []

    visited.append(start)
    for node in graph[start]:
        if(node[0] not in visited):
            heapq.heappush(priority_queue , (node[1],node[0],[start,node[0]])) # priotity , task

    while len(priority_queue) != 0:
        newNode = heapq.heappop(priority_queue)
        if(newNode[1] not in visited):
            # if last node is visited exit !
            visited.append(newNode[1])
            if(newNode[2][len(newNode[2])-1] == end):
                print(visited)
                print("elapsed time is ", time.perf_counter()-start_time," seconds")
                print(newNode[2],newNode[0])
                return
        cost = newNode[0]
        for node in graph[newNode[1]]:
            if(node[0] not in visited):
                heapq.heappush(priority_queue , (node[1]+cost , node[0], newNode[2] + [node[0]]))
            

def AStar(graph,hurestic,start,end):
    start_time = time.perf_counter()
    visited = []
    priorityQueue = []

    visited.append(start)
    for node in graph[start]:
        heapq.heappush(priorityQueue,(node[1]+hurestic[node[0]] , node[0] , [start,node[0]]))
    

    while len(priorityQueue) != 0:
        newNode = heapq.heappop(priorityQueue)
        if(newNode[1] not in visited):
            # if last node is visited exit !
            visited.append(newNode[1])
            if(newNode[2][len(newNode[2])-1] == end):
                print(visited)
                print("elapsed time is ", time.perf_counter()-start_time," seconds")
                print(newNode[2],newNode[0])
                return
        cost = newNode[0]
        for node in graph[newNode[1]]:
            if(node[0] not in visited):
                heapq.heappush(priorityQueue , (node[1]+cost+hurestic[node[0]] , node[0], newNode[2] + [node[0]]))
    return


def dfs(graph,start,end):
    visited = set()
    queue = deque()
    path = []
    queue.appendleft(start)

    while queue:
        ele = queue.pop()
        if ele not in visited:
            visited.add(ele)
            path.append(ele)
            
        nodes = graph[ele]
        for node in nodes:
            if node[0] not in visited:
                if node[0] == end:
                    print('reached end')
                    visited.add(node[0])
                    print(path)
                    return
                
                visited.add(node[0])
                path.append(node[0])
                queue.appendleft(node[0])
    return 

datafile = pd.read_csv('../Dataset/indian-cities-dataset.csv')
hurestic_distance = pd.read_csv('../Dataset/Hurestic_distance-Indian-cities.csv')
G = nx.DiGraph()

# create a graph form csv to make digestable for algorithm
networkGraph = {}


# create a hurestic graph
hurestic_graph  ={}

for _,row in hurestic_distance.iterrows():
    # for Thiruvananthapuram
    hurestic_graph[row["Origin"]] = row["Heuristic_Distance_km"]

# print(hurestic_graph)

for _,row in datafile.iterrows():
    G.add_edge(row["Origin"],row["Destination"],weight =row["Distance"])
    if row["Origin"] in  networkGraph:
        networkGraph[row["Origin"]].append((row["Destination"], row["Distance"]))
    else:
        networkGraph[row["Origin"]] = [(row["Destination"], row["Distance"])]

# setting figure size
plt.figure(figsize=(14,10))

#position nodes
pos = nx.spring_layout(G,k=5,seed=1)

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
plt.axis("off")
plt.tight_layout()
plt.show(block=False)
# show plot for 10 sec and then close 
plt.pause(10)
plt.close()




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

# UniformCostSearch(networkGraph, "Patna" , "Thiruvananthapuram")

# AStar(networkGraph,hurestic_graph,"Patna" , "Thiruvananthapuram")


dfs(networkGraph,"Patna","Thiruvananthapuram")