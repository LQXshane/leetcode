## no.166

class Solution(object):
    def fractionToDecimal(self, nu, de):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # res = []
        
        sign = "-" if nu*de<0 else ""
        
        quotient, remainder = divmod(abs(nu),abs(de))
        
        res = [sign, str(quotient) , "."]
        
        remainders = []
        
        while remainder not in remainders:
            
            
            remainders.append(remainder)
            
            quotient, remainder = divmod(remainder*10,abs(de))
            
            res.append(str(quotient))
            
        end_idx = remainders.index(remainder)
        
        res.insert(end_idx+3, "(")
        
        res.append(")")
        
        return ''.join(res).replace('(0)', '').rstrip(".")
        
        # Rstrip: This method returns a copy of the string in which all chars have been stripped from the end of the string (default whitespace characters)
            
