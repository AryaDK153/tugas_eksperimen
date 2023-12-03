'''
Idea:
1. Make N nodes, put it in list
=> nodes = [1, 2, 3, 4, ..., N]

2. Take nodes in order
=> current_node: nodes.pop(0)

3. addedge(adj, node_a, node_b) P times;
    Q <= P <= len(nodes)
    Q = previous_node_b
    node_a = current_node
    node_b = child_to_be
=> node_b = nodes.pop(0)
...

so anyway, I continued without any idea documentation :D
'''

from vertex_cover_dp import addEdge
import random

def maketree(N):
    result = []
    last_bottom = 0
    top = 500

    # Ok this works (hopefully with correct dataset result, also, no idea about max recursion, but definitely not infinite)
    for repeat in range((N//8000)+1):
        # Stack overflow prevention (tested ==> max recursion is 500 without this, but max recursion becomes 8000 with this... still not enough)
        while N > 0:
            if N < top:
                top = N

            nodes = [i for i in range(top)]
            adj = [[] for i in range(top)]

            current_node = nodes.pop(0)
            try:
                adj = create_adj(nodes, adj, current_node)
            except RecursionError:
                break
            
            for adj_each in adj:
                for i in range(len(adj_each)):
                    adj_each[i] += last_bottom
                result.append(adj_each)

            last_bottom += top
            N -= top
    return result

def create_adj(nodes = [], adj = [[]], current_node = 0):
    if len(nodes) == 0:
        return adj
    
    add_child = random.choice([True, False])

    if add_child or current_node == 0:
        # Add child
        next_node = nodes.pop(0)
        addEdge(adj, current_node, next_node)
        return create_adj(nodes, adj, next_node)
    else:
        # Backtrack 1 node
        prev_node = 0
        for node in adj[current_node]:
            if node < current_node:
                prev_node = node
                break
        return create_adj(nodes, adj, prev_node)


# '''
# Testing
# '''    
# if __name__ == '__main__':
#     tree = maketree(100000)
#     print(tree)


# # Run IF AND ONLY IF you want to get new datasets in dataset.txt
if __name__ == "__main__":
    file = open("TE2\dataset.txt", "w")
    to_write = ""
    size = 10000
    for i in range(3):
        to_write += f"{maketree(size)}\n"
        size *= 10
    file.write(to_write)
    file.close()
    print("Created new datasets for dataset.txt")