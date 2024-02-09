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

import pickle
import tkinter
from tkinter import ttk, messagebox
from tkinter import *
import usefulfuncs
import pyglet
import createcontest

pyglet.font.add_file("SourceHanSansSC.otf")

root = Tk(className="Nomel")
root.title("编辑题目")
root.iconbitmap("icon.ico")
root.geometry("950x650")
root.resizable(0, 0)

try:
    f = open("lastcontest\\newlast.dat", "rb")
    fname = pickle.load(f)
    f.close()
except Exception as e:
    messagebox.showerror("Nomel 0x01000021", "FileNotFoundError: " + e, parent=root)
    exit()

# mbpython = miniblink.Miniblink
# mb = mbpython.init(os.getcwd()+r'\miniblink_4975_x64.dll')
# wke = mbpython(mb)
# window = wke.window


contest = createcontest.Contest(1, 1, 1, 1)
try:
    contest.read(fname)
except Exception:
    messagebox.showerror("Nomel 0x01000022", "文件已被移除或文件格式不受支持", parent=root)
    exit()

normallabel = Label(
    root, text="编辑您的比赛：%s" % contest.name, font=("Source Han Sans SC", 20)
)

informationlabel = Label(root, text="文件基本信息：", font=("Source Han Sans SC", 14))
informationslabel = Label(
    root,
    text="比赛名：%s  赛制：%s  开始时间：%s  结束时间：%s"
    % (
        contest.name,
        contest.rule,
        usefulfuncs.runtimee(contest.starttime),
        usefulfuncs.runtimee(contest.endtime),
    ),
    font=("Source Han Sans SC", 10),
)


def change(*args):
    new = tkinter.Toplevel()
    new.title("修改比赛")
    new.iconbitmap("icon.ico")
    new.geometry("250x315+150+150")
    new.resizable(0, 0)

    namelab = Label(new, text="比赛名称")
    namelab.place(x=10, y=10)
    nameen = ttk.Entry(new, width=23)
    nameen.place(x=70, y=10)
    nameen.insert(0, contest.name)

    rullab = Label(new, text="比赛规则")
    rullab.place(x=10, y=45)
    varrul = StringVar()
    rulen = ttk.Combobox(new, state="readonly", textvariable=varrul)
    rulen["values"] = ["OI", "IOI", "ACM"]
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

    def gomust(*args):
        contest.name = nameen.get()
        contest.rule = varrul.get()
        contest.starttime = createcontest.settime(
            stimeyearspin.get(),
            stimemonthspin.get(),
            stimedayspin.get(),
            westimeyearspin.get(),
            westimemonthspin.get(),
            westimedayspin.get(),
        )
        contest.endtime = createcontest.settime(
            estimeyearspin.get(),
            estimemonthspin.get(),
            estimedayspin.get(),
            wwestimeyearspin.get(),
            wwestimemonthspin.get(),
            wwestimedayspin.get(),
        )
        informationslabel.config(
            text="比赛名：%s  赛制：%s  开始时间：%s  结束时间：%s"
            % (
                contest.name,
                contest.rule,
                usefulfuncs.runtimee(contest.starttime),
                usefulfuncs.runtimee(contest.endtime),
            )
        )
        root.update()
        new.destroy()

    qbuttonnew = ttk.Button(new, text="确认", command=gomust)
    qbuttonnew.place(x=160, y=280)


inforbutton = ttk.Button(root, text="修改基本信息", command=change)
inforbutton.place(x=850, y=80)

tableframe = Frame(root)
columns = ["id", "name"]
table = ttk.Treeview(tableframe, height=5, columns=columns, show="headings")
table.column("id", width=3, minwidth=3, anchor=W)
table.column("name", width=30, minwidth=50, anchor=W)
table.pack(anchor=W, ipadx=100, ipady=233, side=LEFT, expand=True, fill=BOTH)
vbar1 = ttk.Scrollbar(table, orient=VERTICAL, command=table.yview)
table.configure(yscrollcommand=vbar1.set)
vbar1.pack(side=RIGHT, fill=Y)


normallabel.place(x=root.winfo_width() / 2 - 175, y=20)
informationlabel.place(x=20, y=80)
informationslabel.place(x=150, y=84)
tableframe.place(x=20, y=110)

problemframe = Frame(root, width=650, height=450)


namelabels = Label(problemframe, text="题目编号")
namelabels.place(x=0, y=0)
namelabent = ttk.Entry(problemframe)
namelabent.place(x=60, y=0)

namerlabels = Label(problemframe, text="题目名称")
namerlabels.place(x=230, y=0)
namerlabent = ttk.Entry(problemframe, width=50)
namerlabent.place(x=290, y=0)

setmarklabella = Label(problemframe, text="题目描述（支持Markdown、Latex）")
setmarklabella.place(x=0, y=25)
setmarklabel = Text(problemframe, width=90, height=12, undo=True)
setmarklabel.place(x=0, y=50)

# setmarklabella = Label(problemframe,text="Markdown渲染")
# setmarklabella.place(x=365,y=25)

global webview
webview = 0

