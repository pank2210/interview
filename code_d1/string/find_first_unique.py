'''
Problem Statement#
Implement a function, find_first_unique(lst) that returns the first unique integer in the list.

Input#
A list of integers

Output#
The first unique element in the list

Sample Input#
[9,2,3,2,6,6]
Sample Output#
9

Time complexity = O(n+u) # u are #unique keys
Space complexity = O(u * const) 
'''

def find_first_unique(lst):
    # Write your code here
    val_dict = {}
    for i in range(len(lst)):
        if lst[i] in val_dict:
            val_dict[lst[i]]['r'] = True
        else:
            i_dict = {}
            i_dict['r'] = False
            i_dict['ind'] = i
            val_dict[lst[i]] = i_dict

    min_non_repeat_ind = len(lst)
    for k,v in val_dict.items():
        if not v['r']:
            if v['ind'] < min_non_repeat_ind:
                min_non_repeat_ind = v['ind']

    #print(lst,val_dict,min_non_repeat_ind,lst[min_non_repeat_ind])
    print(lst,lst[min_non_repeat_ind])

    return lst[min_non_repeat_ind]

def run_test():
  test_cases = [
    [[9, 2, 3, 2, 6, 6],9],
    [[4, 5, 1, 2, 0, 4],5]
  ]
  for test_case in test_cases:
    res = find_first_unique(test_case[0])
    if res == test_case[1]:
      print("test_case {} passed".format(test_case[0]))
    else:
      print("test_case {} failed".format(test_case[0]))

if __name__ == "__main__":
  run_test()
