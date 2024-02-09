#!/usr/bin/env python

# Copyright 2023 distjr_
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

"""
0x01000001: 填充本地保存的文件列表时，发现了无法正常打开的文件
0x0200201A: 无法将文件导出至指定位置，可能是权限不够、目标文件正在被使用等原因导致的
0x01000021: 找不到需要编辑的文件
0x01000022: 需要编辑的文件已被移除或文件格式不受支持
0x0A00****: 题目或数据点格式有误
"""

import os
import os.path
import tkinter
import pyglet
from tkinter import ttk, messagebox, filedialog
from tkinter import *
import pickle
import createcontest
import usefulfuncs

pyglet.font.add_file("SourceHanSansSC.otf")

root = Tk(className="Nomel")
root.title("Nomel")
root.iconbitmap("icon.ico")
root.geometry("700x500")
root.resizable(0, 0)


titlelabel = Label(root, text="Nomel", font=("Source Han Sans SC", 40))
titlelabel.place(x=15, y=15)
subtitlelabel = Label(root, text="快速地构建OI比赛", font=("Source Han Sans SC", 15))
subtitlelabel.place(x=15, y=100)

listlabel = Label(root, text="本地保存的文件列表", font=("Source Han Sans SC", 10))
listlabel.place(x=30, y=150)

tableframe = Frame(root)

global table

columns = ["name", "rule", "number", "start", "end"]
table = ttk.Treeview(
    tableframe,
    height=12,
    columns=columns,
    show="headings",
)

table.heading("name", text="比赛名")
table.heading("rule", text="赛制")
table.heading("number", text="题目数量")
table.heading("start", text="开始时间")
table.heading("end", text="结束时间")

table.column("name", width=30, minwidth=50, anchor=S)
table.column("rule", width=5, minwidth=25, anchor=S)
table.column("number", width=3, minwidth=50, anchor=S)
table.column("start", width=90, minwidth=45, anchor=S)
table.column("end", width=110, minwidth=45, anchor=S)
table.pack(anchor=W, ipadx=325, ipady=100, side=LEFT, expand=True, fill=BOTH)

vbar1 = ttk.Scrollbar(table, orient=VERTICAL, command=table.yview)
table.configure(yscrollcommand=vbar1.set)
vbar1.pack(side=RIGHT, fill=Y)

tableframe.place(x=20, y=180)

global inserttable


def inserttable(name, rule, number, start, end):
    table.insert("", END, values=[name, rule, number, start, end])


errorfiles = "无法正确地获取以下本地保存的文件："

for eeroot, dirs, files in os.walk("lastcontest\\", topdown=False):
    for name in files:
        if os.path.splitext(name)[-1] == ".nfctmp":
            contest = createcontest.Contest(1, 1, 1, 1)
            try:
                contest.read("lastcontest\\" + name)
                inserttable(
                    contest.name,
                    contest.rule,
                    len(contest.problems),
                    usefulfuncs.runtimee(contest.starttime),
                    usefulfuncs.runtimee(contest.endtime),
                )
            except Exception:
                errorfiles = errorfiles + "\n" + name

if "\n" in errorfiles:
    messagebox.showerror("Nomel 0x01000001", errorfiles)


def opencon(*args):
    f = open("lastcontest\\newlast.dat", "wb")
    try:
        pickle.dump("lastcontest\\" + table.set(table.focus())["name"] + ".nfctmp", f)
    except KeyError:
        messagebox.showinfo("Nomel", "请先选择一个文件")
        return
    f.close()
    import contestedit


def openfile(*args):
    filename = filedialog.askopenfile(
        title="打开比赛文件", filetypes=[("比赛文件", "*.nfct"), ("All files", "*")]
    )
    if filename == "" or not filename:
        return
    filename = filename.name
    f = open("lastcontest\\newlast.dat", "wb")
    pickle.dump(filename, f)
    f.close()
    import contestedit


