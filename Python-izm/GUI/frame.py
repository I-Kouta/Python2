
# python frame.py

import wx

application = wx.App() # 初期化

frame = wx.Frame(None, wx.ID_ANY, "テストフレーム", size = (300, 300)) # Frameを生成
frame.Centre() # 中央に表示する場合
frame.Show() # 可視化の処理

application.MainLoop() # イベント待ち受け状態へ遷移
