from task import Task
taskArr = []
if len(sys.argv) == 2:
    taskArr.append(Task("yum -y install java-1.8.0-openjdk"))
else:
    print("请输入正确的参数")