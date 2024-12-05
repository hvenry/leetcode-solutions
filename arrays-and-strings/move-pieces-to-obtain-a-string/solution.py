"""
You are given two strings start and target, both of length n. Each string consists of only of the characters 'L', 'R',
and '_' where:

- The charactesr 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space
  directly to its left, and piece 'R' can move to the right only if there is a blank space directly to the right.
- The character '_' represents a blank space that can be occupied by any of teh 'L' and 'R' pieces.

Return True if it is possible to obtain the string target by moving the pieces of the string start any number of times.
Otherwise, return False.

Example 1:
start =  "_L__R__R_"
target = "L______RR"
returns: True

- We can move the L and R pieces to form the target string, we move L all the way left, and both R's all the way right.

Solution:
- We can compare indicies of each char to see if a L index in start comes before L index in target to return False, and
  to the same for R index in start that comes after R index in target to also return False.
- If these conditions can be met, we can return True.

Complexity:
- Time: O(n)
- Space: O(n) -> how do we  get this to O(1)

Solution O(1) space:
- Store seen L's, R's and match to validate.
    - Rule: 'R' cannot move left past an unmatched 'L' in the target string
    - Rule: 'L' cannot move right past an unmatched 'R' in the start string
    - Rule: Each 'R' in the target must correspond to an unmatched 'R' from the start string
    - Rule: Each 'L' in the start must correspond to an unmatched 'L' in the target
- return True if there are no more unmatched characters

Complexity:
- Time: O(n)
- Space: O(1)
"""


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Time: O(n), Space: O(1) solution:
        if start == target:
            return True

        # Track unmatched 'L' in target and 'R' in start
        pending_left = 0
        unmatched_right = 0

        for start_char, target_char in zip(start, target):
            if start_char == "R":
                # Rule: 'R' cannot move left past an unmatched 'L' in the target string
                if pending_left > 0:
                    return False
                unmatched_right += 1

            if target_char == "L":
                # Rule: 'L' cannot move right past an unmatched 'R' in the start string
                if unmatched_right > 0:
                    return False
                pending_left += 1

            if target_char == "R":
                # Rule: Each 'R' in the target must correspond to an unmatched 'R' from the start string
                if unmatched_right == 0:
                    return False
                unmatched_right -= 1

            if start_char == "L":
                # Rule: Each 'L' in the start must correspond to an unmatched 'L' in the target
                if pending_left == 0:
                    return False
                pending_left -= 1

        # Check that there are no leftover unmatched characters
        return pending_left == 0 and unmatched_right == 0

        # # Time: O(n), Space: O(n) solution (a bit easier to follow)
        # start_pos = [(char, index) for index, char in enumerate(start) if char != "_"]
        # target_pos = [(char, index) for index, char in enumerate(target) if char != "_"]
        #
        # # If amount of chars are not equal, it must be false
        # if len(start_pos) != len(target_pos):
        #     return False
        #
        # for (start_c, start_i), (target_c, target_i) in zip(start_pos, target_pos):
        #     if start_c != target_c:
        #         return False
        #
        #     # if L is too far left (cant be moved right to the target index), return False
        #     if start_c == "L" and start_i < target_i:
        #         return False
        #
        #     # if R is too far right (cant be moved left to target index), return False
        #     if start_c == "R" and start_i > target_i:
        #         return False
        #
        # return True
