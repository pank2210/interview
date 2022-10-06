'''
Problem statement#
Given an integer list, return the maximum sublist sum. The list may contain both positive and negative integers and is unsorted.

Partial function definition#
def find_max_sum_sublist(lst):
  pass
Input#
a list lst
Output#
a number (maximum subarray sum)

Sample input#
[-4, 2, -5, 1, 2, 3, 6, -5, 1]

Sample output#
largest_sum = 12

Time complexity = O(n) 
Space complexity = O(const) 
'''
def find_max_sum_sublist(lst): 
  # Write your code here!
  if len(lst) < 2:
    return lst
  print(lst,end="")
  start = len(lst)-1
  end = start + 1
  sub_lst_sum = {}
  max = float('-inf')
  max_ind = (start,end)
  while start >= 0:
    sum_at_ind = sum(lst[start:end])
    if sum_at_ind > max:
      max = sum(lst[start:end])
      max_ind = (start,end)
    if sum_at_ind <= 0:
      end = start
    #print("*",lst[start:end],max,lst[max_ind[0]:max_ind[1]])
    start -= 1
  #print(",",lst[max_ind[0]:max_ind[1]])
  print(",",max)
  
  return max

def run_test():
  test_cases = [
    [[9, -10, 8, 3, -6, -3, 6],11],
    [[-4, 2, -5, 1, 2, 3, 6, -5, 1], 12],
  ]
  for test_case in test_cases:
    res = find_max_sum_sublist(test_case[0])
    if res == test_case[1]:
      print("test_case {} passed".format(test_case))
    else:
      print("test_case {} failed. res {}".format(test_case,res))

if __name__ == "__main__":
  run_test()
