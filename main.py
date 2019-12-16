# -*- coding: UTF-8 -*-
import os
import json
import sys
import time
from task import Task
taskArr = []
commandArr = []
with open('commandList.txt','r') as f:
    for line in f.readlines():
        txt = line.strip().replace('\n','')
        commandArr.append(txt)
if len(sys.argv) == 2:
    if sys.argv[1] == "-d":
        for cmd in commandArr:
                taskArr.append(Task(cmd))
    if sys.argv[1] == "-b":
        if os.path.exists('eula.txt'):
                with open('eula.txt','w') as f:
                        f.write('eula=true')
                taskArr.append(Task("java -Xms512M -Xmx1024M -jar server.jar nogui"))
        else:
                taskArr.append(Task("java -Xms512M -Xmx1024M -jar server.jar nogui"))
                with open('eula.txt','w') as f:
                        f.write('eula=true')
                taskArr.append(Task("java -Xms512M -Xmx1024M -jar server.jar nogui"))
    if sys.argv[1] == "-h":
        print '-d部署，-b启动'
else:
    print("请输入正确的参数")