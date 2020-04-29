from tests import easy_addTest,finalTest
from copy import deepcopy
from prints import printTable
def easy_BTS(table,variables,hints):
    iteration=0
    stack=[[variables[0],0],[variables[0],1]]
    newTable=deepcopy(table)
    unsignVariables=0
    path=[]
    while stack:
        current=stack.pop()
        iteration+=1
        path.append(current)
        unsignVariables+=1
        test=easy_addTest(newTable,current,hints)
        if(test==False):
            while path:
                delete=path.pop()
                unsignVariables-=1
                newTable[delete[0][0]][delete[0][1]]=-1
                if delete[1]==1:
                    break
            continue
        else:
            if(unsignVariables==len(variables)):
                test=finalTest(newTable,table,hints)
                if(test==False):
                    while path:
                        delete=path.pop()
                        unsignVariables-=1
                        newTable[delete[0][0]][delete[0][1]]=-1
                        if delete[1]==1:
                            break
                    continue
                else:
                    break
            else:
                stack.append([variables[unsignVariables],0])
                stack.append([variables[unsignVariables],1])
    for hint in hints:
        newTable[hint[0]][hint[1]]=table[hint[0]][hint[1]]
    printTable(newTable,iteration)
    print(iteration)