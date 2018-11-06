from enum import Enum
from spatial import *
import random

TABLE_WIDTH = 1.2192
TABLE_HEIGHT = 2.1336
CUSHION_WIDTH = 0.07
FRAME_WIDTH = 0.03
GARDEN_LINE = 0.4318
BALL_DIAMETER = 0.0508
POCKET_DIAMETER = 0.086
BALL_OFFSET = 0.866025

class BallType(Enum):
    WHITE = 1
    BLACK = 2
    RED = 3
    YELLOW = 4

class PoolTable:

    def __init__(self):
        self.balls = []
        self.white_ball = Ball(TABLE_WIDTH/2, GARDEN_LINE, BallType.WHITE)
        self.black_ball = Ball(TABLE_WIDTH/2, TABLE_HEIGHT - GARDEN_LINE, BallType.BLACK)

        self.balls.append(self.white_ball)
        self.balls.append(self.black_ball)
        for i in range(7):
            self.balls.append(Ball(random.random()*TABLE_WIDTH, random.random()*TABLE_HEIGHT, BallType.RED))
        for i in range(7):
            self.balls.append(Ball(random.random()*TABLE_WIDTH, random.random()*TABLE_HEIGHT, BallType.YELLOW))

    def update(self, dt):
        for ball in self.balls:
            ball.update(dt)
        
        for i in range(len(self.balls)):
            for j in range(i+1, len(self.balls)):
                a = self.balls[i]
                b = self.balls[j]
                if a.intersects(b):
                    a.collide(b)

class Ball:

    def __init__(self, x, y, ballType):
        self.pos = Vector2D(x, y)
        self.vel = Vector2D(0, 0)
        self.acc = Vector2D(0, 0)
        self.ballType = ballType

    def intersects(self, other):
        return self.pos.quadrance(other.pos) < BALL_DIAMETER*BALL_DIAMETER

    def collide(self, b):
        Ca = self.vel + b.vel
        Cb = self.vel.square() + b.vel.square()
        Cc = (Ca.square() - Cb) / 2
        v1 = (Vector2D(1, 1) - (Vector2D(1, 1) - Cc*4).root()) / 2
        v2 = Ca - v1
        self.vel = v1
        b.vel = v2

    def update(self, dt):
        self.pos +=  self.vel * dt

        # if hit one of the sides, reverse direction
        if self.pos.x + BALL_DIAMETER / 2 >= TABLE_WIDTH:
            self.vel.x = -self.vel.x
        elif self.pos.x - BALL_DIAMETER / 2 <= 0:
            self.vel.x = -self.vel.x
        if self.pos.y + BALL_DIAMETER / 2 >= TABLE_HEIGHT:
            self.vel.y = -self.vel.y
        elif self.pos.y - BALL_DIAMETER / 2 <= 0:
            self.vel.y = -self.vel.y

                