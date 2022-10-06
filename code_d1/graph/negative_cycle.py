#Uses python3

import sys

debug=False
#debug=True

def log(str,end=None):
  if debug:
    print(str,end=end)

def negative_cycle(adj, cost):
    #write your code here
    log(" adj - {} ".format(adj))
    log(" cost - {} ".format(cost))
    
    inf = float("inf")
     
    dist = [inf]*len(adj)
    dist[0] = 0
    for i in range(len(adj)):
      early_stopping = True
      for ind,next in enumerate(adj[i]): 
        if dist[i] + cost[i][ind] < dist[next]:
          early_stopping = False
          dist[next] = dist[i] + cost[i][ind]
          log("*** {}({}) --({})--> {}({})".format(i,dist[i],cost[i][ind],next,dist[next]))
        else:
          log("+++ {}({}) --({})--> {}({})".format(i,dist[i],cost[i][ind],next,dist[next]))
      log(" #{} iteration dist {}".format(i,dist))
      if early_stopping:
        log("Early stoping after #{} iterations".format(i))
    
    #'''
    log("------------") 
    neg_cycles = []
    for i in range(len(adj)-1):
      early_stopping = True
      for ind,next in enumerate(adj[i]): 
        if dist[i] + cost[i][ind] < dist[next]:
          early_stopping = False
          dist[next] = dist[i] + cost[i][ind]
          neg_cycles.append(next)
          log("*** {}({}) --({})--> {}({})".format(i,dist[i],cost[i][ind],next,dist[next]))
        else:
          log("+++ {}({}) --({})--> {}({})".format(i,dist[i],cost[i][ind],next,dist[next]))
      log(" #{} iteration dist {}".format(i,dist))
      if early_stopping:
        log("Early stoping after #{} iterations".format(i))
    #'''
    log("negative cycles are at {} ".format(neg_cycles)) 
     
    if len(neg_cycles) > 1:
      return 1
    else: 
      return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = "4 4 1 2 1 4 1 2 2 3 2 1 3 5 1 3" #should output 3 
    #input = "3 3 1 2 7 1 3 5 2 3 2 3 2" #o/p -1
    #input = "5 9 1 2 4 1 3 2 2 3 2 3 2 1 2 4 2 3 5 4 5 4 1 2 5 3 3 4 4" #o/p 6
    #input = "8 9 1 2 2 2 3 3 3 4 4 2 5 1 5 7 2 7 8 1 8 4 1 8 5 1 4 6 2 1 6" 
    #input = "4 4 1 2 -5 4 1 2 2 3 2 3 1 1"
     
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
