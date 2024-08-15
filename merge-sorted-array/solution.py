from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Start from the end of nums1 and nums2
        p1 = m - 1
        p2 = n - 1

        # Pointer for the last position in nums1
        p = m + n - 1  
        
        # While there are elements to compare in both arrays
        while p1 >= 0 and p2 >= 0:
            # Compare the elements at p1 and p2
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are any remaining elements in nums2, copy them
        # No need to do this for nums1 because they are already in place
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
