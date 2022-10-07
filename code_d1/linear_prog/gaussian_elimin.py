'''
'''

import numpy as np

class GElimin(object):
  def __init__(self):
    pass 
   
  def gaussian_elimin(self,a,b):
    n = len(b)
    
    ''' 
    print("-"*15)
    for i in range(0,n):
      print(" {}th row of a,b is {} | {}".format(i,a[i],b[i]))
    print("-"*15)
     
    #elimination 
    print("Elimination")
    print("-"*15)
    ''' 
    for i in range(0,n-1):
      for j in range(i+1,n):
        if a[j,i] != 0.:
          lam = a[j,i]/a[i,i]
          #a[j,i+1:n] = a[j,i+1:n] - lam * a[i,i+1:n]
          a[j,i:n] = a[j,i:n] - lam * a[i,i:n]
          b[j] = b[j] - lam * b[i]
        #print("{}th row of a,b is {} | {}".format(j,a[j],b[j]))
    
    ''' 
    print("-"*15)
    for i in range(0,n):
      print(" {}th row of a,b is {} | {}".format(i,a[i],b[i]))
    print("-"*15)
     
    print("-"*15)
    print("Subsitution")
    print("-"*15)
    ''' 
    #subsitution 
    for i in range(n-1,-1,-1):
    #for i in range(n,-1,-1):
      a1 = a[i,i+1:n]
      b1 = b[i+1:n]
      aii = a[i,i]
      #print("( {} - np.dot( {} , {} )) / {}".format(b[i],a1,b1,aii))
      b[i] = (b[i] - np.dot(a1,b1))/aii
     
    ''' 
    print("-"*15)
    print("Final b is {} ".format(b))
    print("-"*15)
    ''' 
    
    return b

class Test(object):
  def __init__(self):
    self.name = 'Test'
    self.instance = GElimin()
    self.input = None
    
    self.test_config = {
      'gaussian_elimin': self.gaussian_elimin
    }
  
  def gaussian_elimin(self,args):
    '''
    input = args[0]
    if not self.input:
      self.input = input
      #self.instance.create_linklist_from_arr(input)
    '''
     
    return self.instance.gaussian_elimin(args[0],args[1])
  
  def run_testcase(self,testcase,args):
    return self.test_config[testcase](args=args)
    

def run_test():
  test_cases = [
    [ 'gaussian_elimin' \
      ,[ np.array( \
         [ [4.,-2.,1.] \
          ,[-2.,4.,-2.] \
          ,[1.,-2.,4.] \
         ]) \
      ,np.array( \
          [11.,-16.,17.] \
         )] \
      , np.array([1.,-2.,3.]) ]
    ,[ 'gaussian_elimin' \
      ,[ np.array( \
         [ [1.,1.,-1.] \
          ,[2.,-1.,1.] \
          ,[-1.,2.,2.] \
         ]) \
      ,np.array( \
          [-2.,5.,1.] \
         )] \
      , np.array([1.,-1.,2.]) ]
    ]
   
  test = Test()
  for test_case in test_cases:
    res = test.run_testcase(test_case[0],test_case[1])
    if (res == test_case[2]).all():
      print("test_case {} passed".format(test_case))
    else:
      print("test_case {} failed. res {}".format(test_case,res))

if __name__ == "__main__":
  run_test()

