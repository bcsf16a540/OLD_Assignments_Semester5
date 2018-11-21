ProcessList=[]
print("Enter the Number of Process: ")
n=int(input())
for i in range(0,n):
    procInfo={}
    procInfo["Number"]=i+1
    procInfo["BT"]=int(input("Brust Time for process "+str(i+1)+" :"))
    ProcessList.append(procInfo)

ProcessList=sorted(ProcessList,key=lambda x: x["BT"])
Total_BT=0
for process in ProcessList:
    Total_BT+=process["BT"]
AVG_BT=Total_BT/len(ProcessList)

x=0
process=ProcessList[x]
ending_time=process["BT"]
Waiting_time=[]
Waiting_time.append(0)
for i in range (1,Total_BT+1):
    if(ending_time==i):
        print(process["Number"],end="")
        x+=1
        Waiting_time.append(i)
        if(x<len(ProcessList)):
            process=ProcessList[x]
            ending_time+=process["BT"]
    else:
        print("_",end="")
        
print("\n\nAVERAGE Waiting Time = "+str(sum(Waiting_time)/n)+"\n")