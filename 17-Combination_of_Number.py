class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"],
                    "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"],
                    "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        # Use recursion (TLE, MLE)
        # Base case
        # if len(digits) == 0:
        #     return []
        # elif len(digits) == 1:
        #     return mapping[digits]
        # WRONG!!
        # else:
        #     result = []
        #     recursion_res = self.letterCombinations(digits[1:])
        #     for res in recursion_res:
        #         for letter in mapping[digits[0]]:
        #             result.append(letter+res)
        #     return result
        
        # Use DP
        # Define Algo(i) as the result of all possible combinations starting at i^th letter(base 1).
        # Algo(i) = mapping(Algo(i))                    if i = 1
        #         = mapping(Algo(i)) x Algo(i+1)        if i > 1
        # Use a standard array to store the result
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return mapping[digits[0]]
        else:
            result = mapping[digits[0]]
            temp = []
            for digit in digits[1:]:
                for temp_res in result:
                    for letter in mapping[digit]:
                        temp.append(temp_res + letter)
                result = temp # result is algo(i-1)
                temp = []
            return result
                    
