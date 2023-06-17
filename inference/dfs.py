# 深さ優先探索(python dfs.py)
# 木構造を表すデータ構造のためのクラス
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(1, 2, 3) # 木構造を作成
print(root.val, root.left, root.right)
