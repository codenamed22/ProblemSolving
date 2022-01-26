"""

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #move  through the tree breath first, in the queue maintain the node and the column its on
        #consider root to be column 0
        #maintain a dict of mapping column -> values
        #when going left send column - 1
        #when going right send column + 1
        #at the end sort the dict keywise and return the value lists
        d = defaultdict(list)
        q = deque()
        q.append([root,0])
        
        while q:
            n,c = q.popleft()
            
            if n is not None:
                d[c].append(n.val)
                q.append([n.left,c-1])
                q.append([n.right,c+1])
            
        return [d[x] for x in sorted(d.keys())]
