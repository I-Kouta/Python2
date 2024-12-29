
# python frame.py

import wx

application = wx.App() # 初期化

x = 300
y = 300
frame = wx.Frame(None, wx.ID_ANY, "テストフレーム", size = (x, y)) # Frameを生成(横, 縦)
frame.Centre() # 中央に表示する場合

r_panel = wx.Panel(frame, wx.ID_ANY, pos = (0, 0), size = (100, 300)) # Panelを生成
r_panel.SetBackgroundColour("#ffcccc")

r_panel = wx.Panel(frame, wx.ID_ANY, pos = (100, 0), size = (100, 300)) # Panelを生成
r_panel.SetBackgroundColour("#ccffcc")

r_panel = wx.Panel(frame, wx.ID_ANY, pos = (200, 0), size = (100, 300)) # Panelを生成
r_panel.SetBackgroundColour("#ccccff")

frame.CreateStatusBar()
frame.SetStatusText("ステータスバー") # 下部にステータスバーを表示

frame.Show() # 可視化の処理

application.MainLoop() # イベント待ち受け状態へ遷移
