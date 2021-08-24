def length_of_edge_list(graph):
    count = 0
    for node in graph:
        for child_node in graph[node]:
            count+=len(graph[child_node])
    return count

def solution(arr):
    
    length = len(arr)

    graph = {}

    # Creating graph where node is index
    for node in range(length):
        graph[node] = []


    for node in range(0, length):
        for index in range(node+1, length):
            # If condition satisfy it will add edges
            if arr[index] % arr[node] == 0:
                # If graph is empty
                if graph[node] == []:
                    graph[node] = [index]
                else:
                    graph[node].append(index)
    
    # The sum of all edge list     
    return length_of_edge_list(graph)

if __name__ == "__main__":
    user_list = [1, 2, 3, 4, 5, 6]
    """
    user_list = []

    for i in range(0,2000):
        if i%2==0:
            user_list.append(1)
        else:
            user_list.append(2)
            """

    result = solution(user_list)
    print(result)