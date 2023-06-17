# 深さ優先探索(python dfs.py)
# 木構造を表すデータ構造のためのクラス
class TreeNode: # 左下と右下に繋がっているノードが何かを定義している
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
tree = [1, 2, 3, 4, 5, 6]
def make_tree(tree, node, i, n): # 二文木を作成
    # node:今見ているノード
    # i:今見ているノードのインデックス
    # n:木のノード数
    if n > i:
        if tree[i] is None:
            return None
        temp = TreeNode(tree[i])
        node = temp
        node.left = make_tree(tree, node.left, 2 * i + 1, n)
        node.right = make_tree(tree, node.right, 2 * i + 2, n)
    return node

root = make_tree(tree, None, 0, len(tree))
print(root.val, root.left.val, root.right.val)
