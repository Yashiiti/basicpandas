import pandas as pd
import numpy as np
from collections import defaultdict
a=pd.read_excel('input1.xlsx',sheet_name='Sheet1')
b=pd.read_excel('input2.xlsx',sheet_name='Sheet1')
# print(a.head())
d={}
arr1=[]
for i in range(len(b)):
    arr1.append([b['name'][i],b['uid'][i],b['total_statements'][i],b['total_reasons'][i]])

    d[a['Name'][i]]=a['Team Name'][i]
# print(d)
print(arr1)
arr1.sort(key=lambda x: [-x[2],-x[3],x[0]])
arr2=[]
for i in range(len(arr1)):
    arr2.append([i+1]+arr1[i])
df1=pd.DataFrame(arr2,columns=['Rank','Name','UID','No. of Statements','No. of Reasons'])
statement=defaultdict(int)
df1.to_csv('individualleaderboard.csv',index=False)
count=defaultdict(int)
reason=defaultdict(int)
for i in range(len(b)):
   
   
    teamname=d[b['name'][i]]
    count[teamname]+=1
    # print(teamname)
    y=b['total_statements'][i]
    z=b['total_reasons'][i]
    statement[teamname]+=y
    reason[teamname]+=z

    # reason[b['Name'][i]]=b['Reason'][i]

teams={}
for i in statement:
    teams[i]=[i,statement[i]/count[i],reason[i]//count[i]]
# print(teams)
arr=[]
for i in teams:
    arr.append(teams[i])
arr.sort(key=lambda x: x[1]+x[2],reverse=True)
# print(arr)
final=[]
for i in range(len(arr)):
    j=[i+1]+arr[i]
    final.append(j)
print(final)
df=pd.DataFrame(final,columns=['Team Rank','Thinking Teams Leaderboard','Average Statements','Average Reasons'])
df.to_csv('teamleaderboard.csv',index=False)



