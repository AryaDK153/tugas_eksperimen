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
    nodes = [i for i in range(N+1)]
    adj = [[] for i in range(N+1)]

    current_node = nodes.pop(0)
    return create_adj(nodes, adj, current_node)

def create_adj(nodes = [], adj = [[]], current_node = 0):
    if len(nodes) == 0:
        return adj
    
    add_child = random.choice([True, False])

    if add_child:
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


'''
Testing
'''    
if __name__ == '__main__':
    tree = maketree(5)
    print(tree)