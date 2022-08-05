
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
   
  def traverse(self,node,depth=0):
    if node:
      if node.right:
        self.traverse(node.right,depth+1)
      print(" -%d(%d)- > " % (node.get(),depth),end="")
      if depth in self.depth: #build depth dict
        self.depth[depth].append(node)
      else:
        self.depth[depth]=[node]
      if node.left:
        self.traverse(node.left,depth+1)
   
  def refresh_depth_arr(self):
    print("Refreshing depth array of the Tree...")
    if self.head:
      self.traverse(self.head)
    else:
      print("empty tree")
   
  def print(self):
    for d in sorted(self.depth):
      print("\ndepth[%d]-" % (d))
      for n in self.depth[d]:
        print("%d " % (n.get()),end="")

def execute_test():
  #vals = [ 50, 20, 10, 15, 90, 5, 13]
  vals = [ 50,25,74,12,60,100,6,18,55,65,85,150,3,9,4,14,22,13,16,15,17,22,21,23,80,90,125,175,160]
  
  bt = BT()
  
  for v in vals:
    bt.add(v)
   
  bt.refresh_depth_arr()
  bt.print()
  print("\n","-"*10)

  print("right most child - ",bt.find_right_most_child(bt.head).get()) 
  print("left most child - ",bt.find_left_most_child(bt.head).get())
   
  del_vals = [50,10,13,22,85]
  for v in del_vals:
    bt.del_node(v)

if __name__ == "__main__":
  execute_test()
