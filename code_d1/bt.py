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
    self.parent = None
    self.h = 1
   
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
        #handle duplicate by selecting the last child
        while node.right and node.right.get() == val:
          pnode = node
          node = node.right
        return (pnode, node)
      if val > node.get():
        return self.search(node,node.right,val)
      else:
        return self.search(node,node.left,val)
   
  ''' 
  def find_min_val_node(self,cnode):
    if cnode.left:
      #print(" found - %s [%s] " % (type(cnode),cnode.get())) 
      return find_min_val_node(cnode.left)
  ''' 
   
  def del_node(self,val):
    print("\nsearching [%d]" % (val))
    ret = self.search(None,self.head,val)
    if ret: #search succeed 
      if ret[0]: #parent exist.
        print(" search of [%d] passed. parent[%d]" % (val,ret[0].get()))
      else: #parent is null so we found head match
        print(" search of [%d] passed. parent is null, head[%d] and node[%d]" % (val,self.head.get(),ret[1].get()))
    else:
      print(" search of [%d] failed. So, no action" % (val))
   
    parent = ret[0] #parent of node to be deleted
    node = ret[1] #keep hold for node to be deleted
     
    parents_left = False 
    if parent.left == node:
      print("del node is left child of its parent.")
      parents_left = True 
    else:
      print("del node is right child of its parent.")
      parents_left = False 
     
    if not node.left and not node.right: #case node is leaf node
      print("del node was leaf node.")
      if parents_left:
        parent.left = None
      else:
        parent.right = None
      node = None
    else:
      if node.left and node.right: #case node has tree on both side
        print("del node has both childs.")
         
        #find min value node and unplug it to replace our del node 
        min_val_node = self.find_left_most_child(node.right)
        print("identified min_val_node[{}]".format(min_val_node.get()))
        parent_min_val_node = min_val_node.parent
        parent_min_val_node.left = None

        #adjust right child of node which we are going to unplug. repoint min value node parent to the right child.
        node_to_trigger_height_adj = parent_min_val_node
        if min_val_node.right:
          print("min_val_node[{}] has right child[{}]".format(min_val_node.get(),min_val_node.right.get()))
          parent_min_val_node.left = min_val_node.right
          node_to_trigger_height_adj = min_val_node.right #upd height trigger
          min_val_node.right.parent = parent_min_val_node #upd parent
         
        #now replace del node with min val node.
        if parents_left: #update correct pointer of parent
          parent.left = min_val_node
        else:
          parent.right = min_val_node
        min_val_node.parent = node.parent  #set parent of node
        min_val_node.left = node.left  #upd right child
        min_val_node.right = node.right  #upd left child
        node.right.parent = min_val_node #upd childs parent
        node.left.parent = min_val_node #upd childs parent
        print("** mv n[{}] p[{}] l[{}] r[{}] htrigger[{}]".format( \
                   min_val_node.get() 
                   ,min_val_node.parent.get() 
                   ,min_val_node.left.get() 
                   ,min_val_node.right.get() 
                   ,node_to_trigger_height_adj.get() ))
        self.adjust_height(node_to_trigger_height_adj)
         
      if not node.left: #case no left child 
        print("del node doesnt have left child.")
        if parents_left:
          parent.left = node.right
        else:
          parent.right = node.right
      if not node.right: #case no right child 
        print("del node doesnt have right child.")
        if parents_left:
          parent.left = node.left
        else:
          parent.right = node.left
       
      #finally delete the node 
      print("finally delete the identified node")
      node = None
  
  def adjust_height(self,cnode):
    if cnode:
      max_h = cnode.h
      if cnode.left:
        max_h = cnode.left.h
      if cnode.right:
        if max_h < cnode.right.h:
          max_h = cnode.right.h
      cnode.h = max_h + 1
      self.adjust_height(cnode.parent)
   
  def add_node(self,cnode,node):
    if cnode:
      if node.get() >= cnode.get(): 
        if cnode.right:
          #print(" %s > c[%d] n[%d]" % ('R',cnode.get(),node.get()))
          self.add_node(cnode.right,node)
        else:
          #print(" %s > c[%d] n[%d]" % ('*R',cnode.get(),node.get()))
          cnode.right = node
          node.parent = cnode
          self.adjust_height(cnode)
      else:
        if cnode.left:
          #print(" %s > c[%d] n[%d]" % ('L',cnode.get(),node.get()))
          self.add_node(cnode.left,node)
        else:
          #print(" %s > c[%d] n[%d]" % ('*L',cnode.get(),node.get()))
          cnode.left = node
          node.parent = cnode
          self.adjust_height(cnode)
   
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
   
  def preorder(self,node,depth=0,display=True):
    if node:
      if display:
        print("%d(%d) " % (node.get(),depth),end="")
      if depth in self.depth: #build depth dict
        self.depth[depth].append(node)
      else:
        self.depth[depth]=[node]
      self.preorder(node.left,depth+1,display)
      self.preorder(node.right,depth+1,display)
   
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
   
  def refresh_depth(self):
    if self.head:
      self.depth = {}
      self.preorder(self.head,depth=0,display=False)
   
  def refresh_depth_arr(self):
    if self.head:
      print("InOrder / LPR...")
      self.inorder(self.head)
      print("\n PreOrder / PLR Refreshing depth array of the Tree...")
      self.preorder(self.head,depth=0)
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
        if n.parent:
          print("%3d(%3d,%2d) " % (n.get(),n.parent.get(),n.h),end="")
        else:
          print("%3d(Non,%2d) " % (n.get(),n.h),end="")

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
   
  #del_vals = [50,10,13,22,85]
  print("\n","-"*10)
  bt.print()
  del_vals = [13,18]
  for v in del_vals:
    bt.del_node(v)
  print("\n","-"*10)
  bt.refresh_depth()
  bt.print()

if __name__ == "__main__":
  execute_test()
