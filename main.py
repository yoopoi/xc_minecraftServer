# -*- coding: UTF-8 -*-
import os
import json
import sys
import time
from task import Task
taskArr = []
commandArr = []
with open('commandList.txt','r') as f:
    txt = f.read().split("#")
print txt
if len(sys.argv) == 2:
    if sys.argv[1] == "-d":
        taskArr.append(Task("yum -y install java-1.8.0-openjdk"))
        taskArr.append(Task("yum -y install java-1.8.0-openjdk"))
        taskArr.append(Task("yum -y install java-1.8.0-openjdk"))

        
else:
    print("请输入正确的参数")