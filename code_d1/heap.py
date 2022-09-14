
import sys
import random

debug = True

def log(str,end=None):
  if debug:
    print(str,end=end)

heap = []
size = 20
last = 0
buffer = 10

'''
'''
def swap( index0, index1):
  temp = heap[index0]
  heap[index0] = heap[index1]
  heap[index1] = temp

'''
  bubble up newly added element (last in array) until it gets to min at level
'''
def heapifyup():
  child = last-1
  parent = int((child-1)/2) #this is key formula for getting parent
  while parent >= 0 and heap[child] < heap[parent]:
    log("c {}({}) p {}({}) ".format(heap[child],child,heap[parent],parent),end="")
    swap(child,parent)
    child = parent
    parent = int((child-1)/2) 

'''
  after pop() when zeroth element is removed and last element from array is set as zeroth then push down that first element until min level is reached.
'''
def heapifydown(parent=0):
  left = parent*2+1 #key step to get to left child
  stop = False
  while left < last: #key looping condition, left child exists
    #log(" p {}({}) l {}({}) ".format(heap[parent],parent,heap[left],left))
    smallChildIndex = left #set left child as smaller
     
    #check for right child if smaller then left 
    right = parent*2+2
    if right < last and heap[right] < heap[left]:
      smallChildIndex = right
     
    #swap smaller child if exists or break the loop item is right place
    if heap[parent] > heap[smallChildIndex]:
      swap(parent,smallChildIndex)
      parent = smallChildIndex
      left = parent*2+1
    else:
      break
'''
 pop's first element and replace it with last element from array, reduce array's last/size and finally pushdown new first element to its min level
 pop defaults pull elements as per ascending sort. it is also called as heapsort.
'''
def pop():
  global last 
   
  if last == 0:
    return None
   
  item = heap[0]
  heap[0] = heap[last-1]
  last -= 1
  heapifydown()
  
  return item

'''
  add's new element to end of heap or last and then buble it up as per min level
'''
def push(item):
  global last
   
  if len(heap) >= size:
    log("Error heap full at size[{}]".format(size))
    return False
  log(" adding {} ".format(item))
  heap.append(item)
  last += 1
  heapifyup()
  log(" {}".format(["%d(%d)" % (v,i) for i,v in enumerate(heap)]))

'''
wrapper runner for simulating heap fill up and then its spitting.
'''
def run(arr):
  for item in arr:
    push(item)
  
  while last > 0:
    log(" pop {} last {} ".format(pop(),last))

if __name__ == "__main__":
  samples = 10
  if len(sys.argv) > 1:
    samples = int(sys.argv[1])
  random.seed(100)
  arr = random.sample(range(-samples,samples),k=samples)
  log("arr - {}".format(arr))
  run(arr)
