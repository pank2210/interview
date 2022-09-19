
import sys
import random 

debug = True
random.seed(100)

def log(str,end=None):
  if debug:
    print(str)

#genrate large random prime number
def get_large_prime_number():
  n = random.randint(1,100)
  return random.randrange( 2**(n-1), 2**n -1)

def polyhash(s,p,x):
  hashcode = 0 
   
  #print(s,p,x) 
  for i in range(len(s)-1,-1,-1):
    hashcode += (hashcode * x + ord(s[i])) % p
   
  return hashcode 

'''
 RabinKarp Algorithm for searching pattern in string
 This is still approximation patch len(Source String)/prime_number probability of mismatch
'''
def rabinkarp(p,s):
  match = []
  prime_num = get_large_prime_number()
  #random_x = random.sample(range(1,prime_num-1),k=1)
  random_x = random.randint(1,prime_num-1)
   
  pHash = polyhash(p,prime_num,random_x) #get hashcode for pattern
   
  for i in range(len(s)-len(p),-1,-1):
    tHash = polyhash(s[i:i+len(p)],prime_num,random_x)
    if tHash == pHash: #match found
      match.append(i)
   
  return match

def run(s,p):
  print(" pattern {} src {}".format(p,s))
  print(" matched offsets {}".format(rabinkarp(p,s)))

'''
 code uses polyhash for substring pattern search.
 if demo of O(n+p) time complexity. n is source string lenght and p len of pattern to be searched.
'''
if __name__ == "__main__":
  s = "AATCGGGTTCAATCGGGGT"
  p = "ATCG" #,"GGGT"]
  if len(sys.argv) > 2:
    s = sys.argv[1]
    p = sys.argv[2]
  run(s,p)
