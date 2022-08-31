
import sys

sys.setrecursionlimit(200000)

debug = False
#debug = True

def log(msg,end=None):
  if debug:
    print(msg,end=end)

class Vertex(object):
  def __init__(self,id):
    self.id = id
    self.next = []
    self.level = None 
    self.pre_order = None 
    self.post_order = None 
   
  def print(self,next=True,end=None):
    if next:
      str = " {}({},{}/{}) : {}".format(self.id
                                       ,self.level
                                       ,self.pre_order
                                       ,self.post_order
                                       ,self.next)
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
    edges = list(zip(data[0:n:2],data[1:n:2]))
    log(" edges {} ".format(edges))
    self.adj = {}
    for (u,v) in edges:
      if u in self.adj:
        self.adj[u].next.append(v)
      else:
        self.adj[u] = Vertex(u)
        self.adj[u].next = [v]
      #for v create empty vertex initially
      if v not in self.adj:
        self.adj[v] = Vertex(v)
        self.adj[v].next = []
    self.size = len(self.adj.keys())
    self.print_adj()
   
  def print_adj(self):
    for v in self.adj:
      #str = " %s(%d,%d/%d) : ".format(self.adj[v].id
      self.adj[v].print()
   
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
    #self.print_adj()
     
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

def number_of_strongly_connected_components(input_data):
    dag = DAG(input_data)
    dag.run_scc()
     
    return dag.scc_count
   
if __name__ == '__main__':
    input_data = sys.stdin.read()
    #input_data = "5 10 1 2 1 3 4 5 1 4 1 5 2 3 2 5 3 4 2 4 3 5 1 5" #grader example
    #input_data = "4 2 1 2 3 2" #2 independant graphs
    #input_data = "7 4 1 2 3 2 5 6 6 7" #3 independant graphs
    #input_data = "4 0 1 2 3 2" #constraints testing
    #input_data = "4 4 1 2 3 2 4 3"
    #input_data = "4 4 1 2 4 1 2 3 3 1" #scc's 2
    #input_data = "5 72 1 3 2 3 1 4 3 4 1 5 2 5 3" #scc's 5
    #input_data = "8 8 0 1 1 2 2 3 2 4 3 0 4 5 5 6 6 4 6 7" #example from progamiz.com
    #input_data = "12 12 1 2 3 2 4 3 5 6 6 7 7 8 6 9 9 11 11 12 12 8 12 9 8 10" #cycle detect test
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
    print(number_of_strongly_connected_components(input_data))
