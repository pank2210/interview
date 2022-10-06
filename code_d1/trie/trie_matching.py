# python3
import sys

from datetime import datetime
import queue

'''
   1. Trie is DS with struct 
      a. has char, data and dict to next chars
      b. end of linked chain have '$' char marking end. 
      c. for source DS last struct will also store offset of match
   2. for both patterns and source string create trie data structure
   3. write match algo that uses pattern trie based searc on source trie.
      usecases to handle in match are
      a. pattern and source trie both reaches end while traversing. this is
         a perfect match at end of source string so return the offset  
      b. source string reaches end. nothing to match or matched failed.
      c. pattern reaches end. navigate trie from that point returning all 
         matching offsets for that pattern.
      d. if none of reaches the end then keep recurssion untill a/b/c is met.
'''

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
    log(" {} -> {} ".format(node.c,k))
    print_trie(next)
  
def get_leaf_data(node,results):
 q = queue.Queue()
 q.put(node)
 #stack = [] 
 #stack.append(node)
 while not q.empty():
    node = q.get()
    #node = stack.pop()
    #'''
    while not node.patternEnd and len(node.next.keys()) == 1:
      k = list(node.next.keys())
      node = node.next[k[0]]
    #'''
    if node.patternEnd:
      #log("-----{} {}-----".format(node.c,node.offset))
      results.append(node.offset)
    for k,next in node.next.items():
      #log(" {} -> {} ".format(node.c,k))
      #get_leaf_data(next,results)
      #stack.append(next)
      q.put(next)

def build_trie_for_patterns(patterns):
  root = Node('\0')
  for pattern_str in patterns:
    nodenext = root.next
    node = root
    #log(" Pattern {} added to trie tree ".format(pattern_str))
    for i in range(len(pattern_str)):
      if pattern_str[i] not in nodenext:
        temp = Node(pattern_str[i])
        nodenext[pattern_str[i]] = temp
        nodenext = temp.next
        node = temp
      else:
        nodenext = nodenext[pattern_str[i]].next
        node = node.next[pattern_str[i]]
      #log("   j {} node {} ".format(j,node.c))
    #at end of string add one end indicator node like $. It helps to seperate multiple string source that shares same prefix substring
    temp = Node('$')
    temp.patternEnd = True
    nodenext['$'] = temp
   
  #print_trie(root) 
  
  return root

def build_trie_for_text(text):
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
  
  return root

def match_patterns(patterns_node,text_node,result):
  #log(" running pattern match with {}".format(patterns))
  if text_node.patternEnd:
    return
  if patterns_node.patternEnd:
    if patterns_node.patternEnd:
      get_leaf_data(text_node,result)
      log(" pattern last char NA  matched and accumulated result is {} ".format(result))
    return
  for c,patterns_next in patterns_node.next.items():
    if patterns_next.patternEnd:
      get_leaf_data(text_node,result)
      #log(" pattern last char NA  matched and accumulated result is {} ".format(result))
      return
    if c in text_node.next:
      #print(" {} -> {} |".format(patterns_node.c,c),end="")
      match_patterns( patterns_next, text_node.next[c],result)

def solve (text, n, patterns):
  result = []
   
  # write your code here
  text_root = build_trie_for_text(text) 
  patterns_root = build_trie_for_patterns(patterns) 
  #print_trie(root) 
  match_patterns(patterns_root,text_root,result)
  
   
  return sorted(list(set(result)))
  #return result

#'''
text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
  patterns += [sys.stdin.readline ().strip ()]
'''
text = "ACATA"
n = 3
patterns = ["AT","A","AG"]
text = "AATCGGGTTCAATCGGGGT"
n = 2
patterns = ["ATCG","GGGT"]
'''
#t1 = datetime.now()
ans = solve (text, n, patterns)
#print("time taken {}".format(datetime.now()-t1))

sys.stdout.write (' '.join (map (str, ans)) + '\n')

