'''
Problem Statement#
Implement a function find_second_maximum(lst) which returns the second largest element in the list.

Input:#
A List

Output:#
Second largest element in the list

Sample Input#
[9,2,3,6]
Sample Output#
6

Time complexity = O(n) 
Space complexity = O(const) 
'''

def find_second_max(lst):
   if (len(lst) < 2):
       return
   # initialize the two to infinity
   max_no = second_max_no = float('-inf')
   for i in range(len(lst)):
       # update the max_no if max_no value found
       if (lst[i] > max_no):
           second_max_no = max_no
           max_no = lst[i]
       # check if it is the second_max_no and not equal to max_no
       elif (lst[i] > second_max_no and lst[i] != max_no):
           second_max_no = lst[i]
   print(lst,second_max_no)
   if (second_max_no == float('-inf')):
       return
   else:
       return second_max_no

def run_test():
  test_cases = [
    [[9, 2, 3, 2, 4, 6],6],
    [[4, 5, 1, 2, 0, 4],4]
  ]
  for test_case in test_cases:
    res = find_second_max(test_case[0])
    if res == test_case[1]:
      print("test_case {} passed".format(test_case[0]))
    else:
      print("test_case {} failed".format(test_case[0]))

if __name__ == "__main__":
  run_test()
