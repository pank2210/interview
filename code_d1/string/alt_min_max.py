'''
Problem Statement#
Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such that the 0th index will have the largest number, the 1st index will have the smallest, and the 2nd index will have second-largest, and so on. In other words, all the even-numbered indices will have the largest numbers in the list in descending order and the odd-numbered indices will have the smallest numbers in ascending order.

Input:#
A sorted list

Output:#
A list with elements stored in max/min form

Sample Input#
lst = [1,2,3,4,5]
Sample Output#
lst = [5,1,4,2,3]


Time complexity = O(n/2) 
Space complexity = O(const)
'''

def max_min(lst):
    # Write your code here
    min_ind = 0
    max_ind = len(lst)-1
    res_arr = []

    if len(lst) < 2:
        return lst

    print(lst,end="")
    ''' solution with Space complexity O(n)
    while min_ind < max_ind:
        res_arr.append(lst[max_ind])
        res_arr.append(lst[min_ind])
        max_ind -= 1
        min_ind += 1
    
    if len(lst) % 2 != 0:
        res_arr.append(lst[min_ind])
    '''

    #time complexity O(n/2) and space complexity O(const)
    last = len(lst)-1
    left = 0
    till_ind = int(len(lst)/2) + 1
    left_swap = True
    #print("*",left,till_ind,last)
    #'''
    while left < till_ind:
        #print("*",left,left_swap,lst)
        if left_swap:
            tmp = lst[last]
            lst[last] = lst[left]
            lst[left] = tmp
            if left:
              left_swap = False
            left += 1
        else:
            #print("-----",lst[last-1],lst[last],lst)
            tmp = lst[last]
            lst[last] = lst[last-1]
            lst[last-1] = tmp
            left_swap = True
            #print("-----",lst[last-1],lst[last],lst)
        #right -= 1
        #left += 1
    #'''
    print(",",lst)    

    #return res_arr
    return lst


def run_test():
  test_cases = [
     [[1, 2, 3, 4, 5, 6, 7], [7, 1, 6, 2, 5, 3, 4]],
     [[1, 2, 3, 4, 5], [5, 1, 4, 2, 3]],
     [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],
     [[-10, -1, 1, 1, 1, 1], [1, -10, 1, -1, 1, 1]]
  ]
  for test_case in test_cases:
    res = max_min(test_case[0])
    if res == test_case[1]:
      print("test_case {} passed".format(test_case[0]))
    else:
      print("test_case {} failed".format(test_case[0]))

if __name__ == "__main__":
  run_test()
