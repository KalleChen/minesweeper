# def cmp(e):
#     return e[1]
# a=[[1,2],[10,1],[1,6],[1,3]]
# print(a)
# a,index=min(a,key=cmp)
# print(a,index)
# x=2
# print(x== 2 or x==1)
from PIL import ImageDraw,Image
img = Image.new("RGB", (300, 300))
img1 = ImageDraw.Draw(img)   
pos=(0,0)
for row in range(6):
        for element in range(6):
            if(len(str(element))==1):
                print('',element,end=' ')
            else:
                print(element,end=' ')
            img1.rectangle([pos,(pos[0]+300/6,pos[1]+300/6)], fill ="yellow", outline ="red")
            pos=(pos[0]+300/6,pos[1])
        print()
        pos=(0,pos[1]+300/6)
img.show() 