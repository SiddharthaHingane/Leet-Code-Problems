class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        
        # x overlap 
        xtop = min(ax2,bx2)
        xbot = max(ax1,bx1)
        x_over = xtop - xbot
        
        
        # y overlap
        ytop = min(ay2,by2)
        ybot = max(ay1,by1)
        y_over = ytop - ybot

        
        over_area = 0
        
        if x_over > 0 and y_over > 0:
            over_area = x_over * y_over

        #overlap_area = ((min(ax2, bx2) - max(ax1, bx1)) * (min(ay2, by2) - max(ay1, by1)))
        x = area_a + area_b - over_area
        return x
