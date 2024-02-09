#!/usr/bin/env python

# Copyright 2023-2024 distjr_
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import socket
import select
import threading
import createcontest
from datetime import datetime
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import time

# os.system("mode con cols=100 lines=30")
# page = """
#  ***********************************************************************************************
#  |                                 Nomel 考试系统 服务器端                                     |
#  ***********************************************************************************************
#  |    当前在线的学生     |     最新消息      |          命令行(输入help以查看帮助)             |
#  +-----------------------+-------------------+-------------------------------------------------+
#  |                       |                   |                                                 |
#  |                       |                   |                                                 |
#  |                       |                   |                                                 |
#  |                       |                   |                                                 |
#  |                       |                   |                                                 |
#  |                       |                   |                                                 |
#  |                       |                   |                                                 |
#  |                       |                   |                                                 |
#  |                       |                   |                                                 |
#  |                       |                   |                                                 |
#  |                       |                   |                                                 |
#  |                       |                   |                                                 |
#  |                       |                   |                                                 |
#  |                       |                   |                                                 |
#  |                       |                   |                                                 |
#  |                       |                   | >>>                                             |
#  +-----------------------+-------------------+-------------------------------------------------+
#  |                                                                                             |
#  |                                                                                             |
#  |                                                               copyright 2023-2024 distjr_   |
#  ***********************************************************************************************
# """

# print(page)

# messageprint = ""
# cmdprint = ""

# def newstudent(name,ip):
#     messageprint = messageprint + ("\n%s加入比赛" % name)
#     cmdprint = cmdprint + ("New Client: %s (name=%s)" % (ip,name))
# def leavestudent(name,ip):
#     messageprint = messageprint + ("\n%s离开比赛" % name)
#     cmdprint = cmdprint + ("Connection disconnected: %s (name=%s)" % (ip,name))

root = Tk(className="Nomel")
root.title("Nomel 比赛服务器")
root.iconbitmap("icon.ico")
root.geometry("700x500")
root.resizable(0, 0)

global notice
notice = "None"

f = Frame(root,width=700,height=500)
f.place(x=0,y=0)
t1 = tkinter.Text(f,width=97,height=35,state=tkinter.DISABLED)
scrollbar = Scrollbar(f, command=t1.yview)
t1.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
t1.pack(side=LEFT, fill=BOTH, expand=True)

def print(string,isend=True,showtime=True):
    t1.configure(state=tkinter.NORMAL)
    t1.insert('end',((datetime.now().strftime("%Y-%m-%d %H:%M:%S")+": ") if showtime else "")+string+("\n" if isend else " "))
    t1.see(END)
    t1.configure(state=tkinter.DISABLED)
    root.update()

contest = createcontest.Contest(1, 1, 1, 1)
try:
    contest.read("nowcontest\\now.nfct")
except Exception:
    messagebox.showerror("Nomel 0x01000022", "文件已被移除或文件格式不受支持", parent=root)
    exit()

ltxt = Label(root,text="在此输入通知：")
ltxt.place(x=10,y=470)
lent = Entry(root,width=65)
lent.place(x=100,y=470)

address = ("127.0.0.1",2008)    

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(address)

def goex(*args):
    global notice
    notice = lent.get()
    try:
        conn,addr = server.accept()
    except OSError:
        print("服务器已关闭，无法发布通知")
        return
    if not notice:
        notice = "None"
    lent.delete('0','end')

lbut = ttk.Button(root,text="发布",command=goex)
lbut.place(x=580,y=470)



