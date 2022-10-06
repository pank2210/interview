# python3
import sys

NA = -1

debug=False
#debug=True

def log(str):
  if debug:
    print(str)

class Node:
  def __init__ (self,c):
    self.c = c
    self.next = {}
    self.patternEnd = False
    self.offset = None
  
def print_trie(node):
  if node.patternEnd:
    log("-----{} {}-----".format(node.c,node.offset))
    return
  for k,next in node.next.items():
    #log(" {} -> {} ".format(node.c,k))
    print_trie(next)
  
def get_leaf_data(node,results):
 stack = [] 
 stack.append(node)
 while stack:
    node = stack.pop()
    while not node.patternEnd and len(node.next.keys()) == 1:
      k = list(node.next.keys())
      node = node.next[k[0]]
    if node.patternEnd:
      #log("-----{} {}-----".format(node.c,node.offset))
      results.append(node.offset)
    for k,next in node.next.items():
      #log(" {} -> {} ".format(node.c,k))
      #get_leaf_data(next,results)
      stack.append(next)

def solve (text, n, patterns):
  result = []
   
  # write your code here
  root = Node('\0')
  for i in range(len(text)):
    nodenext = root.next
    node = root
    #log(" i {} str {} ".format(i,text[i:]))
    for j in range(len(text[i:])):
      if text[i+j] not in nodenext:
        temp = Node(text[i+j])
        nodenext[text[i+j]] = temp
        nodenext = temp.next
        node = temp
      else:
        nodenext = nodenext[text[i+j]].next
        node = node.next[text[i+j]]
      #log("   j {} node {} ".format(j,node.c))
    #at end of string add one end indicator node like $. It helps to seperate multiple string source that shares same prefix substring
    temp = Node('$')
    temp.patternEnd = True
    temp.offset = i
    nodenext['$'] = temp
    #print_trie(root) 
   
  #print_trie(root) 
  
  log(" running pattern match with {}".format(patterns))
  for str in patterns:
    node = root
    no_match = False
    str_pattern_search_result = []
    for i in range(len(str)):
      if str[i] in node.next:
        node = node.next[str[i]]
      else:
        no_match = True
        break
    if no_match:
      log(" pattern matched failed for {}".format(str))
    else:
      get_leaf_data(node,str_pattern_search_result)
      log(" pattern {} matched and leaf data is {} ".format(str,str_pattern_search_result))
      result += str_pattern_search_result
   
  return sorted(list(set(result)))

#'''
text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
  patterns += [sys.stdin.readline ().strip ()]
'''
text = "AATCGGGTTCAATCGGGGT"
n = 2
patterns = ["ATCG","GGGT"]
text = "ACATA"
n = 3
patterns = ["AT","A","AG"]
'''

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')

