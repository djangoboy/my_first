import wx

class nabin(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"Frame as window",size=(300,200))

if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=nabin(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
