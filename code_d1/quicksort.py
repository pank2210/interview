
import sys
import random
import datetime

debug = True

def log(str):
  if debug:
    print(str)

def quick(arr,temp,start,end):
  if start >= end:
    return
  log( "start {} end {} temp {}".format(start,end,temp))
  leftEnd = int((start+end)/2) 
  left = start
  right = leftEnd + 1
  rightEnd = end
  index = left
  #log("l {} v {} le {} r {} v {} re {} ".format(left,arr[left],leftEnd,right,arr[right],rightEnd)) 
  log("v {} le {} v {} re {} ".format(arr[left],leftEnd,arr[right],rightEnd)) 
  while left <= leftEnd and right <= rightEnd:
    if arr[left] <= arr[right]:
      temp[index] = arr[left]
      left += 1
    else:
      temp[index] = arr[right]
      right += 1
    index += 1
  #log(" l {} r {} index {} temp {} ".format(left,right,index,temp))
  for i in range(left,leftEnd+1):
      temp[index] = arr[i]
      index += 1 
  for i in range(right,rightEnd+1):
      temp[index] = arr[i]
      index += 1 
  for i in range(start,rightEnd+1):
    arr[i] = temp[i]
  log(" temp {} ".format(temp))

def swap(l,r,arr):
  temp = arr[l]
  arr[l] = arr[r]
  arr[r] = temp

def quicksort(arr,start,end):
  if start >= end:
    return
  left = start
  right = end
  '''
  pivot = int((start+end)/2)
  log("** start {} pivot {} end {} arr {}".format(start,pivot,end,arr))
  log(" {} {} {} ".format(arr[left],arr[pivot],arr[right]))
  while left < right:
    if arr[left] >= arr[pivot] and arr[right] < arr[pivot]:
        swap(left,right,arr)
        right -= 1
        left += 1
    else: 
      if arr[left] < arr[pivot]:
        left += 1 
      if arr[right] >= arr[pivot]:
        right -= 1
  '''
  pivot = arr[int((start+end)/2)]
  log("** start {} pivot {} end {} arr {}".format(start,pivot,end,arr[start:end]))
  log(" {} {} {} ".format(arr[left],pivot,arr[right]))
  while left <= right:
    if arr[left] >= pivot and arr[right] <= pivot:
        swap(left,right,arr)
        right -= 1
        left += 1
    else: 
      if arr[left] < pivot:
        left += 1 
      if arr[right] > pivot:
        right -= 1
    log("****** l {} v {} r {} v {} arr {}".format(left,arr[left],right,arr[right],arr[start:end]))
  if left > right:
    left -= 1
  if left < 0:
    left = 0
  quicksort(arr,start,left)
  quicksort(arr,left+1,end)

def run(arr):
  print("input - ",arr)
  end = len(arr)-1
  quicksort(arr,0,end)
  print("sorted - ",arr)

if __name__ == "__main__":
  random.seed(100)
  sample_size = 6
  if len(sys.argv) > 1:
    sample_size = int(sys.argv[1])
  arr = random.sample(range(1,sample_size+25),k=sample_size)
  run(arr)
