print("Enter the number of processes: ")
No_of_processes=int(input())
processes=[]
for i in range(0,No_of_processes):
    processes.insert(i,i+1)
Arrival_Time=[]
Brust_time=[]
for i in range (0,No_of_processes):
    print("Enter the Burst time and then Arrival for Process " + str(i+1) + ": ")
    Ith_Burst_time=int(input())
    arrival=int(input())
    Brust_time.insert(i,Ith_Burst_time)
    Arrival_Time.insert(i,arrival)

for i in range(0,No_of_processes-1):
    for j in range(0,No_of_processes-1):
        if(Arrival_Time[j]>Arrival_Time[j+1]):
            swap=Arrival_Time[j]
            Arrival_Time[j]=Arrival_Time[j+1]
            Arrival_Time[j+1]=swap
            swap=Brust_time[j]
            Brust_time[j]=Brust_time[j+1]
            Brust_time[j+1]=swap
            swap=processes[j]
            processes[j]=processes[j+1]
            processes[j+1]=swap
            #I'm trying to swap the three arrays on the basis of the priority.

Total_Required_Time=0
Running_Sum_of_time=[]
for i in range(0,No_of_processes):
    Running_Sum_of_time.insert(i,0)
for i in range(0,No_of_processes):
    Total_Required_Time+=Brust_time[i]
for j in range(0,No_of_processes):
    sum=0
    for k in range(0,j+1):
        sum+=Brust_time[k]
    Running_Sum_of_time[j]=sum

Waiting_Time=[]
for i in range(0,No_of_processes):
    Waiting_Time.insert(i,0)
for j in range(0,No_of_processes):
    sum=0
    for k in range(0,j):
        sum+=Brust_time[k]
    Waiting_Time[j]=sum

k=0
for i in range(1,Total_Required_Time+1):
    if(i==Running_Sum_of_time[k]):
        print("_",end="")
        print(processes[k],end="")
        k+=1
    else:
        print("_",end="")
print("\n")
avg_Waiting=0
avg_Turnaround=0
TurnAroundTime=[]
for i in range(0,No_of_processes):
    TurnAroundTime.insert(i,Running_Sum_of_time[i]-Arrival_Time[i])

print("Process_No.\tWaiting_Time\tTurnaround_Time")
for i in range(0,No_of_processes):
    print(processes[i],end="\t\t")
    print(Waiting_Time[i],end="\t\t")
    print(TurnAroundTime[i],end="\n")
    avg_Waiting+=Waiting_Time[i]
    avg_Turnaround+=TurnAroundTime[i]
print("\n")
avg_Waiting=avg_Waiting/No_of_processes
avg_Turnaround=avg_Turnaround/No_of_processes
print("Average Waiting Time: "+str(avg_Waiting)+"\n")
print("Average TurnAround Time: "+str(avg_Turnaround)+"\n")

