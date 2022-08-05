import timeit 

class Solution(object):
        
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r_val_dict = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        
        r_allowed_seq = {
            'I': ['X','V'],
            'X': ['C','L'],
            'C': ['D','M']
        }
        ret = 0
        s_len = len(s)
        
        if s_len >= 1 and s_len <= 15:
            r_val_valid_vals = r_val_dict.keys()
            for i in range(0,s_len):
                if s[i] not in r_val_valid_vals:
                    ret = 0
                    break
                else:
                    ret += r_val_dict[s[i]]
                    if i > 0:
                        if r_val_dict[s[i-1]] < r_val_dict[s[i]]:
                            if s[i-1] in r_allowed_seq.keys() and s[i] in r_allowed_seq[s[i-1]]:
                                ret -= r_val_dict[s[i-1]]*2
                            else:
                                print("Error condition not handled, seq[%s%s] invalid, supported seq for [%s] is val[%s]..." % (s[1-1],s[i],s[i-1],r_allowed_seq[s[i-1]]))
                                ret = 0
                                break
        else:
            ret = 0
         
        return ret
     
    def romanToInt_f(self, s: str) -> int:
        ''' faster solution which doesn't require iterating through every element of s (currently faster than 99.49% of submissions'''

        # store all possible conversions
        roman_conversion = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        ret = 0

        # dictionary is ordered, so we find if string contains special cases first
        for k, v in roman_conversion.items():
            if k in s:
                ret += s.count(k) * v
                s = s.replace(k, "")

        return ret
        
def execute_test():
  s = Solution()
   
  tc = {
    '0': {
          'm': "Simple pass I",
          'i': "I",
          'o': int(1)
        },
    '1': {
          'm': "Simple fail empty",
          'i': "",
          'o': int(0)
        },
    '2': {
          'm': "Simple pass MDCLXVI",
          'i': "MDCLXVI", 
          'o': int(1666) 
        },
    '3': {
          'm': "Simple fail invalid char",
          'i': "MDCLPVI",
          'o': int(0)
        },
    '4': {
          'm': "Simple pass IV",
          'i': "IV",
          'o': int(4)
        },
    '5': {
          'm': "Simple pass IX",
          'i': "IX",
          'o': int(9)
        },
    '6': {
          'm': "Simple pass XI",
          'i': "XI",
          'o': int(11)
        },
    '7': {
          'm': "Simple pass MIX",
          'i': "MIX",
          'o': int(1009)
        },
    '8': {
          'm': "Simple pass MXI",
          'i': "MXI",
          'o': int(1011)
        },
    '9': {
          'm': "Simple pass XC",
          'i': "XC",
          'o': int(90)
        },
    '10': {
          'm': "Simple seq fail pass XD",
          'i': "XD",
          'o': int(0)
        },
    '11': {
          'm': "Simple pass CM",
          'i': "CM",
          'o': int(900)
        },
    '12': {
          'm': "Seq incorrect, fail IM",
          'i': "IM",
          'o': int(0)
        },
    '13': {
          'm': "pass, XIX",
          'i': "XIX",
          'o': int(19)
        },
    '14': {
          'm': "Simple pass CD",
          'i': "CD",
          'o': int(400)
        }
  }
  
  for k,v in tc.items():
    print("--- k[%s] v[%s]" % (k,v['m']))
    ret = s.romanToInt(v['i'])
    if ret == v['o']:
      print(" %s passed input[%s] ret[%d] " % (v['m'],v['i'],ret))
    else:
      print("***** %s failed input[%s] ret[%d] expected[%d]" % (v['m'],v['i'],ret,v['o']))


if __name__ == "__main__":
  num = 100
  print(timeit.timeit(execute_test,number=num))
