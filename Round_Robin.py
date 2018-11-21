ProcessList=[]
n=int(input("Enter The Numbe of Processes: "))
Quantum=int(input("Enter Time Quantum: "))

for i in range(0,n):
    procInfo={}
    procInfo["Number"]=i+1
    procInfo["BT"]=int(input("Brust Time for process "+str(i+1)+": "))
    procInfo["AT"]=int(input("Arrival Time for process "+str(i+1)+": "))
    procInfo["Time"]=0
    procInfo["Current_RunningTime"]=0
    procInfo["To_Waiting"]=int(input("Time after which process "+str(i+1)+"goes to waiting: "))
    procInfo["From_Waiting"]=int(input("Waiting Time in I/O: "))
    procInfo["Current_Waiting"]=0
    procInfo["ET"]=0
    ProcessList.append(procInfo)

Ready=[]
waiting=[]
Running=[]
check=1;
i=0
k=0
r=0
while(check==1):
    for j in range(0,n):
        if(i==ProcessList[j]["AT"]):
            ProcessList[j]["To_Waiting"]+=i
            Ready.append(ProcessList[j])
    if(Running==[] and Ready!=[]):
        Ready[k]["Time"]=i+Quantum
        Running.insert(r,Ready[k])
    if(Ready!=[]):
        for process in Running:
            if(process["To_Waiting"]==i):
                process["Current_Waiting"]=i+process["From_Waiting"]
                waiting.append(process)
                Running.remove(process)
        for process in waiting:
            if(i==process["Current_Waiting"]):
                Ready.append(process)
                waiting.remove(process)
        for process in Running:
            if(process["BT"]==0):
                print(process["Number"],end="")
                process["ET"]=i
                r=r+1
            elif(process["Time"]==0):
                Ready[k]["Time"]=i+Quantum
                Running.insert(r,Ready[k])
            else:
                Running[k]["BT"]-=1
                Running[k]["Time"]-=1
                print("_",end="")
    x=0
    for process in ProcessList:
        if(process["BT"]==0):
            x+=1
    if (x==len(ProcessList)):
        check=0;
i+=1
