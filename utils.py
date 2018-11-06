import pyglet
import math

def drawLine(x1, y1, x2, y2, colour, thickness):
    pyglet.gl.glLineWidth(thickness)
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', (x1, y1, x2, y2)), ('c3B', colour * 2))

def drawRectangle(x, y, w, h, colour, thickness):
    pyglet.gl.glLineWidth(thickness)
    p1 = (x, y)
    p2 = (x + w, y)
    p3 = (x + w, y + h)
    p4 = (x, y + h)
    p = p1+2*p2+2*p3+2*p4+p1
    pyglet.graphics.draw(8, pyglet.gl.GL_LINES, ('v2f', p), ('c3B', colour * 8))

def fillRectangle(x, y, w, h, colour):
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', (x, y, x+w, y, x+w, y+h, x, y+h)), ('c3B', colour * 4))

def fillEllipse(x, y, rx, ry, colour):
    verts = []
    numPoints = 10
    for i in range(numPoints):
        angle = math.radians(float(i)/numPoints * 360.0)
        tx = rx*math.cos(angle) + x
        ty = ry*math.sin(angle) + y
        verts += [tx,ty]
    pyglet.graphics.draw(numPoints, pyglet.gl.GL_POLYGON, ('v2f', verts), ('c3B', colour * numPoints))