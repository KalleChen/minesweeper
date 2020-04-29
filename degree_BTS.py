from copy import deepcopy
from prints import printTable
from tests import easy_addTest,finalTest,mrv_recover
def degree_BTS(table,variables,hints):
    # printTable(table)
    iteration=0
    newTable=deepcopy(table)
    path=[]
    unsigned=deepcopy(variables)
    stack=[]
    degree=degree_init(newTable,hints,variables)
    newNode=find_max(newTable,degree,unsigned,variables)
    stack.append([newNode,0,-1])
    stack.append([newNode,1,0])
    while stack:
        current=stack.pop()
        iteration+=1
        path.append(current)
        unsigned.remove(current[0])
        # print(1)
        test=easy_addTest(newTable,current,hints)
        # if current[0]==[3,5]:
        #     print(test)
        if(test==False):
            while path:
                delete=path.pop()
                unsigned.append(delete[0])
                newTable[delete[0][0]][delete[0][1]]=-1
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
                        newTable[delete[0][0]][delete[0][1]]=-1
                        if delete[2]==0:
                            break
                    continue
                else:
                    break
            else:
                newNode=find_max(newTable,degree,unsigned,variables)
                stack.append([newNode,0,-1])
                stack.append([newNode,1,0])
    for hint in hints:
        newTable[hint[0]][hint[1]]=table[hint[0]][hint[1]]
    # print(stack)
    printTable(newTable,iteration)
    print(iteration)

def cmp(e):
    return e[0]

def find_max(newTable,degree,unsigned,variables):
    newDegree=deepcopy(degree)
    while newDegree:
        m=max(newDegree,key=cmp)
        if variables[m[1]] not in unsigned:
            newDegree.remove(m)
        else:
            return variables[m[1]]

def degree_init(newTable,hints,variables):
    degree=[[0,i] for i in range(len(variables))]
    for hint in hints:
        for i in range(-1,2):
            for j in range(-1,2):
                if [hint[0]+i,hint[1]+j] not in hints:
                    if(hint[0]+i>=0 and hint[0]+i<len(newTable[0]) and hint[1]+j>=0 and hint[1]+j<len(newTable)):
                        degree[variables.index([hint[0]+i,hint[1]+j])][0]+=1
    return degree