# coding:utf8
import wx
##### 定义按钮事件
def load(event):
    file = open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()
def save(event):
    file = open(filename.GetValue(),'w')
    file.write(contents.GetValue())
    file.close

##### 生成窗口
app = wx.App()
win = wx.Frame(None,title="李杨的测试",size=(410,335))
bkg = wx.Panel(win)

##### 定义按钮
loadButton = wx.Button(bkg,label='打开')
loadButton.Bind(wx.EVT_BUTTON,load)
saveButton = wx.Button(bkg,label='保存')
saveButton.Bind(wx.EVT_BUTTON,save)

##### 定义文本框
filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)

##### 定义组件相对位置
hbox = wx.BoxSizer()
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(loadButton,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)

bkg.SetSizer(vbox)

win.Show()
app.MainLoop()