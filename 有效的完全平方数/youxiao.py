class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1:
            return num
        x0 = 1.0
        ran = x0 * x0 - num
        if ran < 0:
            ran = 0 - ran
        while ran > 0.2:
            x1 = x0/2 + num/(x0*2)
            x0 = x1
            ran = x1 * x1 - num
            if ran < 0:
                ran = 0 - ran
            x1 = int(x1)
        if x1 * x1 == num:
            return 1
        return 0