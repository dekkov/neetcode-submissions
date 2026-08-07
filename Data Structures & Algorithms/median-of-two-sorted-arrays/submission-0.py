class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        half = ( len(A) + len(B) ) // 2
        l, r = 0, len(A) - 1

        while True:
            mA = (l + r) // 2
            mB = half - mA - 2

            Aleft = A[mA] if mA >= 0 else float('-inf')
            Aright = A[mA + 1] if mA + 1 < len(A) else float('inf')

            Bleft = B[mB] if mB >= 0 else float('-inf')
            Bright = B[mB + 1] if mB + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if (len(A) + len(B)) % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright,Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft <= Bright and Bleft > Aright:
                l = mA + 1
            else:
                r = mA - 1
        
        return -1