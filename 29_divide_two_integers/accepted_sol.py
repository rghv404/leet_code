class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0 or abs(dividend) < abs(divisor):
            return 0
        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        
        #overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        dividend, divisor = abs(dividend), abs(divisor)
        
        if divisor == 1:
            return dividend if sign else -dividend
        
        return get_quo(dividend, divisor, sign)
            
def get_quo(divid, divis, sign):
    quo = 0
    while divid >= divis:
        d_ = divis
        tmp_quo = 1
        while d_ + d_ < divid:
            d_ += d_
            tmp_quo += tmp_quo
        quo += tmp_quo
        divid -= d_
    return quo if sign else -quo
