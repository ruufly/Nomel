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
import os, sys

def settime(year,month,day,hour,minute,second):
    return (int(year),int(month),int(day),int(hour),int(minute),int(second))

def rule(rule):     # IOI / OI
    return rule

def judgeway(way):  # Full text comparison -> (FTC) / Special Judge -> (SPJ) / Submit answer questions -> (SAQ) / Interactive questions -> (IQ)
    return way

class Problem(object):
    def __init__(self,name,judgeway='FTC'):
        self.name = name
        self.timelimit = 0      # ms
        self.memorylimit = 0      # MB
        self.data = {}
        self.description = "暂无本题的描述"
        self.judgeway = judgeway
        self.spj = ""
    def setproblem(self,description):
        self.description = description
    def setdata(self,data,ans,datacode,datatime,datamemory,score):
        self.data[datacode] = {'data':data,'timelimit':datatime,'memorylimit':datamemory,'ans':ans,'score':score}
        self.timelimit = max(datatime,self.timelimit)
        self.memorylimit = max(datamemory,self.memorylimit)

class Contest(object):
    def __init__(self,name,starttime,endtime,rule):
        self.name = name
        self.starttime = starttime
        self.endtime = endtime
        self.rule = rule
        self.password = ""
        self.problems = {}
    def newproblem(self,problem : Problem,proid):
        self.problems[proid] = problem
    def setpassword(self,password):
        self.password = password
    def read(self,file):
        f = open(file,"rb")
        datas = pickle.load(f)
        f.close()
        self.name = datas['name']
        self.starttime = datas['start']
        self.endtime = datas['end']
        self.rule = datas['rule']
        self.password = datas['password']
        for i in datas['problem']:
            problem = Problem(datas['problem'][i]['name'],datas['problem'][i]['judgeway'])
            problem.setproblem(datas['problem'][i]['description'])
            problem.timelimit = datas['problem'][i]['timelimit']
            problem.memorylimit = datas['problem'][i]['memorylimit']
            problem.data = datas['problem'][i]['data']
            self.newproblem(problem,i)
    def save(self,file):
        f = open(file,"wb")
        datas = {'name':self.name,
                 'start':self.starttime,
                 'end':self.endtime,
                 'rule':self.rule,
                 'password':self.password,
                 'problem':{}}
        for i in self.problems:
            datas['problem'][i] = {'name':self.problems[i].name,
                                   'judgeway':self.problems[i].judgeway,
                                   'timelimit':self.problems[i].timelimit,
                                   'memorylimit':self.problems[i].memorylimit,
                                   'description':self.problems[i].description,
                                   'data':self.problems[i].data}
        pickle.dump(datas,f)
        f.close()


if __name__ == "__main__":
    a = Contest("1",(1,1,1,1,1,1),(1,1,1,1,1,1),'OI')
    a.save("lastcontest\\a.nfctmp")
