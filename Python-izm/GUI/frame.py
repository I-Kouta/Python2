
# python frame.py

import wx

application = wx.App()

frame = wx.Frame(None, wx.ID_ANY, "テストフレーム")
frame.Show()

application.MainLoop()
