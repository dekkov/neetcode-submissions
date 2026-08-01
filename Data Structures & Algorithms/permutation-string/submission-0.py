class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        ord_map_s1 = [0] * 26
        ord_map_s2 = [0] * 26


        for i in range(len(s1)):
            ord_map_s1[ord(s1[i]) - ord('a')] += 1
            ord_map_s2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if ord_map_s1[i] == ord_map_s2[i] else 0)
        
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            ord_map_s2[index] += 1
            if ord_map_s1[index] == ord_map_s2[index]:
                matches += 1
            elif ord_map_s1[index] + 1 == ord_map_s2[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            ord_map_s2[index] -= 1
            if ord_map_s1[index] == ord_map_s2[index]:
                matches += 1
            elif ord_map_s1[index] - 1 == ord_map_s2[index]:
                matches -= 1
            
            l += 1
        return matches == 26


