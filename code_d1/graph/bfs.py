#Uses python3

import sys
import queue

debug=False
#debug=True

def log(msg,end=None):
  if debug:
    print(msg,end=end)

def bfs(adj,s,t,order,prev,dist):
  q = queue.Queue()
  q.put(s)
  while not q.empty():
    x = q.get()
    order.append(x)
    for next in adj[x]:
      log(" x {} next {} ".format(x,next))
      if dist[next] == 999:
        if next != t:
          q.put(next)
        dist[next] = dist[x] + 1
        prev[next] = x

def distance(adj, s, t):
    #write your code here
    order = []
    dist = {}
    prev = {}
        
    log(" s {} t {} adj {} ".format(s,t,adj))    
        
    for v,_ in enumerate(adj):
      dist[v] = 999 
      prev[v] = None 
    
    dist[s] = 0
    bfs(adj,s,t,order,prev,dist)
    log("{} {} {}".format(order,prev,dist))
    if t in dist and dist[t] != 999:
      if debug:
        log("\ndist of {} to {} is #{} and path is [".format(s,t,dist[t]),end="")
        cur = t
        while cur != s:
          log(" {} ->".format(cur),end="")
          cur = prev[cur]
        log(" {}".format(cur))
       
      return dist[t]
    else: 
      return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = "12 14 1 2 2 3 3 6 6 7 2 4 4 5 5 7 7 8 2 9 9 10 10 8 2 11 11 12 12 8 1 4"
    #input = "4 4 1 2 4 1 2 3 3 1 2 4"
    #input = "5 4 5 2 1 3 3 4 1 4 3 5"
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
