
'''
Problem Statement#
Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.

Input:#
A list of numbers (could be floating points or integers)

Output:#
A list such that each index has a product of all the numbers in the list except the number stored at that index.

Sample Input#
arr = [1,2,3,4]
Sample Output#
arr = [24,12,8,6]

Time complexity is O(n)
Space complexity is O(n)
'''

def find_product(lst):
    # Write your code here
    lst_prod = 1
    zero_ind = 0

    for ind,i in enumerate(lst):
        if i == 0:
            if zero_ind > 0:
                zero_ind += 1
            else:
                zero_ind = 1
        else:
            lst_prod *= i
                
    print("***",lst,lst_prod,zero_ind,end="")

    for ind,i in enumerate(lst):
        if i != 0:
            if zero_ind > 0:
                lst[ind] = 0
            else:
                lst[ind] = lst_prod / i
        else:
            if zero_ind > 1:
                lst[ind] = 0
            else:
                lst[ind] = lst_prod
    print(lst)

    return lst

def run_test():
  test_cases = [
     [[1, 2, 3, 4],[24.0, 12.0, 8.0, 6.0]],
     [[2, 5, 9, 3, 6],[810.0, 324.0, 180.0, 540.0, 270.0]],
     [[0, 1, 10, 100] ,[1000, 0, 0, 0]],
     [[0, 2, 9, 0, 12, 25] ,[0, 0, 0, 0, 0, 0]]
  ]
  for test_case in test_cases:
    res = find_product(test_case[0])
    if res == test_case[1]:
      print("test_case {} passed".format(test_case[0]))
    else:
      print("test_case {} failed".format(test_case[0]))

if __name__ == "__main__":
  run_test()
