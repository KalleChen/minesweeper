from copy import deepcopy
from prints import printTable
from tests import mrv_addTest,finalTest,mrv_recover
from forward_BTS import forward_checking
def mrv_BTS(table,variables,hints):
    # printTable(table)
    iteration=0
    newTable=deepcopy(table)
    path=[]
    unsigned=deepcopy(variables)
    stack=[]
    newNode,result=find_min(newTable,hints,unsigned)
    if result==-1:
        stack.append([newNode,0,-1])
        stack.append([newNode,1,0])
    else:
        #print(newNode)
        stack.append([newNode,result,-1])
    while stack:
        current=stack.pop()
        iteration+=1
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
                newNode,result=find_min(newTable,hints,unsigned)
                if result==-1:
                    stack.append([newNode,0,-1])
                    stack.append([newNode,1,0])
                else:
                    stack.append([newNode,result,-1])
    for hint in hints:
        newTable[hint[0]][hint[1]]=table[hint[0]][hint[1]]
    # print(stack)
    printTable(newTable,iteration)
    print(iteration)

def find_min(newTable,hints,unsigned):
    # printTable(newTable)
    # print(hints)
    for hint in hints:
        if newTable[hint[0]][hint[1]]==0:
            for i in range(-1,2):
                for j in range(-1,2):
                    if(hint[0]+i>=0 and hint[0]+i<len(newTable[0]) and hint[1]+j>=0 and hint[1]+j<len(newTable)):
                        if [hint[0]+i,hint[1]+j] in unsigned:
                            # print([hint[0]+i,hint[1]+j],hint)
                            return [hint[0]+i,hint[1]+j],0
        if newTable[hint[0]][hint[1]]==1:
            current_x=-1
            current_y=-1
            for i in range(-1,2):
                for j in range(-1,2):
                    if(hint[0]+i>=0 and hint[0]+i<len(newTable[0]) and hint[1]+j>=0 and hint[1]+j<len(newTable)):
                        if [hint[0]+i,hint[1]+j] in unsigned:
                            if current_x==-1:
                                current_x=hint[0]+i
                                current_y=hint[1]+j
                            else:
                                return unsigned[0],-1
            if current_x!=-1:
                # print(hint,current_x,current_y)
                # printTable(newTable)
                return [current_x,current_y],1
    return unsigned[0],-1