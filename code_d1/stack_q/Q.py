'''
  1. stack is LIFO implemtation using array.
  2. Limit elements to particular limit i.e. capacity
  3. Implement using array by keeping cursor maintained for top item in queue.
  4. put new item in queue only is queue has capacity
  5. empty queue returns none
'''

import random

Q_CAPACITY = 100

class Q(object):
  def __init__(self,q_capacity=None):
    if q_capacity and q_capacity > 0:
      self.q_capacity = q_capacity
    else:
      self.q_capacity = Q_CAPACITY
    self.q = []
    self.top = 0
    print("queue created with capacity of [%d] and top set to [%d]" % (self.q_capacity,self.top))
  
  def put(self,item):
    if item: 
      if self.top < self.q_capacity:
        self.q.append(item)
        self.top = len(self.q)
      else:
        print("Error: queue is full, put failed")
    else:
      print("Error: item passed to queue is null")
      
  def get(self):
    if not len(self.q):
      return None #nothing to return
    else:
      item = self.q.pop()
      self.top = len(self.q)
      
      return item

def execute_test():
  random.seed(100)
  sample = random.sample(range(1,100),10)
  print("sample test data - ",sample)
  
  q = Q()
  for i in range(len(sample)):
    q.put(sample[i])
  dequeue_till = 4
  expected = []
  res = []
  for i in range(len(sample)-1,len(sample)-dequeue_till,-1):
    #print("****i={}*****",i)
    expected.append(sample[i])
    res.append(q.get())
  test_msg = "input[{}] dequeue till [{}] res[{}] expected[{}]".format(sample,dequeue_till,res,expected)
  if res == expected:
    print("Simple queue test passed. %s" % (test_msg))
  else:
    print("Simple queue test failed. %s" % (test_msg))
  

if __name__ == "__main__":
  execute_test()

