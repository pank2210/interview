#Uses python3
import sys

debug = False
#debug = True

def log(str):
  if debug:
    print(str)

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    # write your code here
    class Node:
      def __init__(self,c,id):
        self.c = c
        self.id = id
        self.children = {}
     
    str = patterns
    #str = patterns.split() 
    #str = str[1:]
    log(" Processing - {} ".format(str))
    counter = 0
    tree[counter] = {}
     
    for s in str: 
      #log(" s - {}".format(s))
      node = tree[0]
      for i in range(len(s)):
        #if counter not in node:
        #  node[counter] = {}
        if s[i] not in node: 
          counter += 1
          node[s[i]] = counter
          if counter not in tree:
            tree[counter] = {}
            node = tree[counter] 
        else:
          node = tree[node[s[i]]] 
        #log(" i {} counter {} s[i] {} {}".format(i,counter,s[i],node[counter-1]))
        log(" i {} counter {} s[i] {} {}".format(i,counter,s[i],node))
     
    return tree

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    #patterns = "3\nAT\nAG\nAC"
    #patterns = "3\nATAGA\nATC\nGAT"
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

