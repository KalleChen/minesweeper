# when adding new variable test the hints near it
total=0
def easy_addTest(table,info,hints):
    x=info[0][0]
    y=info[0][1]
    sign=info[1]
    check=True
    for i in range(-1,2):
        for j in range(-1,2):
            if([x+i,y+j] in hints):
                if(sign==1):
                    table[x+i][y+j]-=1
                    if table[x+i][y+j]<0:
                        check=False
                else:
                    table[x+i][y+j]+=1
    if sign==1:
        table[x][y]='*'
    else:
        table[x][y]=-1
    return check

# when adding new variable test the hints near it
def mrv_addTest(table,info,hints):
    x=info[0][0]
    y=info[0][1]
    sign=info[1]
    check=True
    for i in range(-1,2):
        for j in range(-1,2):
            if([x+i,y+j] in hints):
                if(sign==1):
                    table[x+i][y+j]-=1
                    if table[x+i][y+j]<0:
                        check=False
    if sign==1:
        table[x][y]='*'
    else:
        table[x][y]=-1
    return check

# when backtracking recover hints
def mrv_recover(table,info,hints):
    x=info[0][0]
    y=info[0][1]
    sign=info[1]
    if sign==1:
        for i in range(-1,2):
            for j in range(-1,2):
                if [x+i,y+j] in hints:
                    table[x+i][y+j]+=1


# test the all hints
def finalTest(newTable,table,hints):
    # printTable(table)
    global total
    for hint in hints:
        count=0
        for i in range(-1,2):
            for j in range(-1,2):
                if(hint[0]+i>=0 and hint[0]+i<len(table[0]) and hint[1]+j>=0 and hint[1]+j<len(table)):
                    if(newTable[hint[0]+i][hint[1]+j]=='*'):
                        count+=1
        if count!=table[hint[0]][hint[1]]:
            return False
    count=0
    for row in newTable:
        for element in row:
            if element=='*':
                count+=1
    if count!=total:
        return False
    return True

def update_total(tot):
    global total
    total=tot