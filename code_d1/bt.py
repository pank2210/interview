'''
   Binary Tree class
   
   1. Should support add/push, pop, remove and search.
   2. add should also add new node as head
   3. pop should always remove node from head
   4. remove should use value based search and then remove. i.e. given node value match then remove it.
   5. print exmaples of preorder, postorder and inorder
      5.1. depth dictionary implemented using preorder
      5.2. Inorder prints a sorted tree and used as a depth first algo. or used for BTree sort.
   6. Implement of Breath first using queue.
'''

import queue

class Node(object):
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None
   
  def set_left(self,node):
    self.left = node
   
  def set_right(self,node):
    self.right = node
   
  def get_left(self):
    return self.left
   
  def get_right(self):
    return self.left
   
  def get(self):
    return self.val

class BT:
  def __init__(self):
    print("BT init")
    self.head = None
    self.depth = {}
   
  def find_left_most_child(self,cnode):
    if not cnode.left:
      #print(" found - %s [%s] " % (type(cnode),cnode.get())) 
      return cnode
    return self.find_left_most_child(cnode.left)
   
  def find_right_most_child(self,cnode):
    if not cnode.right:
      #print(" found - %s [%s] " % (type(cnode),cnode.get())) 
      return cnode
    return self.find_right_most_child(cnode.right)
   
  def search(self,pnode,node,val):
    if node:
      #print("search v[%d] n[%d]" % (val,node.get()))
      if node.get() == val:
        #print(" %d > p[%d] n[%d]" % (val,pnode.get(),node.get()))
        return (pnode, node)
      if val > node.get():
        return self.search(node,node.right,val)
      else:
        return self.search(node,node.left,val)
   
  def del_node(self,val):
    #print("searching [%d]" % (val))
    ret = self.search(None,self.head,val)
    if ret: #search succeed 
      if ret[0]: #parent exist.
        print(" search of [%d] passed. parent[%d] and node[%d]" % (val,ret[0].get(),ret[1].get()))
      else: #parent is null so we foudn head match
        print(" search of [%d] passed. parent is null, head[%d] and node[%d]" % (val,self.head.get(),ret[1].get()))
    else:
      print(" search of [%d] failed. So, no action" % (val))
   
  def add_node(self,cnode,node):
    if cnode:
      if node.get() >= cnode.get(): 
        if cnode.right:
          #print(" %s > c[%d] n[%d]" % ('R',cnode.get(),node.get()))
          self.add_node(cnode.right,node)
        else:
          #print(" %s > c[%d] n[%d]" % ('*R',cnode.get(),node.get()))
          cnode.right = node
      else:
        if cnode.left:
          #print(" %s > c[%d] n[%d]" % ('L',cnode.get(),node.get()))
          self.add_node(cnode.left,node)
        else:
          #print(" %s > c[%d] n[%d]" % ('*L',cnode.get(),node.get()))
          cnode.left = node
   
  def add(self,val):
    if self.head:
      #print("**%d" % (self.head.get()))
      self.add_node(self.head,Node(val))
    else:
      self.head = Node(val)
   
  def inorder(self,node,depth=0):
    if node:
      #if node.left:
      self.inorder(node.left,depth+1)
      #print(" -%d(%d)- > " % (node.get(),depth),end="")
      print("%d(%d) " % (node.get(),depth),end="")
      #if node.right:
      self.inorder(node.right,depth+1)
   
  def preorder(self,node,depth=0):
    if node:
      print("%d(%d) " % (node.get(),depth),end="")
      if depth in self.depth: #build depth dict
        self.depth[depth].append(node)
      else:
        self.depth[depth]=[node]
      self.preorder(node.left,depth+1)
      self.preorder(node.right,depth+1)
   
  def preorder_prl(self,node,depth=0):
    if node:
      print("%d(%d) " % (node.get(),depth),end="")
      self.preorder_prl(node.right,depth+1)
      self.preorder_prl(node.left,depth+1)
   
  def postorder(self,node,depth=0):
    if node:
      self.postorder(node.left,depth+1)
      self.postorder(node.right,depth+1)
      print("%d(%d) " % (node.get(),depth),end="")
   
  def traverse(self,node,depth=0):
    if node:
      self.traverse(node.right,depth+1)
      print("%d(%d) " % (node.get(),depth),end="")
      self.traverse(node.left,depth+1)
   
  def refresh_depth_arr(self):
    if self.head:
      print("InOrder / LPR...")
      self.inorder(self.head)
      print("\n PreOrder / PLR Refreshing depth array of the Tree...")
      self.preorder(self.head)
      print("\n PostOrder / LRP...")
      self.postorder(self.head)
      print("\nPreOrder changed to PRL...")
      self.preorder_prl(self.head)
    else:
      print("empty tree")
   
  def bfs(self): #breadth first search implementation
    #q = queue.SimpleQueue()
    q = queue.Queue()
     
    q.put(self.head) #put initial node or head to start the algo
    #print(" head - ",self.head.val," queue empty - ",q.empty())
     
    depth=0 
    while(not q.empty()): #is not empty then keep processing
      node = q.get()
      print("%d " % (node.get()),end="")
      if node.left:
        q.put(node.left)
      if node.right:
        q.put(node.right)
   
  def print(self):
    for d in sorted(self.depth):
      print("\ndepth[%02d] " % (d),end="")
      for n in self.depth[d]:
        print("%3d " % (n.get()),end="")

def execute_test():
  #vals = [ 50, 20, 10, 15, 90, 5, 13]
  vals = [ 50,25,74,12,60,100,6,18,55,65,85,150,3,11,4,14,22,13,16,15,17,22,21,23,80,90,125,175,160,162,164,166,10,9,8]
   
  bt = BT()
  for v in vals:
    bt.add(v)
   
  bt.refresh_depth_arr()
  bt.print()
  print("\n","-"*10)
   
  print("right most child - ",bt.find_right_most_child(bt.head).get()) 
  print("left most child - ",bt.find_left_most_child(bt.head).get())
   
  print("Breadth First...")
  bt.bfs()
  print("\n","-"*10)
   
  del_vals = [50,10,13,22,85]
  for v in del_vals:
    bt.del_node(v)

if __name__ == "__main__":
  execute_test()
