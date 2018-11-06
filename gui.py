import pyglet
import pool
import utils
from spatial import Vector2D
from pyglet.window import mouse

# something

VIEW_SCALE = 200
STROKE_THICKNESS = 2
BLACK_COLOUR = [0, 0, 0]
WHITE_COLOUR = [255, 255, 255]
RED_COLOUR = [255, 0, 0]
YELLOW_COLOUR = [255, 0, 255]
FELT_COLOUR = [27, 137, 38]
FRAME_COLOUR = [96, 62, 19]


window = pyglet.window.Window(800, 600, resizable=True)

fps_display = pyglet.clock.ClockDisplay()

poolTable = pool.PoolTable()
poolTable.white_ball.vel = Vector2D(0.5, 0.5)

def getXOffset():
    return window.width / 2 - pool.TABLE_WIDTH * VIEW_SCALE / 2

def getYOffset():
    return window.height / 2 - pool.TABLE_HEIGHT * VIEW_SCALE / 2

def drawFrame():
    x = -pool.CUSHION_WIDTH-pool.FRAME_WIDTH
    y = -pool.CUSHION_WIDTH-pool.FRAME_WIDTH
    w = pool.TABLE_WIDTH+2*pool.CUSHION_WIDTH+2*pool.FRAME_WIDTH
    h = pool.TABLE_HEIGHT+2*pool.CUSHION_WIDTH+2*pool.FRAME_WIDTH
    utils.fillRectangle(x * VIEW_SCALE + getXOffset(), y * VIEW_SCALE + getYOffset(), w * VIEW_SCALE, h * VIEW_SCALE, FRAME_COLOUR)
    utils.drawRectangle(x * VIEW_SCALE + getXOffset(), y * VIEW_SCALE + getYOffset(), w * VIEW_SCALE, h * VIEW_SCALE, BLACK_COLOUR, STROKE_THICKNESS)

def drawCushion():
    x = -pool.CUSHION_WIDTH
    y = -pool.CUSHION_WIDTH
    w = pool.TABLE_WIDTH+2*pool.CUSHION_WIDTH
    h = pool.TABLE_HEIGHT+2*pool.CUSHION_WIDTH
    utils.fillRectangle(x * VIEW_SCALE + getXOffset(), y * VIEW_SCALE + getYOffset(), w * VIEW_SCALE, h * VIEW_SCALE, FELT_COLOUR)
    utils.drawRectangle(x * VIEW_SCALE + getXOffset(), y * VIEW_SCALE + getYOffset(), w * VIEW_SCALE, h * VIEW_SCALE, BLACK_COLOUR, STROKE_THICKNESS)

def drawBed():
    utils.fillRectangle(getXOffset(), getYOffset(), pool.TABLE_WIDTH * VIEW_SCALE, pool.TABLE_HEIGHT * VIEW_SCALE, FELT_COLOUR)
    utils.drawRectangle(getXOffset(), getYOffset(), pool.TABLE_WIDTH * VIEW_SCALE, pool.TABLE_HEIGHT * VIEW_SCALE, BLACK_COLOUR, STROKE_THICKNESS)

def drawLine():
    utils.drawLine(getXOffset(), pool.GARDEN_LINE * VIEW_SCALE + getYOffset(), pool.TABLE_WIDTH * VIEW_SCALE + getXOffset(), pool.GARDEN_LINE * VIEW_SCALE + getYOffset(), WHITE_COLOUR, STROKE_THICKNESS)

def drawTable():
    drawFrame()
    drawCushion()
    drawBed()
    drawLine()
    drawPockets()
    for ball in poolTable.balls:
        drawBall(ball)

def drawPocket(x, y):
    tx = x * VIEW_SCALE + getXOffset()
    ty = y * VIEW_SCALE + getYOffset()
    utils.fillEllipse(tx, ty, pool.POCKET_DIAMETER * VIEW_SCALE * 0.5, pool.POCKET_DIAMETER * VIEW_SCALE * 0.5, BLACK_COLOUR)

def drawPockets():
    drawPocket(0, 0)
    drawPocket(pool.TABLE_WIDTH, 0)
    drawPocket(0, pool.TABLE_HEIGHT/2)
    drawPocket(pool.TABLE_WIDTH, pool.TABLE_HEIGHT/2)
    drawPocket(pool.TABLE_WIDTH, pool.TABLE_HEIGHT)
    drawPocket(0, pool.TABLE_HEIGHT)
    
def getBallColour(ball):
    if pool.BallType.BLACK is ball.ballType:
        return BLACK_COLOUR
    if pool.BallType.WHITE is ball.ballType:
        return WHITE_COLOUR
    if pool.BallType.RED is ball.ballType:
        return RED_COLOUR
    if pool.BallType.YELLOW is ball.ballType:
        return YELLOW_COLOUR

def drawBall(ball):
    tx = ball.pos.x * VIEW_SCALE + getXOffset()
    ty = ball.pos.y * VIEW_SCALE + getYOffset()
    colour = getBallColour(ball)
    utils.fillEllipse(tx, ty, pool.BALL_DIAMETER * VIEW_SCALE * 0.5, pool.BALL_DIAMETER * VIEW_SCALE * 0.5, colour)

@window.event
def on_draw():
    window.clear()
    drawTable()
    fps_display.draw()

def update(dt):
    poolTable.update(dt)

pyglet.clock.schedule_interval(update, 0.01)
pyglet.app.run()