import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        min_heap = []
        for l in lists:
            cur = l
            while cur:
                heapq.heappush(min_heap, cur.val)
                cur = cur.next

        head = ListNode(0)
        cur = head
        
        while min_heap:
            cur.next = ListNode(heapq.heappop(min_heap))
            cur = cur.next
            
        return head.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     a = 2 ** 32-1
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         # len(lists) == 1
#         # len(lists[i]) == 0
#         head = ListNode(0)
#         temp = head
    
#         while True:
#             minVal = self.a
#             i = 0
#             empty = True
#             for j, node in enumerate(lists):
#                 if node:
#                     empty = empty and False
#                     if node.val < minVal:
#                         minVal = node.val
#                         i = j
                    
#             if empty == True:
#                 break
#             else:
#                 print(i)
#                 temp.next = lists[i]
#                 lists[i] = lists[i].next
#                 temp = temp.next
#         return head.next
