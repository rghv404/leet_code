class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0 or abs(dividend) < abs(divisor):
            return 0
        elif (dividend < 0 and divisor > 0):
            if divisor == 1:
                if dividend >= -2**31:
                    return dividend
                else: return 2**31 - 1    
            return -get_quo(abs(dividend), abs(divisor))
        elif (dividend > 0 and divisor < 0):
            if divisor == -1:
                if dividend < 2**31:
                    return -dividend
                else: return 2**31 - 1    
            return -get_quo(abs(dividend), abs(divisor))
        else:
            if abs(divisor) == 1:
                if abs(dividend) < 2**31:
                    return abs(dividend)
                else: return 2**31 - 1  
            return get_quo(abs(dividend), abs(divisor))
            
def get_quo(a, b):
    quo = 1
    b_ = b
    while quo < 2**31:
        b_ += b
        if b_ <= a:
            quo += 1
        else:
            break
    return quo
    # while b_ <= a and quo <= 2**31:
    #     b_ += b
    #     quo += 1
    # return quo - 1