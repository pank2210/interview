#Uses python3

import sys

debug = True
#debug = False

def log(msg,end=None):
  if debug:
    print(msg,end=end)

'''
  Vertice object holding point in given graph
'''
class Vertice(object):
  def __init__(self,id,links=[],visited=False):
    self.id = id
    self.links = links #holds pointer/reference to connected Vertice
    self.visited = visited #is set to true when this vertice is visited as part of path
   
  def set_visited(self):
    self.visited = True
   
  def isvisited(self):
    return self.visited
   
  def get_links(self):
    return self.links
   
  def print(self):
    log(" id[%s] links[%s] visited[%s]" % (self.id,self.links,self.visited))

'''
  A Collection holding all vertices within the Graph
  collection is maintain as hash dictionary
'''
class Vertices(object):
  def __init__(self):
    self.vertices = {}
  
  def add(self,k,v):
    self.vertices[k] = Vertice(k,v)
  
  def print(self):
    for k,v in self.vertices.items():
      log(" k[%s] : " % (k),end="")
      v.print()
 
'''
  A Instance of Depth-First-Search DFS runed on given starting vertice
   traverse() funciton is recursive DFS and every node it discovers it add it to set
   and stops when same there is no further link node or linked node was previously
   visited.
   Recoccurence is use to recurse when links are encounter.
   Once set collection of all unique vertices/noides within path are collected then 
   any path from given vertice (source) to destination can be checked as assertion
   of vertices id present in the collected set. 
''' 
class Path(object):
  def __init__(self,v,x):
    self.id = x
    self.set = set()
    self.path = []
    self.v = v
    self.cycles = [] #adds id's if cycle detected.
    self.traverse(x)
  
  def exist(self,id):
    if id in self.set:
      return True
    else:
      return False
  
  def reachable(self,id):
    if self.exist(id):
      log(" [%s] is reachable to [%s]" % (self.id,id))
      return 1
    else:
      log(" [%s] is not reachable to [%s]" % (self.id,id))
      return 0
  
  def add(self,id):
    if not self.exist(id):
      log(" Adding %s " % (id))
      self.set.add(id)
      self.path.append(id)
      self.v.vertices[id].set_visited()
      return True
    else:
      log("Error: [%s]id already in [%s]path so ignored" % (id,self.id))
      return False
  
  def print(self):
    log("Path id[{}] Set - {} ".format(self.id,self.set))
    for id in self.path:
      log("[%s] -> " % (id),end="")
     
  def check_loop(self,x,arr:list = []):
    if not x:
      return 
    else:
      if x in arr:
        log("Cycle detect confirmed at #{} within DAG.".format(x))
        log(arr)
        self.cycles.append(x)
        return 
      else:
        arr.append(x)
        for vlink in self.v.vertices[x].get_links(): 
          self.check_loop(vlink,arr)
        return
     
  def traverse(self,x):
    if x not in self.v.vertices: 
      log("Error x[%s] not in vertices collection." % (x))
      return
    else:
      if not self.exist(x):
        self.add(x)
        for vlink in self.v.vertices[x].get_links(): 
          self.traverse(vlink)
        return
      else:
        log("Initial cycle suspect at #{} within DAG.".format(x))
        self.check_loop(x,[])
        return
  
  def get_cycle_count(self):
    return len(self.cycles)

