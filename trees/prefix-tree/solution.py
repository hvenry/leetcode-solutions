"""
A trie (pronounced as "try") or PREFIX TREE is a tree data structure used
to efficiently store and retrieve keys in a dataset of strings. There are various
applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() --> initializes the trie object

- void insert(String word) --> inserts the string word into the tree

- boolean search(String word) --> Returns true if the string word is in the trie,
  (ie, was inserted before), and false otherwise

- boolean startsWith(String prefix) --> returns true if there is a previously inserted
  string word that has the prefix prefix, and false otherwise.


Examples:
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]

[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Output:
[null, null, true, false, true, null, true]

Explanation:
Trie trie = new Trie(); -> null
trie.insert("apple"); -> null
trie.search("apple"); -> true
trie.search("app");  -> false
trie.startsZWith("app"); -> true
trie.insert("app"); -> null
trie.search("app"); -> true

Solution:
The idea here is to store strings in a tree structure as individual chars in order.
- For other strings that overlap, we want them to share the path and branch out as soon as they are different.

Example:
Storing app:

        root
    a
    p
    p
    .

Storing apple:


        root
    a
    |
    p
    |
    p
   /|
  l .
  |
  e
  |
  .


def __init__(self):
- store valus in trie like above
  - we can do this with nested dictionaries

def insert(self, word):
- store values that differ from any original strings

def search(self, word: str) -> bool:
- follow the path and see if you can reach a . when you are finished writing the str

def startsWith(self, prefix: str) -> bool:
- follow the path until you complete the prefix, return True if that is the case, false otherwise


How to store with nested dictionaries:
example:

insert(bin):

{ b: { i : { n : { . : . } } }

now, insert(bind):


{ b: { i : { n : { . : . ,
                   d : { . : .}
                 } } }
"""


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        dict = self.trie

        for char in word:
            # we have not seen char yet, we create a new spot
            if char not in dict:
                dict[char] = {}

            # we have already seen the char, so we nest further
            dict = dict[char]

        # now we mark the ending of the word
        dict["."] = "."

    def search(self, word: str) -> bool:
        dict = self.trie

        for char in word:
            if char not in dict:
                return False

            # if char is in word
            dict = dict[char]

        # make sure that we are at an end (there is a period stored at the current level)
        return "." in dict

    def startsWith(self, prefix: str) -> bool:
        dict = self.trie

        for char in prefix:
            if char not in dict:
                return False
            dict = dict[char]

        return True
