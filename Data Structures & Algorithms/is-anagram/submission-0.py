class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for i in s:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1

        for i in t:
            if i in map:
                map[i] -= 1
            else:
                return False
        
        return all(value == 0 for value in map.values())