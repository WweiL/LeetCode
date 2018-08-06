class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        neg = 1
        if dividend < 0 and divisor > 0:
            neg = -1
            dividend = -dividend
        elif dividend > 0 and divisor < 0:
            neg = -1
            divisor = -divisor
        elif dividend < 0 and divisor < 0:
            divisor = -divisor
            dividend = -dividend
            
        ans = 0
        while dividend >= divisor:
            bit_multiplication_counter = 0
            div = divisor
            while dividend >= div:
                div = div << 1
                bit_multiplication_counter += 1
            ans += 1 << (bit_multiplication_counter - 1)
            dividend -= divisor << (bit_multiplication_counter-1)

        ans = ans if neg == 1 else -ans
        return ans if -2**31 <= ans <= 2**31 -1 else 2**31 -1
        
