def breadth_first_search(graph, node, visited):
    visited.append(node)
    queue.append(node)
    while queue:
        v = queue.pop(0)
        print(v,end=" ")
        
        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

graph1 = {
    'a' : ['b', 'c'],
    'b' : ['d','e','a'],
    'c' : ['f','a'],
    'd' : ['b','g'],
    'e' : ['b'],
    'f' : ['c'],
    'g' : ['d']   
}
graph2 = {    
    'a' : ['b', 'c' ,'d'],
    'b' : ['a','f','e'],
    'c' : ['f','a'],
    'd' : ['a'],
    'e' : ['b'],
    'f' : ['b','c']
}
source = 'a'
visited = []
queue = []

breadth_first_search(graph2, source, visited)
