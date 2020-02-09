# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:59:28 2020

@author: Administrator
"""

import tkinter
import tkinter.messagebox
from tkinter import ttk
import datetime
from PIL import ImageTk,Image

class clock(object):
    
    def __init__(self):
        
        self.win=tkinter.Tk()
        self.flag=False
        self.pause_long=datetime.timedelta(seconds=0)
    
    def set_win(self):
        
        self.win.title("久坐小助手 @算法与数据之美 V1.0")
        self.win.geometry("450x300")
        canvas=tkinter.Canvas(self.win,height=300,width=450)
        img=Image.open('green.jpg')
        photo=ImageTk.PhotoImage(img)
        canvas.create_image(0,0,anchor='nw',image=photo)
        canvas.pack()
        label2=tkinter.Label(self.win,text='请选择时间间隔：').place(x=40,y=20)
        self.cv=tkinter.StringVar()
        self.com=ttk.Combobox(self.win,textvariable=self.cv)
        self.com.place(x=190,y=20)
        self.com['value']=("1分钟","15分钟","30分钟","45分钟","60分钟")
        self.com.current(0)
        self.com.bind("<<ComboboxSelected>>", self.get_time)
        
        
        button=tkinter.Button(self.win,text="开始",command=self.alarm,width=6,height=1)
        button.place(x=40,y=60)
        button2=tkinter.Button(self.win,text="暂停",command=self.pause,width=6,height=1)
        button2.place(x=180,y=60)     
        button3=tkinter.Button(self.win,text="继续",command=self.go_on,width=6,height=1)
        button3.place(x=320,y=60) 

        self.win.mainloop()
     
        
    def alarm(self):
        
        self.now=datetime.datetime.now()
        delta=datetime.timedelta(minutes=self.minute)
        self.target=self.now+delta
        self.win.after(0,self.update)
    
    
    def get_time(self,event):

        self.minute=int(self.com.get()[:-2])
        
        
        
    def pause(self):
        
        self.pause_time=datetime.datetime.now()
        self.flag=True
        self.win.after_cancel()

        
    def go_on(self):
        
        self.go_on_now=datetime.datetime.now()
        self.pause_long=self.go_on_now-self.pause_time+self.pause_long
        self.flag=False
        self.win.after(0,self.update)

    def update(self):
        
        now=datetime.datetime.now()
        countdown=self.target-now+self.pause_long
        self.label=tkinter.Label(self.win,text=str(countdown)[:7],font=("黑体",70))
        self.label.place(x=60,y=130)
        if str(countdown)[:7]=='0:00:00':
            tkinter.messagebox.showwarning(title="FBIWarning",message="您已工作{}分钟,请马上离开座位休息片刻！".format(self.minute))
            self.flag=True
            self.win.after_cancel()
        if self.flag==False:
            self.win.after(1,self.update)

      
if __name__=='__main__':
    
    c=clock()
    c.set_win()

    