# def gotogoto(*args):
#     try:
#         window.wkeDestroyWebView(webview)
#     except Exception:
#         pass
#     webview = window.wkeCreateWebWindow(2,problemframe.winfo_id(),365,50,285,160)
#     mb.wkeLoadHTMLW(webview,usefulfuncs.getmarkhtml(setmarklabel.get('0.0','end')))
#     window.wkeShowWindow(webview)
#     problemframe.update()
#     root.update()

# gotogoto()

# setbutton = ttk.Button(problemframe,text="预览",width=10,command=gotogoto)
# setbutton.place(x=285,y=125)

efunclab = Label(problemframe, text="评测方式")
efunclab.place(x=0, y=215)
ectvarrul = StringVar()
efctrulen = ttk.Combobox(problemframe, state="readonly", textvariable=ectvarrul)
efctrulen["values"] = ["全文比较（过滤空格与回车）", "Special Judge", "交互题", "提交答案题"]
efctrulen.set("全文比较（过滤空格与回车）")
efctrulen.place(x=60, y=215)

etableframe = Frame(problemframe, width=650, height=100)
rccolumns = ["code", "timelimit", "memorylimit", "score"]
mtable = ttk.Treeview(etableframe, height=5, columns=rccolumns, show="headings")
mtable.heading("code", text="数据编号")
mtable.heading("timelimit", text="时间限制(ms)")
mtable.heading("memorylimit", text="空间限制(MB)")
mtable.heading("score", text="数据分值")
mtable.column("code", width=30, minwidth=50, anchor=S)
mtable.column("timelimit", width=30, minwidth=50, anchor=S)
mtable.column("memorylimit", width=30, minwidth=50, anchor=S)
mtable.column("score", width=30, minwidth=50, anchor=S)
mtable.pack(anchor=W, ipadx=313, ipady=50, side=LEFT, expand=True, fill=BOTH)
vcbar1 = ttk.Scrollbar(mtable, orient=VERTICAL, command=mtable.yview)
mtable.configure(yscrollcommand=vcbar1.set)
vcbar1.pack(side=RIGHT, fill=Y)
etableframe.place(x=0, y=250)

global thisdatas
thisdatas = {}


def newdata(isChange):
    if isChange and not mtable.focus():
        messagebox.showinfo("Nomel", "请先选择一个数据再进行修改！", parent=root)
        return
    nredatatk = Toplevel()
    nredatatk.title("添加数据")
    nredatatk.iconbitmap("icon.ico")
    nredatatk.geometry("500x355+150+150")

    edatalab = Label(nredatatk, text="数据编号")
    edatalab.place(x=5, y=5)
    ecodeent = Entry(nredatatk)
    ecodeent.place(x=90, y=5)
    kedatalab = Label(nredatatk, text="数据分值")
    kedatalab.place(x=250, y=5)
    kecodeent = Entry(nredatatk)
    kecodeent.place(x=340, y=5)

    cinlab = Label(nredatatk, text="输入数据")
    cinlab.place(x=5, y=35)
    cincin = Text(nredatatk, width=60, height=5)
    cincin.place(x=10, y=55)
    ccinlab = Label(nredatatk, text="输出数据")
    ccinlab.place(x=5, y=138)
    ccincin = Text(nredatatk, width=60, height=5)
    ccincin.place(x=10, y=158)

    tmeedatalab = Label(nredatatk, text="时间限制(ms)")
    tmeedatalab.place(x=5, y=233)
    tmeecodeent = Entry(nredatatk)
    tmeecodeent.place(x=90, y=233)
    memedatalab = Label(nredatatk, text="空间限制(MB)")
    memedatalab.place(x=250, y=233)
    memecodeent = Entry(nredatatk)
    memecodeent.place(x=340, y=233)

    ccoder = mtable.focus()

    if isChange:
        eccoder = mtable.set(ccoder)["code"]
        ecodeent.insert(0, eccoder)
        kecodeent.insert(0, thisdatas[eccoder]["score"])
        cincin.insert("0.0", thisdatas[eccoder]["data"])
        ccincin.insert("0.0", thisdatas[eccoder]["ans"])
        tmeecodeent.insert(0, thisdatas[eccoder]["timelimit"])
        memecodeent.insert(0, thisdatas[eccoder]["memorylimit"])

    contenlab = Label(
        nredatatk,
        text="注意：交互题请将程序源代码放在“输入数据”中，“输出数据”留空；\n   SPJ请将程序源代码放在“输出数据”中\n   提交答案题请将答案放在“输出数据”中，“输入数据”留空。",
    )
    contenlab.place(x=5, y=270)

    def okbuttongo(*args):
        if not ecodeent.get():
            messagebox.showerror("Nomel 0x0A00207E", "题目编号未填写", parent=root)
            return
        try:
            tl = float(tmeecodeent.get())
        except ValueError:
            messagebox.showerror("Nomel 0x0A00207A", "时间限制未填写或不符合格式", parent=root)
            return
        try:
            ml = float(memecodeent.get())
        except ValueError:
            messagebox.showerror("Nomel 0x0A00207B", "空间限制未填写或不符合格式", parent=root)
            return
        thisdatas[ecodeent.get()] = {
            "data": cincin.get("0.0", END),
            "timelimit": tl,
            "memorylimit": ml,
            "ans": ccincin.get("0.0", END),
            "score": kecodeent.get(),
        }
        if isChange:
            mtable.delete(ccoder)
        mtable.insert(
            "",
            END,
            values=[
                ecodeent.get(),
                thisdatas[ecodeent.get()]["timelimit"],
                thisdatas[ecodeent.get()]["memorylimit"],
                thisdatas[ecodeent.get()]["score"],
            ],
        )
        nredatatk.destroy()

    okbuttonlabt = ttk.Button(nredatatk, text="确定", command=okbuttongo)
    okbuttonlabt.place(x=400, y=325)


