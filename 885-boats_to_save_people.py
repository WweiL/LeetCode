class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if len(people) == 0:
            return 0
        elif len(people) == 1:
            return 1
        else:
            people.sort()
            low = 0
            hi = len(people) - 1
            boat = 0
            while low <= hi:
                if low == hi:
                    boat += 1
                    break
                if people[low] + people[hi] <= limit:
                    low += 1
                    hi -= 1
                else:
                    hi -= 1
                boat += 1

            return boat