def newcon(*args):
    new = tkinter.Toplevel()
    new.title("新建比赛")
    new.iconbitmap("icon.ico")
    new.geometry("250x315+150+150")
    new.resizable(0, 0)

    namelab = Label(new, text="比赛名称")
    namelab.place(x=10, y=10)
    nameen = ttk.Entry(new, width=23)
    nameen.place(x=70, y=10)
    rullab = Label(new, text="比赛规则")
    rullab.place(x=10, y=45)
    varrul = StringVar()
    rulen = ttk.Combobox(new, state="readonly", textvariable=varrul)
    rulen["values"] = ["OI", "IOI"]
    rulen.set("OI")
    rulen.place(x=70, y=45)

    timelab = Label(new, text="开始时间")
    timelab.place(x=10, y=80)
    stimeyearspin = ttk.Spinbox(new, from_=2023, to=2030, width=17)
    stimeyearspin.place(x=70, y=80)
    stimeyearspint = Label(new, text="年")
    stimeyearspint.place(x=210, y=80)
    stimemonthspin = ttk.Spinbox(new, from_=1, to=12, width=5)
    stimemonthspin.place(x=70, y=110)
    stimemonthspint = Label(new, text="月")
    stimemonthspint.place(x=130, y=110)
    stimedayspin = ttk.Spinbox(new, from_=1, to=31, width=5)
    stimedayspin.place(x=154, y=110)
    stimedayspint = Label(new, text="日")
    stimedayspint.place(x=210, y=110)

    westimeyearspin = ttk.Spinbox(new, from_=0, to=24, width=2)
    westimeyearspin.place(x=70, y=140)
    westimeyearspint = Label(new, text="时")
    westimeyearspint.place(x=105, y=140)
    westimemonthspin = ttk.Spinbox(new, from_=0, to=60, width=2)
    westimemonthspin.place(x=120, y=140)
    westimemonthspint = Label(new, text="分")
    westimemonthspint.place(x=155, y=140)
    westimedayspin = ttk.Spinbox(new, from_=0, to=60, width=2)
    westimedayspin.place(x=170, y=140)
    westimedayspint = Label(new, text="秒")
    westimedayspint.place(x=205, y=140)

    etimelab = Label(new, text="结束时间")
    etimelab.place(x=10, y=175)
    estimeyearspin = ttk.Spinbox(new, from_=2023, to=2030, width=17)
    estimeyearspin.place(x=70, y=175)
    estimeyearspint = Label(new, text="年")
    estimeyearspint.place(x=210, y=175)
    estimemonthspin = ttk.Spinbox(new, from_=1, to=12, width=5)
    estimemonthspin.place(x=70, y=205)
    estimemonthspint = Label(new, text="月")
    estimemonthspint.place(x=130, y=205)
    estimedayspin = ttk.Spinbox(new, from_=1, to=31, width=5)
    estimedayspin.place(x=154, y=205)
    estimedayspint = Label(new, text="日")
    estimedayspint.place(x=210, y=205)

    wwestimeyearspin = ttk.Spinbox(new, from_=0, to=24, width=2)
    wwestimeyearspin.place(x=70, y=235)
    wwestimeyearspint = Label(new, text="时")
    wwestimeyearspint.place(x=105, y=235)
    wwestimemonthspin = ttk.Spinbox(new, from_=0, to=60, width=2)
    wwestimemonthspin.place(x=120, y=235)
    wwestimemonthspint = Label(new, text="分")
    wwestimemonthspint.place(x=155, y=235)
    wwestimedayspin = ttk.Spinbox(new, from_=0, to=60, width=2)
    wwestimedayspin.place(x=170, y=235)
    wwestimedayspint = Label(new, text="秒")
    wwestimedayspint.place(x=205, y=235)

    def mustnew(*args):
        aanewcon = createcontest.Contest(
            nameen.get(),
            createcontest.settime(
                stimeyearspin.get(),
                stimemonthspin.get(),
                stimedayspin.get(),
                westimeyearspin.get(),
                westimemonthspin.get(),
                westimedayspin.get(),
            ),
            createcontest.settime(
                estimeyearspin.get(),
                estimemonthspin.get(),
                estimedayspin.get(),
                wwestimeyearspin.get(),
                wwestimemonthspin.get(),
                wwestimedayspin.get(),
            ),
            varrul.get(),
        )
        aanewcon.save("lastcontest\\%s.nfctmp" % nameen.get())
        f = open("lastcontest\\newlast.dat", "wb")
        pickle.dump("lastcontest\\%s.nfctmp" % nameen.get(), f)
        f.close()
        # eg = "lastcontest\\" + nameen.get() + '.nfctmp'
        new.destroy()
        import contestedit

        # fetc = filedialog.asksaveasfilename(title='打开比赛文件',filetypes=[("比赛文件","*.nfct"),("All files","*")])
        # try:
        #     f = open(fetc,"wb")
        #     f1 = open(eg,"rb")
        #     pickle.dump(pickle.load(f1),f)
        #     f.close()
        #     f1.close()
        # except Exception as e:
        #     messagebox.showerror('Nomel','Error: '+e+'\n请尝试手动将 %s 复制到您想保存的目录' % eg)

    qbuttonnew = ttk.Button(new, text="确认新建", command=mustnew)
    qbuttonnew.place(x=160, y=280)

    errorfiles = "无法正确地获取以下本地保存的文件："


