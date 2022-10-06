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
   
  def add(self,val):
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
   
  def print(self,get=False):
    ret = []
    if self.head:
      node = self.head
      #print(" *head[%s] *tail[%s]" % (self.head.val,self.tail.val))
      while(node):
        print(" %s ->" % (node.get()),end="")
        if get:
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
   
  def remove(self,val):
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
   del_index = 6
   for i in range(len(sample)):
     if not del_index == i:
       expected = [sample[i]] + expected
   pop_ret = list.pop()
   ret = list.print(True) #print the list
   if ret == expected and pop_ret == sample[-1]:
     print("Passed: Test pop passed pop ret[{}] list left[{}]".format(pop_ret,ret))
   else:
     print("Failed: Test pop failed pop ret[{}] expected pop ret[{}] list left[{}] expected list left[{}]".format(pop_ret,sample[-1],ret,expected))
    
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
