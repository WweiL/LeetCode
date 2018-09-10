class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        def valid(s, i):
            if i == 1:
                return int(s[0]+s[1]) <= 24 and int(s[0]+s[1]) >= 0
            elif i == 2:
                return int(s[0]+s[1]) <= 60 and int(s[0]+s[1]) >= 0
            else:
                print("Wrong input")
                return 2
            
        def sort(s):
            tmp = []
            for i in s:
                if i != ":":
                    tmp.append(i)
            tmp.sort()
            val_pos = {}
            pos_val = {}
            for i in range(4):
                val_pos[tmp[i]] = i
                pos_val[i] = tmp[i]
            return val_pos, pos_val
        
        def find_replacement(s, flag, val_pos, pos_val):
            for i in [1, 0]:
                tmp = s[i]
                if val_pos[s[i]] < 3:
                    s[i] = pos_val[val_pos[s[i]]+1]
                    if valid(s, flag):
                        if i == 0:
                            s[1] = pos_val[0]
                        return True
                    else:
                        s[i] = tmp
            return False

        if not time:
            return ""
        else:
            val_pos, pos_val = sort(time)
            s1 = [time[0], time[1]]
            s2 = [time[3], time[4]]
            if find_replacement(s2, 2, val_pos, pos_val):
                return "".join(s1)+":"+ "".join(s2)
            elif find_replacement(s1, 1, val_pos, pos_val):
                return "".join(s1)+":"+ pos_val[0]+pos_val[0]
            else:
                return pos_val[0]+pos_val[0]+":"+pos_val[0]+pos_val[0]
