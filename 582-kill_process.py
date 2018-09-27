class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        from collections import defaultdict, deque
        children = defaultdict(list)
        kill_pos = 0
        for i in range(len(pid)):
            children[ppid[i]].append(pid[i])
            if pid[i] == kill:
                kill_pos = i
        ans = []
        queue = deque()
        queue.append(kill)
        while(queue):
            papa = queue.popleft()
            ans.append(papa)
            for i in children[papa]:
                queue.append(i)
        return ans
