from copy import deepcopy
from prints import printTable
from tests import mrv_addTest,finalTest,mrv_recover
def forward_BTS(table,variables,hints):
    # printTable(table)
    iteration=0
    newTable=deepcopy(table)
    path=[]
    unsigned=deepcopy(variables)
    stack=[[variables[0],0,-1],[variables[0],1,0]]
    while stack:
        current=stack.pop()
        iteration+=1
        path.append(current)
        # print(current)
        unsigned.remove(current[0])
        test=forward_checking(newTable,current,hints,unsigned,path)
        # if current[0]==[3,5]:
        #     print(test)
        if(test==False):
            while path:
                delete=path.pop()
                unsigned.append(delete[0])
                mrv_recover(newTable,delete,hints)
                if delete[2]==0:
                    break
            continue
        else:
            if len(unsigned)==0:
                test=finalTest(newTable,table,hints)
                if(test==False):
                    while path:
                        delete=path.pop()
                        unsigned.append(delete[0])
                        mrv_recover(newTable,delete,hints)
                        if delete[2]==0:
                            break
                    continue
                else:
                    break
            else:
                stack.append([unsigned[0],0,-1])
                stack.append([unsigned[0],1,0])
    for hint in hints:
        newTable[hint[0]][hint[1]]=table[hint[0]][hint[1]]
    # print(stack)
    printTable(newTable,iteration)
    print(iteration)

def forward_checking(newTable,current,hints,unsigned,path):
    x=current[0][0]
    y=current[0][1]
    sign=current[1]
    check=True
    for i in range(-1,2):
        for j in range(-1,2):
            if([x+i,y+j] in hints):
                if(sign==1):
                    newTable[x+i][y+j]-=1
                    if newTable[x+i][y+j]<0:
                        check=False
                    elif newTable[x+i][y+j]==0:
                        # equal lower bound
                        for l in range(-1,2):
                            for t in range(-1,2):
                                if([x+i+l,y+j+t] in unsigned):
                                    newTable[x+i+l][y+j+t]=-1
                                    path.append([[x+i+l,y+j+t],0,-1])
                                    unsigned.remove([x+i+l,y+j+t])
                    else:
                        upperBound=0
                        for l in range(-1,2):
                            for t in range(-1,2):
                                if([x+i+l,y+j+t] in unsigned):
                                    upperBound+=1
                        if upperBound<newTable[x+i][y+j]:
                            # printTable(newTable)
                            # print(newTable[x+i][y+j],upperBound)
                            # print(current)
                            # print(unsigned)
                            check=False
                        elif upperBound==newTable[x+i][y+j]:
                            
                            # print(1,[x+i,y+j])
                            # printTable(newTable)
                            for l in range(-1,2):
                                for t in range(-1,2):
                                    if([x+i+l,y+j+t] in unsigned):
                                        # print([x+i+l,y+j+t])
                                        newTable[x+i+l][y+j+t]='*'
                                        path.append([[x+i+l,y+j+t],1,-1])
                                        unsigned.remove([x+i+l,y+j+t])
                                        # checktest=forward_checking(newTable,[[x+i+l,y+j+t],1],hints,unsigned,path)
                                        # if checktest==False:
                                        #     check=False
                                        checktest=mrv_addTest(newTable,[[x+i+l,y+j+t],1],hints)
                                        if checktest==False:
                                            check=checktest
    if sign==1:
        newTable[x][y]='*'
    else:
        newTable[x][y]=-1
    return check