errnewdata = ttk.Button(problemframe, text="修改数据", command=lambda: newdata(True))
errnewdata.place(x=450, y=215)
enewdata = ttk.Button(problemframe, text="添加数据", command=lambda: newdata(False))
enewdata.place(x=550, y=215)

problemframe.place(x=270, y=120)
problemframe.place_forget()


def showit():
    problemframe.place(x=270, y=120)


def newproblem(go):
    global thisdatas
    if go or messagebox.askyesno(
        "Nomel", "如果您现在正在编辑一个题目并没有保存的话，\n打开该题目会导致您的更改被舍弃。\n您真的要新建题目吗？", parent=root
    ):
        thisdatas = {}
        namelabent.delete(0, END)
        namerlabent.delete(0, END)
        setmarklabel.delete("0.0", END)
        # gotogoto()
        efctrulen.set("全文比较（过滤空格与回车）")
        for item in mtable.get_children():
            mtable.delete(item)
        showit()


for i in contest.problems:
    table.insert("", END, values=[i, contest.problems[i].name])


etlist = {"FTC": "全文比较（过滤空格与回车）", "SPJ": "Special Judge", "SAQ": "交互题", "IQ": "提交答案题"}
retlist = {"全文比较（过滤空格与回车）": "FTC", "Special Judge": "SPJ", "交互题": "SAQ", "提交答案题": "IQ"}


def saveproblem(*args):
    if not namelabent.get() or not namerlabent.get():
        messagebox.showinfo("Nomel", "请您先填写题目基本信息", parent=root)
        return
    problem = createcontest.Problem(namerlabent.get(), retlist[efctrulen.get()])
    problem.setproblem(setmarklabel.get("0.0", END))
    problem.data = thisdatas
    contest.newproblem(problem, namelabent.get())
    table.delete(*table.get_children())
    for i in contest.problems:
        table.insert("", END, values=[i, contest.problems[i].name])
    newproblem(True)


def openproblem(*args):
    global thisdatas
    if table.focus() and messagebox.askyesno(
        "Nomel", "如果您现在正在编辑一个题目并没有保存的话，\n打开该题目会导致您的更改被舍弃。\n您真的要打开题目吗？", parent=root
    ):
        nowpro = table.set(table.focus())["id"]
        newproblem(True)
        namelabent.insert(0, nowpro)
        namerlabent.insert(0, contest.problems[nowpro].name)
        setmarklabel.insert("0.0", contest.problems[nowpro].description)
        efctrulen.set(etlist[contest.problems[nowpro].judgeway])
        for i in contest.problems[nowpro].data:
            mtable.insert(
                "",
                END,
                values=[
                    i,
                    contest.problems[nowpro].data[i]["timelimit"],
                    contest.problems[nowpro].data[i]["memorylimit"],
                    contest.problems[nowpro].data[i]["score"],
                ],
            )
        thisdatas = contest.problems[nowpro].data


def delproblem(*args):
    if table.focus() and messagebox.askyesno(
        "Nomel", "您真的要删除该题目吗？\n该操作无法撤销！", parent=root
    ):
        del contest.problems[table.set(table.focus())["id"]]
        table.delete(table.focus())


def savecontesta(*args):
    contest.save(fname)
    messagebox.showinfo("Nomel", "已成功保存！", parent=root)
    # root.destroy()


denewdata = ttk.Button(root, text="删除题目", command=delproblem)
denewdata.place(x=420, y=570)
oenewdata = ttk.Button(root, text="打开题目", command=openproblem)
oenewdata.place(x=520, y=570)
senewdata = ttk.Button(root, text="保存题目", command=saveproblem)
senewdata.place(x=620, y=570)
enewdata = ttk.Button(root, text="新建题目", command=lambda: newproblem(False))
enewdata.place(x=720, y=570)
savecontestasenewdata = ttk.Button(root, text="保存比赛", command=savecontesta)
savecontestasenewdata.place(x=820, y=570)


def undoundo(*args):
    setmarklabel.edit_undo()


def close(*args):
    if messagebox.askyesno("Nomel", "您真的要关闭比赛编辑窗口吗？\n您的更改可能还未保存", parent=root):
        root.destroy()


setmarklabel.bind("<Control-Key-z>", undoundo)
root.protocol("WM_DELETE_WINDOW", close)

root.mainloop()
