def depth_first_search(graph : dict, source : str) -> None:
    print(source)
    for neighbour in graph[source]:
        depth_first_search(graph, neighbour)


graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

source = 'a'

graph = {0: [1, 2, 3, 4, 5, 6, 7, 8, 9], 1: [3, 5, 7, 9], 2: [3, 4, 5, 6, 7, 8, 9], 3: [5, 7, 9], 4: [5, 6, 7, 8, 9], 5: [7, 9], 6: [7, 8, 9], 7: [9], 8: [9]}
source = 0
depth_first_search(graph, source)