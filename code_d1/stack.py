'''
  1. stack is LIFO implemtation using array.
  2. Limit elements to particular limit i.e. capacity
  3. Implement using array by keeping cursor maintained for top item in stack.
  4. put new item in stack only is stack has capacity
  5. empty stack returns none
'''

import random

STACK_CAPACITY = 100

class Stack(object):
  def __init__(self,s_capacity=None):
    if s_capacity and s_capacity > 0:
      self.s_capacity = s_capacity
    else:
      self.s_capacity = STACK_CAPACITY
    self.s = []
    self.top = 0
    print("stack created with capacity of [%d] and top set to [%d]" % (self.s_capacity,self.top))
  
  def put(self,item):
    if item: 
      if self.top < self.s_capacity:
        self.s.append(item)
        self.top = len(self.s)
      else:
        print("Error: stack is full, put failed")
    else:
      print("Error: item passed to stack is null")
      
  def get(self):
    if not len(self.s):
      return None #nothing to return
    else:
      item = self.s.pop()
      self.top = len(self.s)
      
      return item

def execute_test():
  random.seed(100)
  sample = random.sample(range(1,100),10)
  print("sample test data - ",sample)
  
  s = Stack()
  for i in range(len(sample)):
    s.put(sample[i])
  destack_till = 4
  expected = []
  res = []
  for i in range(len(sample)-1,len(sample)-destack_till,-1):
    #print("****i={}*****",i)
    expected.append(sample[i])
    res.append(s.get())
  test_msg = "input[{}] destack till [{}] res[{}] expected[{}]".format(sample,destack_till,res,expected)
  if res == expected:
    print("Simple stack test passed. %s" % (test_msg))
  else:
    print("Simple stack test failed. %s" % (test_msg))
  

if __name__ == "__main__":
  execute_test()

