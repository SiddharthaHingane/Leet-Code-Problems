class Solution:
    def findOriginalArray(self, changed):
        c = Counter(changed)
        # int = [0,0,0,0]
        if c[0]%2:
            return []
        for x in sorted(c): # c = [1:1,2:1,3:1,4:1,6:1,8:1]
            if c[x] > c[2*x]: # [6,3,4,1] = c [1:1,3:1,4:1,6:1]
                return []
            c[2*x] -=c[x] if x else c[x]//2
        return list(c.elements())
