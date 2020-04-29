from copy import deepcopy
from easy_BTS import easy_BTS
from mrv_BTS import mrv_BTS
from degree_BTS import degree_BTS
from lcv_BTS import lcv_BTS 
from forward_BTS import forward_BTS
from tests import  update_total
from prints import update_name,show_image
from mrv_forward import mrv_forward
from degree_forward import degree_forward
import time
def main():
    x=input().split()
    for i in range(len(x)):
        x[i]=int(x[i])
    table=[[0 for i in range(int(x[1]))] for j in range(int(x[0]))]
    index=3
    hints=[]
    variables=[]
    update_total(x[2])
    for i in range(int(x[0])):
        for j in range(int(x[1])):
            table[i][j]=int(x[index])
            if(int(x[index])==-1):
                variables.append([i,j])
            else:
                hints.append([i,j])
            index+=1
    update_name("easy_BTS")
    timeStart=time.time()
    easy_BTS(table,variables,hints)
    timeEnd=time.time()
    print(timeEnd-timeStart)
    print()
    update_name("mrv_BTS")
    timeStart=time.time()
    mrv_BTS(table,variables,hints)
    timeEnd=time.time()
    print(timeEnd-timeStart)
    print()
    update_name("degree_BTS")
    timeStart=time.time()
    degree_BTS(table,variables,hints)
    timeEnd=time.time()
    print(timeEnd-timeStart)
    print()
    update_name("lcv_BTS")
    timeStart=time.time()
    lcv_BTS(table,variables,hints)
    timeEnd=time.time()
    print(timeEnd-timeStart)
    print()
    update_name("forward_BTS")
    timeStart=time.time()
    forward_BTS(table,variables,hints)
    timeEnd=time.time()
    print(timeEnd-timeStart)
    # update_name("MRV+forward checking")
    # timeStart=time.time()
    # mrv_forward(table,variables,hints)
    # timeEnd=time.time()
    # print(timeEnd-timeStart)
    # print()
    # update_name("degree+forward checking")
    # timeStart=time.time()
    # degree_forward(table,variables,hints)
    # timeEnd=time.time()
    # print(timeEnd-timeStart)
    # print()
    show_image()


if __name__ == "__main__":
    main()