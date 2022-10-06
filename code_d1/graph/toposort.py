#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    if used[x]:
      return
    used[x] = 1
    for i in adj[x]:
      dfs(adj,used,order,i)
    order.append(x)

def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here
    #print(adj,used,order)
    for i,next in enumerate(adj):
      if not used[i]:
        dfs(adj,used,order,i)
     
    return order[::-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = "12 12 1 2 3 2 4 3 5 6 6 7 7 8 6 9 9 11 11 12 12 8 12 9 8 10" #cycle detect test
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

