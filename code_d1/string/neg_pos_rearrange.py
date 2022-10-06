'''
Problem Statement#
Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the left and positive elements appear at the right of the list. Note that it is not necessary to maintain the sorted order of the input list.

Generally zero is NOT positive or negative, we will treat zero as a positive integer for this challenge! So, zero will be placed at the right.
Output#
A list with negative elements at the left and positive elements at the right

Sample Input#
[10,-1,20,4,5,-9,-6]
Sample Output#
[-1,-9,-6,10,20,4,5]

Time complexity = O(n) 
Space complexity = O(const) 
'''

def rearrange(lst):
    # Write your code here
    left = 0
    right = len(lst)-1
    print(lst,end="")
    while left < right:
        while left < right and lst[left] < 0:
            left += 1
        while left < right and lst[right] >= 0:
            right -= 1
        if lst[left] >= 0 and lst[right] < 0:
            tmp = lst[left]
            lst[left] = lst[right]
            lst[right] = tmp
            left += 1
            right -= 1
        #print("***",left,right,lst)
    print(",",lst)
    return lst 


def run_test():
  test_cases = [
    [[-1, 2, -3, -4, 5], [-1, -4, -3, 2, 5]],
    [[300, -1, 3, 0], [-1, 300, 3, 0]],
    [[0, 0, 0, -2], [-2, 0, 0, 0]]
  ]
  for test_case in test_cases:
    res = rearrange(test_case[0])
    if res == test_case[1]:
      print("test_case {} passed".format(test_case))
    else:
      print("test_case {} failed".format(test_case))

if __name__ == "__main__":
  run_test()
