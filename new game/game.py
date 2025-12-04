import pygame
import sys
from scripts.entities import PhysicsEntity

class game:

    def __init__(self):
        
        pygame.init()

        pygame.display.set_caption('Ninja game')
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

        self.image = pygame.image.load('data/images/clouds/cloud_1.png')
        self.image.set_colorkey((0,0,0))
        self.img_pos = [120,200]

        self.movement = [False, False]

        self.collision_area = pygame.Rect(30, 50, 300, 50)

        self.player = PhysicsEntity((50,50), 'player', (8,15))


    def run(self):

        while True:

            self.screen.fill((14, 219, 248))

            self.img_r  = pygame.Rect(self.img_pos[0], self.img_pos[1], self.image.get_width(), self.image.get_height())
            if self.img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0,100,225), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0,50,225), self.collision_area)
            
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5

            self.screen.blit(self.image, self.img_pos)

            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                elif event.type == pygame.KEYUP:       
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
            
            pygame.display.update()
            self.clock.tick(60)

game().run()

