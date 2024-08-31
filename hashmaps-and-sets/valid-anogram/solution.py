'''
an anagram is a word or phrase formed by rearranging the letters of a different word

s = "anagram", t = "nanaram"
Output = True
'''

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    # base case
    if len(s) != len(t):
      return False
    
    # solve using dictionary
    a = {}
    b = {}

    # for each char in s, add it to the 'a' dictionary
    for i in s:
      if i in a:
        a[i] += 1
      else:
        a[i] = 1

    # for each char in t, add it to the 'b' dictionary
    for i in t:
      if i in b:
        b[i] += 1
      else:
        b[i] = 1

    # if our dictionaries are the same, they are
    if a == b:
      return True
    else:
      return False


'''
more easy implementation using a counter
'''
# from collections import Counter

# class Solution:
#   def isAnagram(self, s: str, t: str) -> bool:
#     # base case
#     if len(s) != len(t):
#       return False

#     a_dict = Counter(s)
#     b_dict = Counter(t)

#     return a_dict == b_dict
