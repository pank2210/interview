#Uses python3

import sys
import queue

debug=False
#debug=True

def log(str,end=None):
  if debug:
    print(str,end=end)

def distance(adj, cost, s, t):
    #write your code here
    q = queue.PriorityQueue()
    dist = [float("inf")] * len(adj)
    '''
    for i in range(len(adj)):
      dist[i] = -999
      prev[i] = None
    '''
    
    log(" s[{}] t[{}]".format(s,t))
    log(" adj[{}]".format(adj))
    log(" cost[{}]".format(cost))
    dist[s] = 0
    q.put((0,s))
    while not q.empty():
      v = q.get()
      log("+++tuple{} v{}".format(v,v[1]))
      v = v[1]
      for ind,next in enumerate(adj[v]):
        #log("***v {} next {} adj[v] {}***".format(v,next,adj[v]))
        if dist[v] + cost[v][ind] < dist[next]:
          dist[next] = dist[v] + cost[v][ind]
          log("***v {} next {} dist[v] {} dist[next] {}***".format(v,next,dist[v],dist[next]))
          if next != t:
            q.put((dist[next],next))
     
    log(" dist[{}]".format(dist))
    if dist[t] != float("inf"):
      return dist[t]
    else:
      return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    #input = "8 9 1 2 2 2 3 3 3 4 4 2 5 1 5 7 2 7 8 1 8 4 1 8 5 1 4 6 2 1 6" 
    #input = "4 4 1 2 1 4 1 2 2 3 2 1 3 5 1 3" #should output 3 
    #input = "5 9 1 2 4 1 3 2 2 3 2 3 2 1 2 4 2 3 5 4 5 4 1 2 5 3 3 4 4 1 5" #o/p 6
    #input = "3 3 1 2 7 1 3 5 2 3 2 3 2" #o/p -1
     
    data = list(map(int, input.split()))
    n, m = data[0:2]
    log("n {} m{}".format(n,m))
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    log("edges - {}".format(edges))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        log("(({},{}),{})".format(a,b,w))
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
