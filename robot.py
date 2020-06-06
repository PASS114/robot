import wx  
import time
import random
import requests

class MyFrame(wx.Frame):
    msglist=["听不懂你在说什么","呵呵","What","WTF","要吃饭了","哈哈"] 
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"机器人小明!",size=(520,450))
        panel=wx.Panel(self)
        labelAll=wx.StaticText(panel,-1,"全部对话显示")
        self.textAll=wx.TextCtrl(panel,
                                 -1,
                                 size=(480,200),
                                 style=wx.TE_MULTILINE|wx.TE_READONLY)
        labelIn=wx.StaticText(panel,-1,"请在下面发言")
        self.textIn=wx.TextCtrl(panel,-1,size=(480,100),
                                 style=wx.TE_MULTILINE)
        
        self.btnSent=wx.Button(panel,-1,"发送信息",size=(75,25))
        self.btnClear=wx.Button(panel,-1,"清除记录",size=(75,25))
        self.Bind(wx.EVT_BUTTON,self.OnButtonSent,self.btnSent)
        self.Bind(wx.EVT_BUTTON,self.OnButtonClear,self.btnClear)
        
        btnSizer=wx.BoxSizer()
        btnSizer.Add(self.btnSent,proportion=0)
        btnSizer.Add(self.btnClear,proportion=0)
        
        mainSizer=wx.BoxSizer(wx.VERTICAL)
        
        mainSizer.Add(labelAll,proportion=0,flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textAll,proportion=1,flag=wx.EXPAND)
        
        mainSizer.Add(labelIn,proportion=0,flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textIn,proportion=0,flag=wx.EXPAND)
        mainSizer.Add(btnSizer,proportion=0,flag=wx.ALIGN_CENTER)
        panel.SetSizer(mainSizer)
        inmsg="机器人小明 (%s):\n我是机器人小明\n"%(time.ctime())
        self.textAll.AppendText(inmsg)
        
    def OnButtonSent(self,event):
       userinput=self.textIn.GetValue()
       self.textIn.Clear()
       now=time.ctime()
       inmsg="You (%s):\n%s\n"%(now,userinput)
       self.textAll.AppendText(inmsg)
       
       index=random.randint(0,len(self.msglist))
       print(index)
       if index==len(self.msglist):
           reply="你是说 %s 我还在学说话"%(userinput)
       else:
           reply=get_response(userinput)
       print(reply)
       replymsg="机器人小明 (%s):\n%s\n"%(now,reply)
       self.textAll.AppendText(replymsg)
       #self.textAll.SetValue(userinput)
       
    def OnButtonClear(self,event): 
        self.textAll.Clear()
        
KEY = 'ca098ebe818b49df98af997bef29b3b3' 
def get_response(msg):
    Url='http://www.tuling123.com/openapi/api'
    data={'key':KEY,
          'info':msg,
          'userid':'pth-robot',
         }
    try:
        r=requests.post(Url,data=data).json()
        return r.get('text')
    except:
        return
app=wx.App()   
frame=MyFrame()
frame.Show()
app.MainLoop()   
