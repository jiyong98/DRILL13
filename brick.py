import random

from pico2d import *

import game_framework
import game_world


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
class Brick:
    x = 0
    def __init__(self, center=300, y=100):
        self.image = load_image('brick180x40.png')
        self.left_wall, self.right_wall = center - 100, center + 100
        self.x, self.y = center, y
        self.speed = random.randint(100,250) * random.choice([-1,1])

        Brick.x = self.right_wall
    def update(self):
        self.x += game_framework.frame_time * self.speed
        if self.x >= self.right_wall:
            self.speed = random.randint(100,250) * random.choice([-1,1])
            self.x = self.right_wall
        if self.x <= self.left_wall:
            self.speed = random.randint(100,250) * random.choice([-1,1])
            self.x = self.left_wall
        Brick.x = self.right_wall



    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x-90, self.y-20, self.x+90, self.y+20
