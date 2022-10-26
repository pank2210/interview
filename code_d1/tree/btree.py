'''

Time complexity = O(n) 
Space complexity = O(const) 
'''

class Node(object):
  def __init__(self,v):
    self.v = v
    self.left = None
    self.right = None
   
  def get(self):
    return "-{}".format(self.v)

class BTree(object):
  def __init__(self):
    self.head = None
   
  def search(self,pnode,node,v):
    #print("****",v)
    if not node:
      return (pnode, node)
    else:
      if v == node.v:
        return (pnode,node)
      else:
        if v > node.v:
          return self.search(node,node.right,v)
        else:
          return self.search(node,node.left,v)
   
  def add(self,v):
    #print("***",v)
    if not self.head:
      self.head = Node(v)
    else:
      pnode,node = self.search(None,self.head,v)
      if not node: #node not found so we have lead node here so insert it here
        new_node = Node(v)
        if v > pnode.v:
          pnode.right = new_node
        else:
          pnode.left = new_node
      else: #case of duplicate value, so error out
        print("value {} is duplicate at p[{}] c[{}] so eliminating the insert.".format(v,pnode.v,node.v))
   
  def create_tree_from_arr(self,arr):
    for v in arr:
      self.add(v)
  
  def inorder(self,node,ret):
    if node:
      self.inorder(node.left,ret)
      print(node.get(),end="")
      ret.append(node.v)
      self.inorder(node.right,ret)
  
  def preorder(self,node,ret=None):
    if node:
      print(node.get(),end="")
      ret.append(node.v)
      self.preorder(node.left,ret)
      self.preorder(node.right,ret)
  
  def postorder(self,node,ret=None):
    if node:
      self.postorder(node.left,ret)
      self.postorder(node.right,ret)
      print(node.get(),end="")
      ret.append(node.v)
  
  def po_traverse(self,node,ret=None,sum=0):
    if node:
      lval = self.postorder(node.left,ret)
      rval = self.postorder(node.right,ret)
      print("*{},{},{}".format(node.v,lval,rval),end="")
      ret.append(node.v)
      return lval+rval+node.v
      #return node.v
    else:
      return 0
  
  def print(self,order='inorder'):
    ret = []
    if order == 'inorder':
      self.inorder(self.head,ret)
    elif order == 'preorder':
      self.preorder(self.head,ret)
    elif order == 'postorder':
      self.postorder(self.head,ret)
    elif True:
      self.preorder(self.head,ret)
     
    return ret

class Test(object):
  def __init__(self):
    self.name = 'Test'
    self.bt = BTree()
    self.input = None
    
    self.test_config = {
      'inorder': self.inorder,
      'preorder': self.preorder,
      'postorder': self.postorder
    }
  
  def inorder(self,args):
    input = args[0]
    if self.input != input:
      self.input = input
      self.bt.create_tree_from_arr(input)
     
    return self.bt.print(order='inorder')
  
  def preorder(self,args):
    input = args[0]
    if self.input != input:
      self.input = input
      self.bt.create_tree_from_arr(input)
     
    return self.bt.print(order='preorder')
  
  def postorder(self,args):
    input = args[0]
    if self.input != input:
      self.input = input
      self.bt.create_tree_from_arr(input)
     
    return self.bt.print(order='postorder')
  
  def run_testcase(self,testcase,args):
    return self.test_config[testcase](args=args)
    

def run_test():
  test_cases = [
    ['inorder',[[100, 50, 200, 25, 75, 125, 300, 12, 35, 60]],[12, 25, 35, 50, 60, 75, 100, 125, 200, 300]],
    ['preorder',[[100, 50, 200, 25, 75, 125, 300, 12, 35, 60]],[100, 50, 25, 12, 35, 75, 60, 200, 125, 300]],
    ['postorder',[[100, 50, 200, 25, 75, 125, 300, 12, 35, 60]],[12, 35, 25, 60, 75, 50, 125, 300, 200, 100]]
  ]
   
  test = Test()
  for test_case in test_cases:
    res = test.run_testcase(test_case[0],test_case[1])
    if res == test_case[2]:
      print("test_case {} passed".format(test_case))
    else:
      print("test_case {} failed. res {}".format(test_case,res))

if __name__ == "__main__":
  run_test()
