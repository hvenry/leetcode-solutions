"""
You are given a string s and an integer k. You can choose any character of
the string and change it to any other upppercase English character. You can
perform this operation at most k times.

Return the length of the longest substring containing the same letter you can
get after performing the above operations.

example 1:
s = "ABAB"
k = 2

returns 4

this is because k - 1 for changing s[1] and k - 1 again for changing s[3] to A's
gets you the string "AAAA", which is 4 and the longest substring containing the same letter.


solution:
- sliding window approach
- increase count of seen char by incrementing index (0 - 26 representing A - Z).
- continue until the window is invalid
- while the window is invald, move the left pointer until it is valid
    Invalid condition: window lenght - most frequent character > k, meaning we cannot fix the window with our k switches
- once window is valid again, we can change longest to the maximum of previous longest, or our window lenght.
- finally, we can return lognest, as it will contain the longest valid window lenght

time: O(n)
- go through every index of s (n)
- all other operations are constant time (do not increase complexity)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0

        # frequency array
        counts = [0] * 26

        for right in range(len(s)):
            # update counts to include moving right (captial A is 65)
            counts[ord(s[right]) - 65] += 1

            # the window is invalid (window size - most frequent letter is larger than k changes)
            # therefore more characters that we have to convert then we are able to
            while (right - left + 1) - max(counts) > k:
                # try to make window valid
                counts[ord(s[left]) - 65] -= 1
                left += 1

            # now window is valid
            longest = max(longest, (right - left + 1))

        return longest
