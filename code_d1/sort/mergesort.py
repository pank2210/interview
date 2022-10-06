
import sys
import random
import datetime

debug = True

def log(str):
  if debug:
    print(str)

def merge(arr,temp,start,end):
  if start >= end:
    return
   
  log( "start {} end {} temp {}".format(start,end,temp))
  #hold pointer to start and end of bisected array
  leftEnd = int((start+end)/2) 
  left = start
  right = leftEnd + 1
  rightEnd = end
   
  index = left
   
  #log("l {} v {} le {} r {} v {} re {} ".format(left,arr[left],leftEnd,right,arr[right],rightEnd)) 
  log("v {} le {} v {} re {} ".format(arr[left],leftEnd,arr[right],rightEnd)) 
  #iterate both list from left to right extracting minimum from both list to temp
  while left <= leftEnd and right <= rightEnd:
    if arr[left] <= arr[right]:
      temp[index] = arr[left]
      left += 1
    else:
      temp[index] = arr[right]
      right += 1
    index += 1
   
  #log(" l {} r {} index {} temp {} ".format(left,right,index,temp))
   
  #copy remaining elements to end of temo for the list which did not reach end
   
  # copy left, if any
  for i in range(left,leftEnd+1):
      temp[index] = arr[i]
      index += 1 
   
  # copy right, if any
  for i in range(right,rightEnd+1):
      temp[index] = arr[i]
      index += 1 
   
  #update the sorted array to source 
  for i in range(start,rightEnd+1):
    arr[i] = temp[i]
  log(" temp {} ".format(temp))

def mergesort(arr,temp,start,end):
  if start >= end:
    return
  #log("** start {} end {} temp {}".format(start,end,temp))
  middle = int((start +  end) / 2) 
  mergesort(arr,temp,start,middle)
  mergesort(arr,temp,middle+1,end)
  merge(arr,temp,start,end)

def run(arr):
  temp = [0] * len(arr)
  print("input - ",arr)
  mergesort(arr,temp,0,len(arr)-1)
  print("source - ",temp)
  print("sorted - ",temp)

if __name__ == "__main__":
  random.seed(100)
  sample_size = 6
  if len(sys.argv) > 1:
    sample_size = int(sys.argv[1])
  arr = random.sample(range(1,25),k=sample_size)
  run(arr)
