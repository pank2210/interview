
import queue

debug = True
#debug = False

def log(msg,end=None):
  if debug:
    print(msg,end=end)

class Vertex(object):
  def __init__(self,id):
    self.id = id
    self.next = []
    self.weights = []
    self.level = None 
    self.pre_order = None 
    self.post_order = None 
   
  def print(self,next=True,end=None):
    if next:
      str = " {}({},{}/{}) : {} {}".format(self.id
                                       ,self.level
                                       ,self.pre_order
                                       ,self.post_order
                                       ,self.next
                                       ,self.weights)
    else:
      str = " {}({},{}/{})".format(self.id
                                       ,self.level
                                       ,self.pre_order
                                       ,self.post_order)
    log(str,end)
   
class DAG(object):
  def __init__(self,data):
    self.order = 0
     
    data = list(map(int,data.split()))
    data = data[2:]
    n = len(data)
    edges = list(zip(data[0:n:3],data[1:n:3],data[2:n:3]))
    log(" edges {} ".format(edges))
    self.adj = {}
    for (u,v,w) in edges:
      print(" (({},{}),{})".format(u,v,w))
      if u in self.adj:
        self.adj[u].next.append(v)
        self.adj[u].weights.append(w)
      else:
        self.adj[u] = Vertex(u)
        self.adj[u].next = [v]
        self.adj[u].weights = [w]
      #for v create empty vertex initially
      if v not in self.adj:
        self.adj[v] = Vertex(v)
        self.adj[v].next = []
        self.adj[v].weights = []
    self.size = len(self.adj.keys())
    self.print_adj()
   
  def print_adj(self):
    for v in self.adj:
      #str = " %s(%d,%d/%d) : ".format(self.adj[v].id
      self.adj[v].print()
  
  def dijkstra(self,x,dist,prev,target):
    if target not in self.adj:
      log("target {} not in vertices".format(target))
      return
    q = queue.PriorityQueue()
    q.put((0,x)) #key=distance which is 0 for source or starting point
    dist[x] = 0
    while not q.empty():
    #for i in range(len(self.adj)):
      v_tuple = q.get()
      print("Processing {}".format(v_tuple))
      v = v_tuple[1] #select vertex id for node to process
      '''
      #dist[v] = v_tuple[0] #capture weight for the vertex id
      if v == target:
        break
      '''
      for ind,next in enumerate(self.adj[v].next):
        print("  v_dist {} next {} next_dist {}".format(dist[v] + self.adj[v].weights[ind],next,dist[next]))
        if dist[v] + self.adj[v].weights[ind] < dist[next]:
          dist[next] = dist[v] + self.adj[v].weights[ind]
          prev[next] = v
          if v != target:
            q.put((dist[next],next))
    
  def run_dijkstra(self,source,target):
    dist = {k:9999 for k in self.adj}
    prev = {k:None for k in self.adj}
    self.dijkstra(source,dist,prev,target)
    
    if dist[target] == 9999:
      log("No path exists between source {} and target {}".format(source,target))
      return -1 #path between source to target doesnt exists
    else:
      log(" Dijkstra dist [{}] ".format(dist))
      
      cur = target
      log("\n Shortest path from {} to {} is #{} units and path is [".format(source,target,dist[target]),end="")
      while cur != source:
        log(" {}({}) -> ".format(cur,self.adj[cur].pre_order),end="")
        cur = prev[cur]
      log(" {}({})] ".format(cur,self.adj[cur].pre_order))
      
      return dist[target]
     
   
  def bfs(self,x,order,dist,prev,target=None):
    seq = 0
    q = queue.Queue()
    q.put(x)
    while not q.empty():
      v = q.get()
      order.append(v)
      for next in self.adj[v].next:
        if dist[next] == 9999:
          dist[next] = dist[v] + 1
          prev[next] = v
          if target: 
            if next != target:
              q.put(next)
          else:
            q.put(next)
          self.adj[next].pre_order=seq 
          seq += 1
   
  def run_bfs(self):
    #initialize key collectors
    visited = {}
    dist = {}
    prev = {}
    for v in self.adj:
      dist[v] = 9999
      prev[v] = None
     
    #log(" size - {} visited {} ".format(self.size,visited))
    order = []
    for v in self.adj:
      if dist[v] == 999:
        dist[v] = 0
        self.bfs(v,order,dist,prev)
     
    log(" BFS order [{}] ".format(order))
    for v in order:
      log("[{}]({},{},{}) ".format(v,self.adj[v].pre_order,prev[v],dist[v]),end="")
   
  def get_shortest_path(self,source,target):
    if source not in self.adj or target not in self.adj:
      log("Either of source {} and target {} is not valid vertice".format(source,target))
      return -1 #path between source to target doesnt exists
      
    #initialize key collectors
    dist = {}
    prev = {}
    for v in self.adj:
      dist[v] = 9999
      prev[v] = None
     
    #log(" size - {} visited {} ".format(self.size,visited))
    order = []
    dist[source] = 0
    self.bfs(source,order,dist,prev,target)
    
    if dist[target] == 9999:
      log("No path exists between source {} and target {}".format(source,target))
      return -1 #path between source to target doesnt exists
    else:
      log(" BFS order [{}] ".format(order))
      for v in order:
        #log("[{}]({},{}) ".format(v,prev[v],dist[v]),end="")
        log("[{}]({},{},{}) ".format(v,self.adj[v].pre_order,prev[v],dist[v]),end="")
      
      cur = target
      log("\n Shortest path from {} to {} is #{} units and path is [".format(source,target,dist[target]),end="")
      while cur != source:
        log(" {}({}) -> ".format(cur,self.adj[cur].pre_order),end="")
        cur = prev[cur]
      log(" {}({})] ".format(cur,self.adj[cur].pre_order))
      
      return dist[target]
   
  def dfs(self,x,visited:list,level:int=0):
    if visited[x]:
      return
    visited[x] = True
    level += 1
    self.order += 1
    self.adj[x].level = level
    self.adj[x].pre_order = self.order
    self.adj[x].print(next=True, end=" -> ")
    for next in self.adj[x].next:
      #if not visited[next]:
      self.dfs(next,visited,level)
    self.order += 1
    self.adj[x].post_order = self.order
  
  def run_dfs(self):
    visited = {}
    for v in self.adj:
      visited[v] = False
    #log(" size - {} visited {} ".format(self.size,visited))
    for v in self.adj:
      self.dfs(v,visited)
   
  def toposort(self,x,visited,stack): 
    if visited[x]:
      return
    visited[x] = True
    for next in self.adj[x].next:
      self.toposort(next,visited,stack)
    stack.append(x)
   
  def run_toposort(self):
    stack = []
    visited = {}
    for v in self.adj:
      visited[v] = False
     
    for v in self.adj:
      if not visited[v]:
        self.toposort(v,visited,stack)
    
    self.print_adj()
    log("\n stack - {}".format(stack))
    log("\n toposort - {}".format(stack[::-1]))
    
    return stack
   
  def reverse_adj(self):
    reverse_adj = {}
    for i in self.adj:
      for j in self.adj[i].next:
        if j not in reverse_adj:
          reverse_adj[j] = Vertex(j)
          reverse_adj[j].next.append(i)
        else:
          reverse_adj[j].next.append(i)
        if i not in reverse_adj:
          reverse_adj[i] = Vertex(i)
        #log(" (i,j) {} reverse_adj j[{}] i [{}]".format((i,j),reverse_adj[j].id,reverse_adj[i].id))
    self.adj = None
    self.adj = reverse_adj
    #self.print_adj()
        
  def run_scc(self):
    #create toposort stack array 
    stack = self.run_toposort()
     
    #reverse the graph 
    #self.print_adj()
    self.reverse_adj() 
     
    #run DFS on reversegraph using toposort stack of original graph 
    visited = {}
    for v in self.adj:
      visited[v] = False
     
    self.scc_count = 0 
    self.cycles = 0 
    while stack:
      v = stack.pop()
      if not visited[v]:
        scc_stack = []
        self.toposort(v,visited,scc_stack)
        self.scc_count += 1
        if len(scc_stack) > 1:
          self.cycles += 1
        log("\n***** scc_stck {}".format(scc_stack))
     
    log(" scc_count [{}] cycles [{}]".format(self.scc_count,self.cycles)) 

def run_graph(input_data):
    dag = DAG(input_data)
    print(dag.run_dijkstra(5,10))
     
    return 1
   
if __name__ == '__main__':
    #input_data = sys.stdin.read()
    #input_data = "8 9 1 2 2 2 3 3 3 4 4 2 5 1 5 7 2 7 8 1 8 4 1 8 5 1 4 6 2 1 6" 
    input_data = "8 9 5 6 2 6 7 3 7 8 4 6 9 1 9 11 2 11 12 1 12 8 1 12 9 1 8 10 2 5 10" 
   
    '''
      SCC's 4
           4 -> 3 -> 2
                     ^
                     |
                  1 -+
                     
       SCC's 6
            
                         +-> 11 -> 12 -> 9
                         |          |
                     +-> 9          +-> 8
                     |
                5 -> 6 -> 7 -> 8 -> 10
    '''
    log("input_data - {} ".format(input_data))
    print(run_graph(input_data))
