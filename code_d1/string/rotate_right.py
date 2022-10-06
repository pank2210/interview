'''

Time complexity = O(n) 
Space complexity = O(k) #k is #rotate elements
'''
def right_rotate(lst, k):
    # Write your code here
    if k >= len(lst):
        return lst
    k_to_rotate = lst[-k:]
    print(lst,end="")
    i = len(lst)
    #print(lst,k,i)
    while i >= k:
        #print("***",k,i-1,i-k,lst[i-1],lst[i-k-1])
        lst[i-1] = lst[i-k-1]
        i -= 1
    for i in range(k):
        lst[i] = k_to_rotate[i]
    #print(",",lst,k,k_to_rotate)
    print(",",lst)

    return lst

def right_rotate2(lst,k):
  return lst[len(lst)-k:] + lst[:len(lst)-k]

def run_test():
  test_cases = [
     [[1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]],
     [[300, -1, 3, 0], 3, [-1, 3, 0, 300]],
     [[0, 0, 0, 2], 2, [0, 2, 0, 0]]
  ]
  for test_case in test_cases:
    #res = right_rotate(test_case[0],test_case[1])
    res = right_rotate2(test_case[0],test_case[1])
    if res == test_case[2]:
      print("test_case {} passed, res {}".format(test_case,res))
    else:
      print("test_case {} failed, res {}".format(test_case,res))

if __name__ == "__main__":
  run_test()
