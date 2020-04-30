from PIL import Image, ImageDraw
name=''
img = Image.new("RGB", (300, 1320))
img1 = ImageDraw.Draw(img)  
pos=(0,0)
def printTable(table,iteration):
    global name
    # img = Image.new("RGB", (1500, 330))
    # img1 = ImageDraw.Draw(img)
    global img1  
    global pos
    img1.rectangle([pos,(pos[0]+300,pos[1]+30)],fill='white')
    pos=(pos[0],pos[1]+30)
    img1.text((pos[0],pos[1]-15),"function: "+str(name)+"  iterations: "+str(iteration),fill='black')
    print(name)
    for row in table:
        for element in row:
            if(len(str(element))==1):
                print('',element,end=' ')
            else:
                print(element,end=' ')
            if element=='*':
                img1.rectangle([pos,(pos[0]+300/len(table),pos[1]+300/len(table))], fill ="red", outline ="black")
            elif element==-1:
                img1.rectangle([pos,(pos[0]+300/len(table),pos[1]+300/len(table))], fill ="white", outline ="black")
            else:
                img1.rectangle([pos,(pos[0]+300/len(table),pos[1]+300/len(table))], fill ="yellow", outline ="black")
                img1.text((pos[0]+150/len(table),pos[1]+150/len(table)),str(element),fill="black")
            pos=(pos[0]+300/len(table),pos[1])
        print()
        pos=(0,pos[1]+300/len(table))
    # img.show() 

def update_name(n):
    global name
    name=n

def show_image():
    global img
    img.show() 