'''
Double Linked List

1. Double linked list.
2. Should maitain reference to head and tail. Tail is is reuqired to implemente Queue.
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
    self.prev = None
  
  def set_next(self,node):
    self.next = node
  
  def set_prev(self,node):
    self.prev = node
  
  def get(self):
    return self.val
   
  def print(self,msg=None):
    prev = None
    next = None
    if self.next:
      next = self.next.val
    if self.prev:
      prev = self.prev.val
    print("-"*10,msg,"-"*10)
    print("[%s]<=>[%s]<=>[%s]" % (prev,self.val,next))
  
  def __eq__(self,node):
    if self.val == node.val:
      return True
    else:
      return False
 
class List(object):
  def __init__(self):
    self.head = None
    self.tail = None
   
  def add(self,val):
    self.push(val)
   
  def push(self,val):
    if self.head:
      ''' Looks logically correct but last assignement corrupts something.
      temp = Node(val)
      temp.set_prev(None)
      temp.set_next(self.head)
      self.head.set_prev(temp)
      self.head = temp
      '''
       
      #below logic works properly...Key is that existing object reference needs to be preserve before introduction new values
      temp = self.head
      self.head = Node(val)
      self.head.set_prev(None)
      self.head.set_next(temp)
      temp.set_prev(self.head)
      
      #self.head.print("head")
      #temp.print("temp")
    else:
      self.head = Node(val)
      self.tail = self.head
   
  def print(self,get=False):
    ret = []
    if self.head:
      node = self.head
      #self.head.print("head")
      #self.tail.print("tail")
      while(node):
        print(" %s <=>" % (node.get()),end="")
        if get:
          ret.append(node.val)     
        node = node.next
    else:
      print("<<List Empty>>")
      
    return ret
  
  def pop(self):
    ret = None
    #self.tail.print("probe tail")
    #self.tail.prev.print("probe tail prev")
    if self.tail: #reset 2nd element as new head and delete existing head
      pop_node = self.tail #hold reference to the cleanup
      ret = pop_node.val #get value to return or one to pop
      if self.tail == self.head: #Special case, #If we only one node then 
        self.head = None
        return ret
      self.tail = self.tail.prev #update the tail
      self.tail.next = None #set proper end point
      pop_node = None #cleanup
      #self.tail.print("new tail")
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
   
  def remove(self,val):
    if self.head:
      if self.head.val == val:
        self.pop() #delete the head as it matched
      else:
        matched_parent = self.search_parent(self.head,val)
        if matched_parent:
           temp = matched_parent.next #hold matched for cleanup
           #matched_parent.print("matched parent")
           #temp.print("matched node")
           if not temp.next: #Special case, when matched node is the last node.
             matched_parent.next = None
           else:
             #next_of_matched.print("next of matched node")
             next_of_matched = temp.next
             matched_parent.next = next_of_matched
             next_of_matched.prev = matched_parent
           #cleanup
           temp = None
        else:
           print("No match in list for [%s]" % (val))

def execute_test():
   random.seed(100) #set fix seed
   
   #genrate sample test data
   sample = random.sample( string.digits, k=7)
   print(" Input Sample - ",sample)
   
   #create test data sample List
   def create_test_sample_list(_sample=None):
     list = List()
     if _sample: #check if usecase specific sample has been passed. 
       test_data = _sample
     else:
       test_data = sample
     for i in range(len(test_data)):
       list.push(test_data[i])
     return list
    
   #test the list
   list = create_test_sample_list()
   ret = list.print(True) #print the list
   expected = []
   for i in range(len(sample)):
     expected = [sample[i]] + expected
   if ret == expected:
     print("Passed: Simple test passed input[{}] output[{}]".format(sample,ret))
   else:
     print("Failed: Simple test failed input[{}] output[{}] expected[{}]".format(sample,ret,expected))
    
   #test the pop
   list = create_test_sample_list()
   expected = []
   del_index = 0
   for i in range(len(sample)):
     if not del_index == i:
       expected = [sample[i]] + expected
   pop_ret = list.pop()
   ret = list.print(True) #print the list
   if ret == expected and pop_ret == sample[del_index]:
     print("Passed: Test pop passed pop ret[{}] list left[{}]".format(pop_ret,ret))
   else:
     print("Failed: Test pop failed pop ret[{}] expected pop ret[{}] list left[{}] expected list left[{}]".format(pop_ret,sample[del_index],ret,expected))
    
   #test the pop, boundary case. list had only one node
   test_data = 10
   list = create_test_sample_list([test_data])
   expected = []
   pop_ret = list.pop()
   ret = list.print(True) #print the list
   if ret == expected and pop_ret == test_data:
     print("Passed: Pop when only one node test passed pop ret[{}] list left[{}]".format(pop_ret,ret))
   else:
     print("Failed: Pop when only one node test failed pop ret[{}] expected pop ret[{}] list left[{}] expected list left[{}]".format(pop_ret,test_data,ret,expected))
    
   #test the delete case1
   list = create_test_sample_list()
   expected = []
   del_index = 3
   for i in range(len(sample)):
     if not del_index == i:
       expected = [sample[i]] + expected
   list.remove(sample[del_index])
   ret = list.print(True) #print the list
   if ret == expected:
     print("Passed: Random value find and delete test passed deleted[{}] list left[{}]".format(sample[del_index],ret))
   else:
     print("Failed: Random value find and delete test failed delete [{}] failed list left[{}] expected list left[{}]".format(sample[del_index],ret,expected))
    
   #test the delete case2
   list = create_test_sample_list()
   expected = []
   del_index = 0
   for i in range(len(sample)):
     if not del_index == i:
       expected = [sample[i]] + expected
   list.remove(sample[del_index])
   ret = list.print(True) #print the list
   if ret == expected:
     print("Passed: Delete value that is at the end test passed deleted[{}] list left[{}]".format(sample[del_index],ret))
   else:
     print("Failed: Delete value that is at the end test failed delete [{}] failed list left[{}] expected list left[{}]".format(sample[del_index],ret,expected))

if __name__ == "__main__":
   execute_test()
