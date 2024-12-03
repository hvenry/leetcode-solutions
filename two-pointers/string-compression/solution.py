"""
Given an array of characters cards, compress it using the following algorithm.

Begin with an empty string s. For each group of consecutive repeading characters in chars:
- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, in the input character array
chars. Note that the group lenghts that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:
chars = ["a", "a", "b", "b", "c", "c", "c"]
returns: 6 and chars = ["a2b2c3"]

Example 2:
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
returns 4, and chars = ["ab12"]

Solution:
- use two pointers to keep track of current char, and how many chars there are after it (read, read_next)
- also keep track of where to write the distance between read, read_next (write)
- iterate through chars moving read, read_next, and updating write whie read is less than n
- key: for cases when we count more than a 1s position of occurrences, we need to iterate through each
       char value of the total count, inserting it into write and updating the write position.
- we can return write which will be the lenght of it, as this will be number of items inserted.

Complexity
- Time: O(n)
- Space: O(1)
"""

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write, n = 0, 0, len(chars)

        # reach every char in chars
        while read < n:
            # move read_next in front of read to see next char
            read_next = read + 1

            # keep reading next while the chars are the same
            while read_next < n and chars[read_next] == chars[read]:
                read_next += 1

            # write the original char at the start from where we are reading from
            chars[write] = chars[read]
            write += 1

            # we convert sequences longer than 1 to string (less than 1 does not get number)
            if read_next - read > 1:
                # convert to string
                count = str(read_next - read)

                # write digits bigger than 1 (read left to right inserting number into chars)
                for char in count:
                    chars[write] = char
                    write += 1

            # move read down to read_next
            read = read_next

        return write
