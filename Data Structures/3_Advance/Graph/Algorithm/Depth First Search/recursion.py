# Depth First Search is a searching algorithm which explores,
# all nodes unidirectioally until no nodes left
# It uses stack as a fundamental data structure

# directed graph
def dfs_ (graph:dict, src) -> None:

    if (src == None):
        return

    print(src)

    for neighbour_node in graph[src]:
        dfs_(graph, neighbour_node)

    return

# for both directed and undirected graph
def dfs (graph:dict, src, visited:set) -> None:
    
    if(src == None):
        return

    print(src)

    visited.add(src)

    for neighbour_node in graph[src]:
        
        if neighbour_node not in visited:

            dfs(graph, neighbour_node, visited) 
    
    return

if __name__ == "__main__":

    graph = {
        'f' : ['g', 'i'],
        'g' : ['h'],
        'h' : [],
        'i' : ['g', 'k'],
        'j' : ['i'],
        'k' : []
    }

    undirected_graph = {
        'i' : ['j', 'k'],
        'j' : ['i'],
        'k' : ['i', 'm', 'l'],
        'm' : ['k'],
        'l' : ['k'],
        'o' : ['n'],
        'n' : ['o']
    } 

    src = "f"  

    #dfs_(graph, src)

    src = 'i'
    visited = set()

    dfs(undirected_graph, src, visited)