'''
 input data to DirectGrpah specs
    x = "4 4 1 2 3 2 4 3 1 4"
      x[0] = 4 is #vertices
      x[1] = 4 is #edges
      (x[i], x[i+]) from i=2 to range-2 are all individual edges showing graph connections
           where x[subscript] is vertices
      x[range-2] and x[range-1] represent a source to target vertices that needs to validated
           for existance
   DirectedGraph
      self.v hold collection of vertices
      self.path holds all path (for each vertices as source it check all graph starting at 
                  that source or originations.
'''
class DirectedGraph(object):
  def __init__(self,data: list):
    data = list(map(int, input.split()))
    n, m = data[0:2] #n is #vertices and m is #edges
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    ''' Array mode changed to hash mode as original keys can be retained
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        #adj[b - 1].append(a - 1) #line will created a bi-directional Graph or undirected
    '''
    adj = {}
    for (a,b) in edges:
      if a in adj:
        adj[a].append(b)
      else:
        adj[a] = [b]
      if b not in adj: #'b' should also be part of collection
        adj[b] = [] #since undirected graph to vertices needs to be empty for first visit
         
     
    self.adj = adj #A raw form of undirected graph structure
    log(" adj - {} ".format(self.adj))
     
    self.v = self.generate_vertices(self.adj) #buidl vertices collection
    self.starts = self.find_starts() #build list of all starts vertices from collections
    
  '''
    returns vertices collection objects from given dict of vertices represent in edge format.
  '''
  def generate_vertices(self,adj: dict):
    v = Vertices()
    #for ind,vlinks in enumerate(self.adj):
    for ind,vlinks in adj.items():
      v.add(ind,adj[ind])
    v.print()
    
    return v
  
  '''
    return sinks i.e. all vertices from given collection where links are null
  '''
  def find_sinks(self,vertices):
    sinks = []
    for ind,vert in vertices.vertices.items():
      if not len(vert.links): #vertices does have any links to other forward vertices
        sinks.append(ind)
    
    log("sinks discovered {}".format(sinks))
    
    return sinks
  
  '''
    returns all start vertices of graph.
      idea is to reverse the graph so that all starter becomes sinks and then get sinks
      finding started in direct way had same time complexity as reverse but needs more memory
  '''
  def find_starts(self):
    reverse_vertices = self.reverse_graph()
     
    starts = self.find_sinks(reverse_vertices)
    log("starts discovered {}".format(starts))
    
    return starts
  
  ''' 
    just reverses all pointers in dictionary of vertice collection
    key becomes value and value become keys. key with empty array are ignored as they are already taken care.
  ''' 
  def reverse_graph(self):
    #reverse the graph using vertices
    reverse_adj = {}
    for ind,vert in self.v.vertices.items():
      if vert.links:
        #reverse_adj[ind] = []
        for link in vert.links:
          if link in reverse_adj: 
            reverse_adj[link].append(ind)
          else:
            reverse_adj[link] = [ind]
      #log("*** ind[{}] links[{}] reverse_adj[{}]".format(ind,vert.links,reverse_adj))
    
    #populate sinks based on start which fail processing in reverse graph
    starts = list(set(self.v.vertices.keys()) - set (reverse_adj.keys()))
    for ind in starts:
      reverse_adj[ind] = []
    
    return self.generate_vertices(reverse_adj)
   
  def reachable(self,x,y):
    #write your code here
    log(" Checking reachanility from x to {} y - {}".format(x,y))
    
    if x not in self.paths:
        self.paths[x] = Path(self.v,x) #generate path if not already generated
    
    return self.paths[x].reachable(y)
  
  '''
    scans all unvisited vertices from collection to count how many unique independant graph exists.
    generates vertices, graph paths and returns #graph path found
  '''
  def generate_graphs(self):
    result = 0
   
    self.paths = {} 
    for vert_id in self.starts:
      vert = self.v.vertices[vert_id]
      if not vert.isvisited():
        self.paths[vert_id] = Path(self.v,vert_id)
        self.paths[vert_id].print()
        result += 1
      else:
        log("Path id[%s] already explored.." % (vert_id))
     
    log("\n#{} valid graphs/path discovered starting from {}".format(result,self.paths.keys()))
     
    return result
   
  def get_cycles_count(self):
    cycles_count = 0
     
    for vert_id in self.starts:
      cycles_count += self.paths[vert_id].get_cycle_count()
     
    return cycles_count 

if __name__ == '__main__':
    #input = sys.stdin.read()
    #input = "5 10 1 2 1 3 4 5 1 4 1 5 2 3 2 5 3 4 2 4 3 5 1 5" #grader example
    #input = "4 2 1 2 3 2" #2 independant graphs
    #input = "7 4 1 2 3 2 5 6 6 7" #3 independant graphs
    #input = "4 0 1 2 3 2" #constraints testing
    #input = "4 4 1 2 3 2 4 3"
    input = "12 12 1 2 3 2 4 3 5 6 6 7 7 8 6 9 9 11 11 12 12 8 12 9 8 10" #cycle detect test
    '''
           4 -> 3 -> 2
                     ^
                     |
                  1 -+
                     
                     
                         +-> 11 -> 12 -> 9
                         |          |
                     +-> 9          +-> 8
                     |
                5 -> 6 -> 7 -> 8 -> 10
    '''
    log("input - {} ".format(input))
    dag = DirectedGraph(input)
    print(dag.generate_graphs())
    print(dag.get_cycles_count())
    print(dag.reachable(1,4))
    print(dag.reachable(1,3))
    print(dag.reachable(3,2))
