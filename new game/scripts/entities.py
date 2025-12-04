import pygame
import sys

class PhysicsEntity:
    def __init__(self, pos, e_type, size, game):
        self.game = game
        self.pos = list(pos)
        self.e_type = e_type
        self.size = size
        self.velocuty = [0, 0]

    def update(self, movement =(0,0)):
        
        frame_movement = (self.velocity[0] + self.movement[0], self.velocity[1] + self.movement[1])
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)