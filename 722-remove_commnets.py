class Solution:
    class DFA:
        def __init__(self):
            self.ans = []
            self.buffer = []
            self.curr = "wr"
        def parse(self, line):
            i = 0
            n = len(line)
            start = 0
            while i < n:
                if self.curr == "wr": # write, plain text
                    if i < n-1 and line[i] == "/" and line[i+1] == "*":
                        start = i
                        self.curr = "st"
                        i += 2
                    elif(i < n-1 and line[i] == "/" and line[i+1] == "/"):
                        self.flush()
                        self.curr = "sl"
                        i += 2
                    else:
                        self.buffer.append(line[i])
                        i += 1
                elif self.curr == "sl": # slash, // ...
                    self.curr = "wr"
                    self.flush()
                    break
                else: # st, star, /* ... */
                    end = line[start:].find("*/")
                    if end == 1:
                        i += 1
                        start = i
                    else:
                        if end == -1:
                            break
                        else:
                            self.curr = "wr"
                            i = start + end + 2
                            
            if self.curr == "wr":
                self.flush()

        def flush(self):
            s = "".join(self.buffer)
            if len(s) > 0:
                self.ans.append(s)
            self.buffer = []
            
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        dfa = self.DFA()
        for code in source:
            dfa.parse(code)
        dfa.flush()
        return dfa.ans
        