def export(*args):
    fetc = filedialog.asksaveasfilename(
        title="导出比赛文件", filetypes=[("比赛文件", "*.nfct"), ("All files", "*")]
    )
    if fetc[-5:] != ".nfct":
        fetc = fetc + ".nfct"
    eg = "lastcontest\\" + table.set(table.focus())["name"] + ".nfctmp"
    try:
        f = open(fetc, "wb")
        f1 = open(eg, "rb")
        pickle.dump(pickle.load(f1), f)
        f.close()
        f1.close()
    except Exception as e:
        messagebox.showerror("Nomel 0x0200201A", "Error: " + e + "\n请尝试手动将 %s 复制到您想保存的目录" % eg)


def refresh(*args):
    table.delete(*table.get_children())
    errorfiles = "无法正确地获取以下本地保存的文件："
    for eeroot, dirs, files in os.walk("lastcontest\\", topdown=False):
        for name in files:
            if os.path.splitext(name)[-1] == ".nfctmp":
                contest = createcontest.Contest(1, 1, 1, 1)
                try:
                    contest.read("lastcontest\\" + name)
                    inserttable(
                        contest.name,
                        contest.rule,
                        len(contest.problems),
                        usefulfuncs.runtimee(contest.starttime),
                        usefulfuncs.runtimee(contest.endtime),
                    )
                except Exception:
                    errorfiles = errorfiles + "\n" + name
    if "\n" in errorfiles:
        messagebox.showerror("Nomel 0x01000001", errorfiles)
    else:
        messagebox.showinfo("Nomel","刷新成功！")


buttonin = ttk.Button(root, text="打开该文件", command=opencon)
buttonin.place(x=30, y=450)
buttonnew = ttk.Button(root, text="新建比赛", command=newcon)
buttonnew.place(x=140, y=450)
buttonnew = ttk.Button(root, text="打开比赛文件", command=openfile)
buttonnew.place(x=250, y=450)
buttonexport = ttk.Button(root, text="导出该比赛", command=export)
buttonexport.place(x=360, y=450)
buttonrefresh = ttk.Button(root, text="刷新列表", command=refresh)
buttonrefresh.place(x=470, y=450)

copyrightlabel = Label(
    root, text="Copyright 2023 distjr_", font=("Source Han Sans SC", 8)
)
copyrightlabel.place(x=550, y=475)

root.mainloop()
