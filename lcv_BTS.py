from copy import deepcopy
from prints import printTable
from tests import mrv_addTest,finalTest,mrv_recover
def lcv_BTS(table,variables,hints):
    # printTable(table)
    iteration=0
    newTable=deepcopy(table)
    path=[]
    unsigned=deepcopy(variables)
    stack=[]
    newNode,result=new_node(newTable,hints,unsigned[0])
    if result==-1:
        stack.append([newNode,0,-1])
        stack.append([newNode,1,0])
    else:
        #print(newNode)
        stack.append([newNode,1,-1])
        stack.append([newNode,0,0])
    while stack:
        iteration+=1
        current=stack.pop()
        path.append(current)
        # print(current)
        unsigned.remove(current[0])
        test=mrv_addTest(newTable,current,hints)
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
                newNode,result=new_node(newTable,hints,unsigned[0])
                if result==-1:
                    stack.append([newNode,0,-1])
                    stack.append([newNode,1,0])
                else:
                    stack.append([newNode,1,-1])
                    stack.append([newNode,0,0])
    for hint in hints:
        newTable[hint[0]][hint[1]]=table[hint[0]][hint[1]]
    # print(stack)
    printTable(newTable,iteration)
    print(iteration)

def new_node(newTable,hints,current):
    count=0
    for i in range(-1,2):
        for j in range(-1,2):
            if(current[0]+i>=0 and current[0]+i<len(newTable[0]) and current[1]+j>=0 and current[1]+j<len(newTable)):
                if [current[0]+i,current[1]+j] in hints:
                    if newTable[current[0]+i][current[1]+j]==2 or newTable[current[0]+i][current[1]+j]==1:
                        count+=1
    if count==0:
        return current,-1
    else:
        return current,0

