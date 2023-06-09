# 深さ優先探索(python dfs.py)
# 木構造を表すデータ構造のためのクラス
from collections import deque
class TreeNode: # 左下と右下に繋がっているノードが何かを定義している
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree = [1, 2, 3, 4, 5, 6] # このノードを左右のノードに登録する

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

ans = [] # 答えを入れるリスト
root = make_tree(tree, None, 0, len(tree)) # スタート地点
stack = deque([root]) # データ構造にリストを置換
# 深さ優先探索の実装, 空になるまでループを続ける
while stack:
    node = stack.pop() # stackの右側から要素を一つ取り出す
    ans.append(node.val) # ansに追加
    if node.right: # 右側のノードが存在するならstackに追加
        stack.append(node.right)
    if node.left: # 左側のノードが存在するならstackに追加
        stack.append(node.left)

bfsQueue = []
queue = deque([root]) # データ構造にリストを置換
while queue:
    node = queue.popleft() # queueの左側から要素を一つ取り出す
    bfsQueue.append(node.val)
    if node.left: # 左側のノードが存在するならqueueに追加
        queue.append(node.left)
    if node.right: # 右側のノードが存在するならqueueに追加
        queue.append(node.right)


print(root.val, root.left.val, root.right.val, root.left.left.val, root.left.right.val, root.right.left.val)
print(ans) # 深さ優先探索
print(bfsQueue) # 幅優先探索
# 一筆書きをしてノードの値の和が大きくなる経路を探す
ansSum = [] # 各経路の和を保存するためのリスト
sum = 0 # 各経路の和
stackSum = deque([(root, sum)]) # 木と和も同時に記録する必要がある
while stackSum:
    node, current_sum = stackSum.pop()
    current_sum += node.val
    if not node.left and not node.right:
        ansSum.append(current_sum)
    if node.right:
        stackSum.append((node.right, current_sum))
    if node.left:
        stackSum.append((node.left, current_sum))

print(max(ansSum)) # 10
