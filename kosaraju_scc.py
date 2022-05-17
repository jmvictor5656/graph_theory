import collections
n=7
edges = [[0, 1], [0, 6], [1, 4], [2, 3], [2, 5], [3, 2], [3, 5], [4, 0], [4, 5], [6, 4]]

adj = collections.defaultdict(list)
rev_adj = collections.defaultdict(list)

for u, v in edges:
    adj[u].append(v)
    rev_adj[v].append(u)

visited = [False]*n
finish_order = []

def dfs(u, adj):
    visited[u]=True
    for v in adj[u]:
        if not visited[v]:
            dfs(v, adj)
    finish_order.append(u)

# forward dfs
for i in range(n):
    if not visited[i]:
        dfs(i, adj)

# reverse the dfs order
finish_order.reverse()
visited = [False]*n
result = []
transposed = list(finish_order)
finish_order = []

# iterate over reverse finish order in reverse adj list
# and put all visited node for one loop in result
for i in transposed:
    if not visited[i]:
        dfs(i, rev_adj)
        result.append(finish_order)
        finish_order = []

print(result)
    
