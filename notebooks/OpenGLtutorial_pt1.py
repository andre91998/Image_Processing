# -*- coding: utf-8 -*-
"""
Created on Sun May  3 01:21:17 2020

@author: Andre
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)

glutInit() # Initialize a glut instance which will allow us to customize our window
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the width and height of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow("OpenGL Coding Practice") # Give your window a title
glutDisplayFunc(showScreen)  # Tell OpenGL to call the showScreen method continuously
glutIdleFunc(showScreen)     # Draw any graphics or shapes in the showScreen function at all times
glutMainLoop()  # Keeps the window created above displaying/running in a loop
