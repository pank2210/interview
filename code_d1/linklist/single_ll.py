'''
Single Linked List

1. Single linked list.
2. Should maitain reference to head.
3. Should support push.
4. Should support pop.
5. Should support delete by given key i.e. node value based search and delete. A simple with O(n) complexity is fine.

'''

import random
import string

class Node(object):
  def __init__(self,val):
    self.val = val
    self.next = None
  
  def get(self):
    return self.val
  
  def __eq__(self,node):
    if self.val == node.val:
      return True
    else:
      return False
 
class List(object):
  def __init__(self):
    self.head = None
    #self.tail = None
   
  def insert(self,val):
    self.push(val)
   
  def push(self,val):
    if self.head:
      temp = self.head
      self.head = Node(val)
      self.head.next = temp
    else:
      self.head = Node(val)
      #self.tail = self.head
    #print('**',val,self.head.val)
  
  def traverse(self,pnode,node):
    if node:
      print(" %s ->" % (node.get()),end="")
      return self.traverse(node,node.next)
    else:
      return pnode
      
  def recurse_print(self):
    node = self.traverse(None,self.head)
    print(" recurse_print %s " % (node.get()))
     
    return True    
      
  def print(self):
    ret = []
    if self.head:
      node = self.head
      #print(" *head[%s] *tail[%s]" % (self.head.val,self.tail.val))
      while(node):
        print(" %s ->" % (node.get()),end="")
        ret.append(node.val)     
        node = node.next
    else:
      print("<<List Empty>>")
      
    return ret
  
  def pop(self):
    ret = None
    if self.head: #reset 2nd element as new head and delete existing head
      ret = self.head.val
      temp = self.head
      self.head = self.head.next
      temp = None
    else:
      print("<<List Empty>>")
    return ret
  
  def search_parent(self,node,val):
    ret = None
    while(node):
      if node.next and node.next.val == val:
        ret = node
        break
      node = node.next
    return ret
   
  def delete(self,val):
    if self.head:
      if self.head.val == val:
        self.pop() #delete the head as it matched
      else:
        matched_parent = self.search_parent(self.head,val)
        if matched_parent:
           temp = matched_parent.next #hold matched for cleanup
           matched_parent.next = matched_parent.next.next
           temp = None
        else:
           print("No match in list for [%s]" % (val))
    return self.print()
  
  def create_linklist_from_arr(self,arr):
    for v in arr:
      self.insert(v)

class Test(object):
  def __init__(self):
    self.name = 'Test'
    self.instance = List()
    self.input = None
    
    self.test_config = {
      'print': self.print
      ,'delete': self.delete
      ,'recurse_print': self.recurse_print
    }
  
  def print(self,args):
    input = args[0]
    if self.input != input:
      self.input = input
      self.instance.create_linklist_from_arr(input)
     
    return self.instance.print()
  
  def delete(self,args):
    input = args[0]
    if self.input != input:
      self.input = input
      self.instance.create_linklist_from_arr(input)
     
    return self.instance.delete(args[1])
  
  def recurse_print(self,args):
    input = args[0]
    if self.input != input:
      self.input = input
      self.instance.create_linklist_from_arr(input)
     
    return self.instance.recurse_print()
  
  def run_testcase(self,testcase,args):
    return self.test_config[testcase](args=args)
    

def run_test():
  test_cases = [
    ['print',[[ 200, 25, 75, 125, 300, 12, 35, 60]],[60, 35, 12, 300, 125, 75, 25, 200]]
    ,['delete',[[ 200, 25, 75, 125, 300, 12, 35, 60],125],[60, 35, 12, 300, 75, 25, 200]]
    ,['recurse_print',[[ 200, 25, 75, 125, 300, 12, 35, 60]], True]
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

