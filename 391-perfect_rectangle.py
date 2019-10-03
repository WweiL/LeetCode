class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        lm, rm, bm, um = float('inf'), -float('inf'), float('inf'), -float('inf')
        area = 0
        corners = {}
        for rect in rectangles:
            l, b, r, u = rect
            lm, rm, bm, um = min(lm, l), max(rm, r), min(bm, b), max(um, u)
            area += (r-l) * (u-b)
            # count the number of apperance of each point
            corners[(l, b)] = corners.get((l, b), 0) + 1
            corners[(l, u)] = corners.get((l, u), 0) + 1
            corners[(r, b)] = corners.get((r, b), 0) + 1
            corners[(r, u)] = corners.get((r, u), 0) + 1
        if area != (rm-lm) * (um-bm):
            return False
        for point, cnt in corners.items():
            if point in [(lm, bm), (lm, um), (rm, bm), (rm, um)]:
                if corners[point] != 1:
                    return False
            else:
                if corners[point] % 2 != 0:
                    return False
        return True
