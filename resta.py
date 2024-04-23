import glfw
from OpenGL.GL import *
import time

def main():
    
    if not glfw.init():
        return

    window = glfw.create_window(480, 480, "Triángulo", None, None)
    
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    
    sumando = 0.0
    
    while not glfw.window_should_close(window):       
        glfw.poll_events()
        
        primerVertice = [0.0 - sumando, 0.5 - sumando]
        segundoVertice = [-0.5 - sumando, -0.5 - sumando]
        tercerVertice = [0.5 - sumando, -0.5 - sumando]
        
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        
        glBegin(GL_TRIANGLES) 
        #* desempaqueta los valores
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(*primerVertice)  
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(*segundoVertice) 
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(*tercerVertice)
        glEnd()
        
        time.sleep(0.5)
        
        sumando += 0.01
        
        
        glfw.swap_buffers(window)
    
    glfw.terminate()

main()
