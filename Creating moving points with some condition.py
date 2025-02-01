from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

#Here after clicking right button points will create randomly and start to move,
# also the functions of the points will be control by some keys like ,blinking, freeze,speed increase and decrease etc.
point_info=[]
flag=False
freeze=False
back=True
blink_time=time.time()
speed=1
boun_x=500
boun_y=500


def draw_points(x, y,clr):
   glPointSize(4) #pixel size. by default 1 thake
   glBegin(GL_POINTS)
   glColor3f(clr[0], clr[1], clr[2])
   glVertex2f(x,y)
   glEnd()


def random_clr():


   return [random.random(),random.random(),random.random()]
def random_spd():
   return random.uniform(0.3,0.3)*speed
def random_movement():
   x_move= random.choice([-1,1])
   y_move=random.choice([-1,1])
   return x_move,y_move
def random_point(x,y):
   global point_info
   for i in range(5):
       clr=random_clr()
       runs=random_spd()
       x_dir,y_dir=random_movement()
       point_info.append({'x':x,'y':y,'clr':clr,'black':[0,0,0],'speed':runs,'dx':x_dir,'dy':y_dir,'blink':False})




def mouseListener(button,state,x,y):
   global back,blink_time,freeze,point_info
   # if freeze:
   #     return
   if button==GLUT_LEFT_BUTTON and state ==GLUT_DOWN:
       random_point(x,boun_y-y)
       # blink=not blink
       # blink_time=time.time()
   elif button==GLUT_RIGHT_BUTTON and state==GLUT_DOWN:


       for p in point_info:
           p['blink'] = not p['blink']


def specialKeyListener(key,x,y):
   global point_info,speed,freeze
   if key==GLUT_KEY_UP:
       speed+=0.2
       update_speed()
   elif key==GLUT_KEY_DOWN :
       speed-=0.2
       update_speed()
   #for p in point_info:
    #   point_info['speed']=speed
def update_speed():
   global point_info
   for p in point_info:
       p['speed']=random.uniform(0.3,0.3)*speed
def keyboardListener(key,x,y):
   global freeze
   if key ==b' ':
       freeze=not freeze
#----------------------


def animate():
   global point_info,boun_x,boun_y,freeze,flag
   if not freeze and not flag:
       for p in point_info:
           p['x']+=p['dx']*p['speed']
           p['y']+=p['dy']*p['speed']
           if p['x']>=boun_x or p['x']<=0:
               p['dx']*=-1
           if p['y']>=boun_y or p['y']<=0:
               p['dy']*=-1
   glutPostRedisplay()
def showScreen():
   global point_info,back,blink_time
   glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   #glClearColor(back_white,back_black, 1.0)
   #glLoadIdentity()
   iterate()
   cur_time=time.time()
   if cur_time-blink_time>=0.5:
       back=not back
       blink_time=cur_time


   for p in point_info:
       if p['blink'] and back:
           draw_points(p['x'],p['y'],p['black'])
       else:
           draw_points(p['x'],p['y'],p['clr'])
   glutSwapBuffers()
def iterate():
  # global blink_time,blink
   glViewport(0, 0, 500, 500)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
   glMatrixMode (GL_MODELVIEW)
   glLoadIdentity()


glutInit()
glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutKeyboardFunc(keyboardListener)
glutMainLoop()







