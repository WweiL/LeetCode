"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root: return ''
        ans = '[ ' + self.serizlize_dfs(root) + ' ]'
        print(ans)
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if data == '': return None
        root, i = Node(0, []), 0
        children_stack, nodes_stack = [[]], [root]

        while i < len(data):
            if data[i] == ']':
                i += 2
                children = children_stack.pop()
                node = nodes_stack.pop()
                node.children = children
            else:
                if data[i] == '[':
                    val, i = self.strip_num(data, i+1)
                else:
                    val, i = self.strip_num(data, i-1)
                node = Node(val, [])
                children_stack[-1].append(node)
                if data[i] == '[':
                    nodes_stack.append(node)
                    children_stack.append([])
        return root.children[0]
        
    def strip_num(self, data, start):
        end = start + 1
        while data[end].isdigit():
            end += 1
        return int(data[start+1:end]), end+1
                   
    def serizlize_dfs(self, root):
        if len(root.children) == 0:
            return str(root.val)
        ret = str(root.val) + ' [ '
        for child in root.children:
            ret += self.serizlize_dfs(child)
            ret += ' '
        return ret[:-1] + ' ]'
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
