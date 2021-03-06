import random
import simplegui2pygame as simplegui
img=simplegui.load_image("slb.png")
inplay=False
p1=True
p2=False
ls=[]
flag=True

for j in range(427,(22-45),-45):
    if(flag):
        for i in range(22,(427+45),45):
            ls.append([i+0.5,j+0.5])
        flag=False
    else:
        for i in range(427,(22-45),-45):
            ls.append([i+0.5,j+0.5])
        flag=True
        
'''ld=[[22.5,427.5],[67.5,427.5],[112.5,427.5],[157.5,427.5],[202.5,427.5],[247.5,427.5],[292.5,427.5],[337.5,427.5],[382.5,427.5],[427.5,427.5],
[427.5,382.5],[382.5,382.5],[337.5,382.5],[292.5,382.5],[247.5,382.5],[202.5,382.5],[157.5,382.5],[112.5,382.5],[67.5,382.5],[22.5,382.5],
[22.5,337.5],[67.5,337.5],[112.5,337.5],[157.5,337.5],[202.5,337.5],[247.5,337.5],[292.5,337.5],[337.5,337.5],[382.5,337.5],[427.5,337.5],
[427.5,292.5],[382.5,292.5],[337.5,292.5],[292.5,292.5],[247.5,292.5],[202.5,292.5],[157.5,292.5],[112.5,292.5],[67.5,292.5],[22.5,292.5],
[22.5,247.5],[67.5,247.5],[112.5,247.5],[157.5,247.5],[202.5,247.5],[247.5,247.5],[292.5,247.5],[337.5,247.5],[382.5,247.5],[427.5,247.5],
[427.5,202.5],[382.5,202.5],[337.5,202.5],[292.5,202.5],[247.5,202.5],[202.5,202.5],[157.5,202.5],[112.5,202.5],[67.5,202.5],[22.5,202.5],
[22.5,157.5],[67.5,157.5],[112.5,157.5],[157.5,157.5],[202.5,157.5],[247.5,157.5],[292.5,157.5],[337.5,157.5],[382.5,157.5],[427.5,157.5],
[427.5,112.5],[382.5,112.5],[337.5,112.5],[292.5,112.5],[247.5,112.5],[202.5,112.5],[157.5,112.5],[112.5,112.5],[67.5,112.5],[22.5,112.5],
[22.5,67.5],[67.5,67.5],[112.5,67.5],[157.5,67.5],[202.5,67.5],[247.5,67.5],[292.5,67.5],[337.5,67.5],[382.5,67.5],[427.5,67.5],
[427.5,22.5],[382.5,22.5],[337.5,22.5],[292.5,22.5],[247.5,22.5],[202.5,22.5],[157.5,22.5],[112.5,22.5],[67.5,22.5],[22.5,22.5]]'''

d={0:0,1:1,2:2,3:13,4:4,5:5,6:6,7:7,8:30,9:9,10:10,
   11:11,12:12,13:13,14:14,15:15,16:6,17:17,18:18,19:19,20:41,
   21:21,22:22,23:23,24:24,25:25,26:26,27:83,28:28,29:29,30:30,
   31:31,32:32,33:33,34:34,35:35,36:36,37:37,38:38,39:39,40:40,
   41:41,42:42,43:43,44:44,45:45,46:46,47:47,48:48,49:49,50:66,
   51:51,52:52,53:33,54:54,55:55,56:56,57:57,58:58,59:59,60:60,
   61:18,62:62,63:59,64:64,65:65,66:66,67:67,68:68,69:69,70:70,
   71:90,72:72,73:73,74:74,75:75,76:76,77:77,78:78,79:98,80:80,
   81:81,82:82,83:83,84:84,85:85,86:35,87:87,88:88,89:89,90:90,
   91:91,92:72,93:93,94:74,95:95,96:96,97:78,98:98,99:99}

a=0
b=0

def p1():
    global a,d,inplay,p1,p2,ls
    if(p1):
        label.set_text("Turn: Player 2")
        inplay=True
        p1=False
        p2=True
        n=random.randint(1,6)
        a=a+n
        if(a in d):
            a=d[a]
        if(a>99):
            a=99-(a-99)
            a=d[a]
        if(a==99):
            inplay=False
            p1=False
            p2=False
            
def p2():
    global b,d,inplay,p1,p2
    if(p2):
        label.set_text("Turn: Player 1")
        inplay=True
        p2=False
        p1=True
        n=random.randint(1,6)
        b=b+n
        if(b in d):
            b=d[b]
        if(b>99):
            b=99-(b-99)
            b=d[b]
        if(b==99):
            inplay=False
            p1=False
            p2=False
            
            
def draw(canvas):
    global ls,a,b,inplay,p1,p2
    canvas.draw_image(img,[225,225],[450,450],[225,225],[450,450])
    canvas.draw_circle(ls[a],10,1,"Black","Blue")
    canvas.draw_circle(ls[b],10,1,"Black","Pink")
    
    if(inplay==False and p1==False and p2==False):
        if(a==99):
            canvas.draw_circle(ls[99],10,1,"Black","Blue")
            canvas.draw_text("Player 1 wins!!",[100,225],50,"Blue")
        if(b==99):
            canvas.draw_circle(ls[99],10,1,"Black","Pink")
            canvas.draw_text("Player 2 wins!!",[100,225],50,"Blue")
            
    if(inplay==True):
        canvas.draw_circle(ls[a],10,1,"Black","Blue")
        canvas.draw_circle(ls[b],10,1,"Black","Pink")
        
frame=simplegui.create_frame("S&L",450,450)
frame.add_button("Player 1",p1)
frame.add_button("Player 2",p2)
label=frame.add_label("Turn: Player 1")
frame.set_draw_handler(draw)
frame.start()
            
