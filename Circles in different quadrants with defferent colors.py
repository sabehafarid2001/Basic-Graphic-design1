from OpenGL.GL import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLUT.fonts import GLUT_BITMAP_HELVETICA_18
import random
import time
import math
from math import sqrt

centerX=256
centerY=256
flag=True
width=512
height=512
in_rad=10
out_rad=60

pulsating=True
pulsating_direction=1
pulsating_speed=0.1

colors=[(1,1,0),(0,1,0),(1,0,0),(0,0,1)]

def midpoint_line(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1#
    if x1 < x2:
        change_x = 1
    else:
        change_x=-1

    if y1 < y2:
        change_y = 1# up
    else:
        change_y=-1
    incr=dx-dy
    count=0
    while True:
        if count%20<10:
            glVertex2f(x1,y1)
        if x1==x2 and y1==y2:
            break
        e2=2*incr
        if e2>-dy:
            incr-=dy
            x1+=change_x
        if e2<dx:
            incr+=dx
            y1+=change_y
        count+=1
color=[1,1,1]
def midpointcircle(radius, centerX=0, centerY=0,color=(1,1,1),flag=False):
    x=0
    y=radius
    d=1-radius
    glColor3f(*color)
    while x<y:
        plot_point(centerX,centerY,x,y,flag)
        x+=1
        if d<0:
            d+=2*x+1
        else:
            y-=1
            d+=2*(x-y)+1
#==============

def plot_point(centerX,centerY,x,y,flag):
        point=[(centerX+x,centerY+y),(centerX-x,centerY+y),(centerX+x,centerY-y),(centerX-x,centerY-y),(centerX+y,centerY+x),(centerX-y,centerY+x),(centerX+y,centerY-x),(centerX-y,centerY-x)]
        for i ,j in point:
            if flag:
                i%=512
                j%=512
            glVertex2f(i,j)


def quad(x,y):
    if x>245 and y>256:
        return 0#quad 1
    elif x<256 and y>256:
        return 1#zone 2
    elif x<256 and y<256:
        return 2#zone 3
    elif x>256 and y<256:
        return 3

    else:# zone 4
        return 0

def specialKeyListener(key,x,y):
    global centerX,centerY
    move_x=4
    move_y=4
    if key==GLUT_KEY_RIGHT:
        centerX+=move_x
    elif key==GLUT_KEY_LEFT:
        centerX-=move_x
    elif key==GLUT_KEY_UP:
        centerY+=move_y
    elif key==GLUT_KEY_DOWN:
        centerY-=move_y
    glutPostRedisplay()


def keyboardListener(key, _, __):

    global pulsating
    if key == b' ':
        pulsating=not pulsating


def mouseListener(button,state,x,y):
    global pulsating,centerX,centerY
    if button ==GLUT_RIGHT_BUTTON and state ==GLUT_DOWN:

        centerX=x
        centerY=512-y
def animate():
    global in_rad,out_rad,pulsating,pulsating_speed,pulsating_direction

    if pulsating==True:
        out_rad+=pulsating_speed*pulsating_direction
        if out_rad>=100 or out_rad<=10:
            pulsating_direction*=-1

    glutPostRedisplay()
def showScreen():
    global in_rad,out_rad,pulsating,pulsating_speed,pulsating_direction


    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    glColor3f(1,1,1)
    midpoint_line(0,256,512,256)
    midpoint_line(256,0,256,512)
    midpointcircle(in_rad,centerX,centerY,(1,1,1),flag)
    quadrant_clr=colors[quad(centerX,centerY)]
    midpointcircle(out_rad,centerX,centerY,quadrant_clr,flag=True)
    glEnd()


    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(512,512)
glutCreateWindow(b"create circle in four quadrant")

glClearColor(0, 0, 0, 1)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0,512,0,512,0,1)

glutIdleFunc(showScreen)
glutIdleFunc(animate)
glutDisplayFunc(showScreen)


glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()









