from turtle import *
from math import *
'''
    file structure:
        num
        px
        py
        vx
        vy
        arg
        r
        c
        s
        k
'''
Vec0 = Vec2D(0, 0)
class Bird:
    def __init__(self, position, velocity, color, painter = None):
        self.position = position
        self.velocity = velocity
        self.painter = painter or Turtle()
        self.painter.pencolor(color)
        self.painter.speed(0)
        self.painter.penup()
        self.goto()
        self.painter.shape('classic')
        self.painter.pendown()
    def goto(self):
        self.facing()
        self.painter.goto(self.position)
    def facing(self):
        self.painter.seth(degrees(atan2(*(self.velocity)) + 90))
    def copy(self):
        return __class__(self.position.copy(),
                         self.velocity.copy(),
                         self.turtle)
class BOID_system:
    def __init__(self, similate_acc, display_acc,
                 arguments, num = 0, birds = None):
        self.num = num
        self.birds = birds or []
        self.simulate_acc = similate_acc
        self.display_acc = display_acc
        self.arguments = arguments
        self.cnt = 0
    def add_bird(self, bird):
        self.num += 1
        self.birds.append(bird)
    def remove_bird(self, bird_no):
        self.num -= 1
        return self.birds.pop(bird_no)
    def simulate(self):
        new = self.birds.copy()
        for i in range(self.num):
            zor = []
            zoo = []
            zoa = []
            for j in range(self.num):
                if i == j:
                    continue
                distance = abs(self.birds[j].position -
                               self.birds[i].position)
                if distance < self.arguments[0]:
                    zor.append((self.birds[j].position -
                                self.birds[i].position, distance))
                elif distance < self.arguments[1]:
                    zoo.append((self.birds[j].velocity -
                                self.birds[i].velocity,
                                abs(self.birds[j].velocity -
                                    self.birds[i].velocity)))
                elif distance < self.arguments[2]:
                    zoa.append((self.birds[j].position -
                                self.birds[i].position, distance))
            if zor:
                new[i].velocity += self.simulate_acc * \
                                   self.arguments[3] * \
                                   sum((-1 / j[1] * j[0] for j in zor),
                                       start = Vec0)
            elif zoo and zoa:
                new[i].velocity += self.simulate_acc / 2 * \
                                   (sum((1 / j[1] * j[0]
                                         for j in zoo if j[1]),
                                        start = Vec0) *
                                    self.arguments[4] +
                                    sum((1 / j[1] * j[0]
                                         for j in zoa),
                                        start = Vec0) *
                                    self.arguments[5])
            elif zoo:
                new[i].velocity += self.simulate_acc * \
                                   self.arguments[4] * \
                                   sum((1 / j[1] * j[0] for j in zoo),
                                       start = Vec0)
            elif zoa:
                new[i].velocity += self.simulate_acc * \
                                   self.arguments[5] * \
                                   sum((1 / j[1] * j[0] for j in zoa),
                                       start = Vec0)
            new[i].position += new[i].velocity * self.simulate_acc
            if self.cnt % self.display_acc == 0:
                new[i].goto()
        self.birds = new
        self.cnt += 1
with open('BOID.cfg') as file:
    f = file.readlines()
    for i in range(1, 6):
        f[i] = list(map(float, f[i].split()))
    num = int(f[0])
    position = [Vec2D(f[1][i], f[2][i]) for i in range(num)]
    velocity = [Vec2D(f[3][i], f[4][i]) for i in range(num)]
    arguments = f[5]
    color = f[6].split()
    simulate_acc = float(f[7])
    display_acc = int(f[8])
    background = f[9]
boid_system = BOID_system(simulate_acc, display_acc, arguments)
bgcolor(background)
title('BOID Model')
delay(0)
for i in range(num):
    boid_system.add_bird(Bird(position[i], velocity[i], color[i]))
while True:
    boid_system.simulate()
