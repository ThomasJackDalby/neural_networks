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

COEFFICIENT_OF_FRICTION = 0.4

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
        self.pockets = []
        self.pockets.append(Vector2D(0, 0))
        self.pockets.append(Vector2D(0, TABLE_HEIGHT/2))
        self.pockets.append(Vector2D(0, TABLE_HEIGHT))
        self.pockets.append(Vector2D(TABLE_WIDTH, 0))
        self.pockets.append(Vector2D(TABLE_WIDTH, TABLE_HEIGHT/2))
        self.pockets.append(Vector2D(TABLE_WIDTH, TABLE_HEIGHT))

        self.balls.append(self.white_ball)
        self.balls.append(self.black_ball)


        for j in range(5):
            for i in range(5-j): 
                x = (TABLE_WIDTH/2) - 2 * BALL_DIAMETER + i * BALL_DIAMETER + j * BALL_DIAMETER/2
                y = TABLE_HEIGHT - GARDEN_LINE + 2 * BALL_DIAMETER - j * BALL_DIAMETER * BALL_OFFSET
                self.balls.append(Ball(x, y, BallType.RED))

        # for i in range(7):
        #     self.balls.append(Ball(random.random()*TABLE_WIDTH, random.random()*TABLE_HEIGHT, BallType.RED))
        # for i in range(7):
        #     self.balls.append(Ball(random.random()*TABLE_WIDTH, random.random()*TABLE_HEIGHT, BallType.YELLOW))

    def hasFinished(self):
        for i in range(len(self.balls)):
            ball = self.balls[i]
            if ball.isPocketed:
                continue
            if (ball.vel.mag() > 0):
                return False
        return True

    def takeShot(self, power, angle):
        self.white_ball.vel = Vector2D(power * math.cos(angle), power * math.sin(angle))

    def update(self, dt):
        for ball in self.balls:
            if ball.isPocketed:
                continue
            ball.update(dt)
        
        # Check any collisions
        for i in range(len(self.balls)):
            a = self.balls[i]
            if a.isPocketed:
                continue
            for j in range(i+1, len(self.balls)):
                b = self.balls[j]
                if b.isPocketed:
                    continue
                if a.intersects(b):
                    a.collide(b, dt)

        # check any in the pockets
        for i in range(len(self.balls)-1, 0, -1):
            ball = self.balls[i]
            if ball.isPocketed:
                continue
            for j in range(len(self.pockets)):
                pocket = self.pockets[j]
                if (ball.pos - pocket).mag() < (POCKET_DIAMETER + BALL_DIAMETER) * 0.7/2:
                    print(ball.ballType.name,"Ball pocketed!")
                    ball.isPocketed = True
                    ball.pos = Vector2D(-1, -1)
                    ball.vel = Vector2D(0, 0)

class Ball:
    def __init__(self, x, y, ballType):
        self.pos = Vector2D(x, y)
        self.vel = Vector2D(0, 0)
        self.ballType = ballType
        self.isPocketed = False

    def intersects(self, other):
        return self.pos.quadrance(other.pos) < BALL_DIAMETER*BALL_DIAMETER

    def collide(self, other, dt):
        if self == other:
            return

        collision = other.pos - self.pos
        distance = collision.mag()

        collision = collision / distance
        aci = self.vel.dot(collision)
        bci = other.vel.dot(collision)
        self.vel += collision * (bci - aci)
        other.vel += collision * (aci - bci)

    def update(self, dt):
        if self.vel.mag() < 0.01:
            self.vel = Vector2D(0, 0)
            return

        self.vel += self.vel.normalise() * -COEFFICIENT_OF_FRICTION * dt
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

                