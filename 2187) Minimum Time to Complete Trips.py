class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left=1
        right=max(time)*totalTrips
        time.sort()
        
        def isFeasible(t):
            total=0
            for num in time:
                total+=t//num
                if total>=totalTrips:
                    return True
            return False
                 
        while(left<right):
            mid=(left+right)//2
            if isFeasible(mid):
                right=mid
            else:
                left=mid+1
        return left