def process(tcpCliSock,addr):
    print("Successfully established connection with client: " + str(addr))
    name = ""
    sent = "Got it!"
    while True:
        try:
            data = tcpCliSock.recv(1024).decode('utf-8')
            if data != '':
                if data[0] == "n":
                    name = data[1:]
                    print("欢迎 %s 加入比赛！" % (name))
                if data[0] == "w":
                    print("%s 正在申请获取题目……" % (name),False)
                    aetime = contest.starttime
                    atime = "%04d-%02d-%02d %02d:%02d:%02d" % (aetime[0],aetime[1],aetime[2],aetime[3],aetime[4],aetime[5])
                    aetime = contest.endtime
                    ttime = "%04d-%02d-%02d %02d:%02d:%02d" % (aetime[0],aetime[1],aetime[2],aetime[3],aetime[4],aetime[5])
                    cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    if ((datetime.strptime(atime,"%Y-%m-%d %H:%M:%S")-datetime.strptime(cur_time,"%Y-%m-%d %H:%M:%S")).days > 0):
                        print("失败，比赛尚未开始",True,False)
                    elif ((datetime.strptime(ttime,"%Y-%m-%d %H:%M:%S")-datetime.strptime(cur_time,"%Y-%m-%d %H:%M:%S")).days < 0):
                        print("失败，比赛已经结束",True,False)
                    else:
                        print("成功",True,False)
                if data[0] == "l":
                    print("%s 退出比赛！" % (name))
                if data[0] == "s":
                    realdata = data.splitlines()
                    problemname = realdata[0][1:]
                    code = '\n'.join(realdata[1:])
                    print("%s 提交了题目 %s 的代码……" % (name,problemname),False)
                    aetime = contest.starttime
                    atime = "%04d-%02d-%02d %02d:%02d:%02d" % (aetime[0],aetime[1],aetime[2],aetime[3],aetime[4],aetime[5])
                    aetime = contest.endtime
                    ttime = "%04d-%02d-%02d %02d:%02d:%02d" % (aetime[0],aetime[1],aetime[2],aetime[3],aetime[4],aetime[5])
                    cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    if ((datetime.strptime(atime,"%Y-%m-%d %H:%M:%S")-datetime.strptime(cur_time,"%Y-%m-%d %H:%M:%S")).days > 0):
                        print("失败，比赛尚未开始",True,False)
                    elif ((datetime.strptime(ttime,"%Y-%m-%d %H:%M:%S")-datetime.strptime(cur_time,"%Y-%m-%d %H:%M:%S")).days < 0):
                        print("失败，比赛已经结束",True,False)
                    else:
                        print("成功",True,False)
                        print("    正在评测中...")
                if data[0] == "o":
                    sent = notice
                    if notice != "None":
                        print("%s 收到了你的通知：%s" % (name,notice))
            tcpCliSock.send(bytes(sent,encoding='utf-8'))
            sent = "Got it!"
        except socket.error:
            break
    print("Disconnected from client: " + str(addr))



def run():
    global server
    server.listen(5)
    while True:
        r,w,e = select.select([server,],[],[],1)
        for i,server in enumerate(r):
            try:
                conn,addr = server.accept()
            except OSError:
                return
            t = threading.Thread(target=process,args=(conn,addr))
            t.start()
        
print("服务器已在 %s:%s 开放" % (address[0],address[1]))

r = threading.Thread(target=run)
r.start()

def loop():
    while True:
        aetime = contest.starttime
        atime = "%04d-%02d-%02d %02d:%02d:%02d" % (aetime[0],aetime[1],aetime[2],aetime[3],aetime[4],aetime[5])
        aetime = contest.endtime
        ttime = "%04d-%02d-%02d %02d:%02d:%02d" % (aetime[0],aetime[1],aetime[2],aetime[3],aetime[4],aetime[5])
        while ((datetime.strptime(atime,"%Y-%m-%d %H:%M:%S")-datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")).days > 0):
            time.sleep(10)
        print("*****比赛正式开始*****",True,False)
        while ((datetime.strptime(ttime,"%Y-%m-%d %H:%M:%S")-datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")).days > 0):
            time.sleep(10)
        print("*****比赛正式结束*****",True,False)
        break
    server.close()
    print("服务器已关闭")


wer = threading.Thread(target=loop)
wer.start()


root.mainloop()
