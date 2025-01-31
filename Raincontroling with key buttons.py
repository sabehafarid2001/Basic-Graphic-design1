from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
#point_x=150
#PIXEL_size=5
import random
rain_move_x=0
arr_rain=[]
house_clr=(0,0,0)
back_clr=(1,1,1,1)
def draw_rain_points(x, y):
    glPointSize(4) #pixel size. by default 1 thake
    glColor3f(1,0,0)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
#jekhane show korbe pixel
    glEnd()
for j in range(100):
   x2=random.uniform(10,400)
   y2=random.uniform(400,600)
   arr_rain.append((x2,y2))
def drawhouse():
    global house_clr
    glColor3f(*house_clr)
    glLineWidth(1)
    glBegin(GL_TRIANGLES)
    glVertex2f(100,300)
    glVertex2f(200,500)
    glVertex2f(300,300)
    glEnd()
# body
   # glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(100,300)
    glVertex2f(100,100)

    glVertex2f(100,100)
    glVertex2f(300,100)

    glVertex2f(300,100)
    glVertex2f(300,300)
    glEnd()

    glLineWidth(2)
    glBegin(GL_LINES)
    #door
    glVertex2f(150,100)
    glVertex2f(150,200)

    glVertex2f(150, 200)
    glVertex2f(170,200)

    glVertex2f(170, 200)
    glVertex2f(170,100)

    #window
    glVertex2f(250,250)
    glVertex2f(250,270)

    glVertex2f(250, 270)
    glVertex2f(270, 270)

    glVertex2f(270, 270)
    glVertex2f(270, 250)

    glVertex2f(270, 250)
    glVertex2f(250, 250)

    #mid of window
    glVertex2f(250, 260)
    glVertex2f(270, 260)

    glVertex2f(260, 250)
    glVertex2f(260, 270)
    glEnd()

    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(165,150)
    glEnd()

def specialKeyListener(key,x,y):
    global rain_move_x
    if key==GLUT_KEY_RIGHT:
        rain_move_x+=0.1
    if key==GLUT_KEY_LEFT:
        rain_move_x-=0.1
    glutPostRedisplay()

def keyboardListener(key,x,y):

    global back_clr ,house_clr
    if key==b'd':
        back_clr=(1,1,1,1)
        house_clr=(0,0,0)
    if key==b'n':
        back_clr=(0,0,0,0)
        house_clr=(1,1,1)
    glutPostRedisplay()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def animate():#randrop left right angled
    global rain_move_x
    for i in range(len(arr_rain)):
        new_x,new_y=arr_rain[i]
        new_x+=rain_move_x
        new_y-=1

        if new_y<0:
            new_x=random.uniform(10,400)
            new_y=random.uniform(400,600)
        arr_rain[i]=(new_x,new_y)

    glutPostRedisplay()

def showScreen():
    glClearColor(*back_clr)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #glClearColor(back_white,back_black, 1.0)
    glLoadIdentity()
    iterate()

    drawhouse()
    for p in arr_rain:
        draw_rain_points(p[0],p[1])
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutKeyboardFunc(keyboardListener)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutMainLoop()





