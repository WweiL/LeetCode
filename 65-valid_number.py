class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dfa = [
                {},
                {"blank": 1, "sign": 2, "digit": 3, "dot": 4},
                {"digit": 3, "dot": 4},
                {"digit": 3, "dot": 5, "e": 6, "blank": 9},
                {"digit": 5},
                {"digit": 5, "e": 6, "blank": 9},
                {"sign": 7, "digit": 8},
                {"digit": 8},
                {"digit": 8, "blank": 9},
                {"blank": 9}
        ]
        
        state = 1
        for c in s:
            if c.isdigit():
                nextState = "digit"
            elif c == ".":
                nextState = "dot"
            elif c == "+" or c == "-":
                nextState = "sign"
            elif c == " ":
                nextState = "blank"
            elif c == "e":
                nextState = "e"
            else:
                return False
            
            if nextState in dfa[state].keys():
                state = dfa[state][nextState]
            else:
                return False
            
        if state in [3, 5, 8, 9]:
            return True
        else:
            return False
        
