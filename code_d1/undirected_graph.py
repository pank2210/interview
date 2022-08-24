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
        return

'''
 input data to UndirectGrpah specs
    x = "4 4 1 2 3 2 4 3 1 4"
      x[0] = 4 is #vertices
      x[1] = 4 is #edges
      (x[i], x[i+]) from i=2 to range-2 are all individual edges showing graph connections
           where x[subscript] is vertices
      x[range-2] and x[range-1] represent a source to target vertices that needs to validated
           for existance
   UndirectedGraph
      self.v hold collection of vertices
      self.path holds all path (for each vertices as source it check all graph starting at 
                  that source or originations.
'''
class UndirectedGraph(object):
  def __init__(self,data: list):
    data = list(map(int, input.split()))
    n, m = data[0:2] #n is #vertices and m is #edges
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
     
    self.adj = adj #A raw form of undirected graph structure
    log(" adj - {} ".format(self.adj))
    
    self.v = Vertices()
    for ind,vlinks in enumerate(self.adj):
      self.v.add(ind,self.adj[ind])
    self.v.print()
   
  def reachable(x,y):
    #write your code here
    log(" Checking reachanility from x to {} y - {}".format(x,y))
    
    if x not in self.paths:
        self.paths[x] = Path(self.v,x) #generate path if not already generated
    
    return self.path[x].reachable(y)
  
  '''
    scans all unvisited vertices from collection to count how many unique independant graph exists.
    generates vertices, graph paths and returns #graph path found
  '''
  def generate_graphs(self):
    result = 0
   
    self.paths = {} 
    for vert_id,vert in self.v.vertices.items():
      if not vert.isvisited():
        self.paths[vert_id] = Path(self.v,vert_id)
        self.paths[vert_id].print()
        result += 1
      else:
        log("Path id[%s] already explored.." % (vert_id))
     
    return result

if __name__ == '__main__':
    #input = sys.stdin.read()
    #input = "5 10 1 2 1 3 4 5 1 4 1 5 2 3 2 5 3 4 2 4 3 5 1 5" #grader example
    #input = "4 2 1 2 3 2" #2 independant graphs
    #input = "7 4 1 2 3 2 5 6 6 7" #3 independant graphs
    #input = "4 0 1 2 3 2" #constraints testing
    input = "4 4 1 2 3 2 4 3 1 4"
    ug = UndirectedGraph(input)
    print(ug.generate_graphs())
