from turtle import *
from FPS import FPS
import random
class Bar:
    def __init__(self,value,r=0.5,g=0.7,b=1):
        self.bar = Turtle()
        self.bar.speed(0)
        self.bar.shape("square")
        self.bar.shapesize(stretch_wid= value/20, stretch_len= 1)
        self.bar.color(r,g,b)
        self.bar.penup()
        self.value = value
        self.posx = 0
        self.posy = 0
    
    def GoTo(self,x,y):
        self.bar.goto(x,y)
        self.posx = x
        self.posy = y

def swap (barsay, o , p):
    barsay[o].posx, barsay[p].posx = barsay[p].posx, barsay[o].posx
    barsay[o].GoTo(barsay[o].posx,barsay[o].posy)
    barsay[p].GoTo(barsay[p].posx,barsay[p].posy)
    barsay[o],barsay[p] = barsay[p],barsay[o]

def insert(barsay,o,p):
    x = barsay[o].posx
    y = barsay[o].posy
    barsay[o] = Bar(barsay[p].value)
    barsay[o].GoTo(x,y)
    window.update()


#Tester Code 
def createWindow (gap):
    bars = []
    j = 0
    x = 20
    for i in range(-490, 500, gap):
        bars.append(Bar(random.randint(20,2000))) #
        x+= 50
        bars[j].GoTo(i,-500)
        j += 1
    return bars




window = Screen()
window.title("Bubble Sort")
window.bgcolor(0,0,0.2)
window.setup(width=1000,height=1000)
window.tracer(0)
bars = createWindow(30)



    
fp = FPS()
fp.fpsLimit(10)
n = len(bars)
window.update()
for i in range(n//2):
    bars[i].bar.color(1,0,0)
    bars[n-1-i].bar.color(1,0,0)
    window.update()
    fp.fpsLimit(10)
    swap(bars,i,n-i-1)
    # bars[i], bars[n-i-1] = bars[n-i-1],bars[i]
    bars[i].bar.color(1,1,1)
    bars[n-1-i].bar.color(1,1,1)
    fp.fpsLimit(10)
    window.update()


for i in bars:
    i.bar.color(0.5,0.7,1)
    window.update()
    fp.fpsLimit(15)


# BUBBLE SORT
speed = 60
for i in range(n):

    for j in range(0, n - i - 1):
        bars[j].bar.color(1,0,0)
        bars[j+1].bar.color(1,0,0)
        window.update()
        fp.fpsLimit(speed)
        if bars[j].value > bars[j + 1].value:
            bars[j].bar.color(1,1,0)
            bars[j+1].bar.color(1,1,0)
            window.update()
            fp.fpsLimit(2*speed)
            swap(bars,j,j+1)
            fp.fpsLimit(speed)
            window.update()
        bars[j].bar.color(0.5,0.7,1)
        bars[j+1].bar.color(1,1,1)
        window.update()
            


for i in bars:
    i.bar.color(0.5,0.7,1)
    window.update()
    fp.fpsLimit(15)

window.clearscreen()
window.bgcolor(0,0,0.2)
window.title("Insertion Sort")
bars = createWindow(30)

#INSERTION SORT
# speed = 20

for i in range(n):
    
    min_idx = i
    bars[i].bar.color(0,0,1)
    for j in range(i+1, n):
        bars[j].bar.color(1,0,0)
        window.update()
        fp.fpsLimit(speed)
        if bars[min_idx].value > bars[j].value:
            bars[min_idx].bar.color(0.5,0.7,1)
            min_idx = j
            bars[min_idx].bar.color(0,0,1)
            window.update()
        bars[j].bar.color(0.5,0.7,1)
        bars[min_idx].bar.color(0,0,1)
        # bars[i].bar.color(0.5,0.7,1)
        window.update()
    bars[min_idx].bar.color(1,1,1)
    window.update()
    swap(bars,i,min_idx)    
    fp.fpsLimit(speed)
    window.update()  
    #A[i], A[min_idx] = A[min_idx], A[i]


for i in bars:
    i.bar.color(0.5,0.7,1)
    window.update()
    fp.fpsLimit(15)
