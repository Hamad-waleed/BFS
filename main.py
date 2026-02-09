from tree import *

# Key: Destination
# Value: List of tuples (Source, Cost)

romania_graph = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Vaslui', 142), ('Hirsova', 98)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}



import queue
qu = queue.Queue()
root = Tree(("Arad" , 0))

# This is a recursive implementation of BFS, but it is not recommended for large graphs due to potential stack overflow issues.
def bfs(root):
    # here we unpack root to cost as co and source as src
    co = root.value[1]
    src = root.value[0]
    # this is safety and check if this node is the destination 
    # is condition stop
    if(co > 1000 or src == "Neamt"):
        return root
    
    # unpack the root to childern and add them to the queue
    for des , cost in romania_graph[src]:
        totalcost = root.value[1]+cost
        chiled = root.add_child((des , totalcost))
        qu.put(chiled)
    #here we get the first node in the queue and call bfs on it
    z  = qu.get()
    return bfs(z)



# this is an while loop implementation of BFS , it is more efficient and does not have the risk of stack overflow.
def bfswhile(firstnode:Tree , dest:str):
    #it take a tree as a prameter and a destination city as a string
    # then put teh first node in the queue
    q = queue.Queue()
    q.put(firstnode)
    print(type(firstnode))

    while not q.empty():
        # here cuurnt node to the first node in the queue
        currnt_node = q.get()
         # here we unpack root to cost  and city
        city = currnt_node.value[0]
        cost = currnt_node.value[1]
        # the condition to stop the loop 
        # if the city to currnt node = detination return the currnt node
        if city == dest or cost>1500:
            return currnt_node
    

        # unpack the root to childern and add them to the queue
        for src , co in romania_graph[city]:
            totalcost = cost + co
            chiled = currnt_node.add_child((src , totalcost))
            q.put(chiled)
    # if the queue is empty and we did not find the destination, we return None
    return None


# here test the bfs function and print the result
x = bfswhile(root, "Neamt")
print("-"*30)
print(f'the distinchin is {x.value[0]} and cost is {x.value[1]}\nand the bath is {path(x)}')

