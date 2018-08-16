# # # dfs: build graph, find strongly connected components
# class Solution:
#     def accountsMerge(self, accounts):
#         """
#         :type accounts: List[List[str]]
#         :rtype: List[List[str]]
#         """
        
# # union find
# class Solution:
#     def accountsMerge(self, accounts):
#         """
#         :type accounts: List[List[str]]
#         :rtype: List[List[str]]
#         """
#         from collections import defaultdict
#         parent = {}
#         email_to_name = {}
#         def find(email):
#             if parent[email] != email:
#                 parent[email] = find(parent[email])
#             return parent[email]
        
#         def union(email1, email2):
#             parent[find(email2)] = find(email1)

#         for account in accounts:
#             name = account[0]
#             for email in account[1:]:
#                 if email not in parent:
#                     # the email is not in any set, initialize itself as a set
#                     parent[email] = email
#                 email_to_name[email] = name
#                 # union(account[1], email)
#                 union(email, account[1])
        
#         root_email_to_emails = defaultdict(list)
#         for email in parent.keys():
#             root = find(email)
#             root_email_to_emails[root].append(email)
#         # root_email_to_emails: {root_email1: [email1, email2, ...], root_email2: [email3, email4, ...]}
#         return [[email_to_name[root_email]] + sorted(root_email_to_emails[root_email]) for root_email in root_email_to_emails.keys()]
    
# # hash table, not feasible
# class Solution:
#     def accountsMerge(self, accounts):
#         """
#         :type accounts: List[List[str]]
#         :rtype: List[List[str]]
#         """
#         ans_map = {}
#         email_name_map = {}
#         for account in accounts:
#             name = account[0]
#             emails = account[1:]
#             should_merge = False
#             to_be_merged = []
#             for email in emails:
#                 if email_name_map.get(email, -1) != -1:
#                     should_merge = True or should_merge
#                 else:
#                     to_be_merged.append(email)
#             if should_merge:
#                 # found an element to be merged
#                 ans_map[name].append(to_be_merged)
#             else:
#                 ans_map[name] = emails
#                 email_name_map[email] = name
#         ans = []
#         for name in ans_map:
#             ans.append([name] + sorted(ans_map[name]))
#         print(ans)
#         return ans
                
