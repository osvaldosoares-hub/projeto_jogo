
from types import new_class
from pygame import color, rect
import states.play_state_two
from states.state import State
import pygame, os
import game_constants
from pygame.sprite import Group, Sprite
from random import randint


class Nav_player():
    def __init__(self,game):

        nav_number = randint(1,4)

        self.nav_image = pygame.image.load(os.path.join(game.dir_imagens,game_constants.NAV_IMAGE + str(nav_number) + '.png'))
        self.nav_image = pygame.transform.scale(self.nav_image, (40*2, 40*2))
        self.nav_rect = self.nav_image.get_rect()
        self.screen_rect = game.screen.get_rect()
        self.nav_rect.centerx = self.screen_rect.centerx
        self.nav_rect.bottom = self.screen_rect.bottom
        self.vel = 100



    def render(self,surface):
        surface.blit(self.nav_image,self.nav_rect)


    def update(self,delta_time, actions):



        if actions['right']:
            if self.nav_rect.x < game_constants.WIDTH - 100:
                self.nav_rect.x += 100*self.vel*delta_time
                actions['right'] = False
        
        if actions['left']:
            if self.nav_rect.x > 1:
                self.nav_rect.x -= 100*self.vel*delta_time
                actions['left'] = False
        
    
    def create_bullet(self):
        return Bullet(self.nav_rect.centerx, self.nav_rect.centery,game_constants.WHITE)
            




class Bullet(Sprite): 

    def __init__(self,position_x,position_y,color):
        super().__init__()

        self.image = pygame.Surface((4,10))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (position_x,position_y))
        self.vel = 100
    
        
        
    def update(self, delta_time, actions):

        self.rect.y -= delta_time*self.vel



class Corona_base(Sprite):

    def __init__(self,game):
        super().__init__()

        self.image = pygame.image.load(os.path.join(game.dir_imagens,game_constants.CORONA))
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()
        self.rect.centerx = randint(0,(game_constants.WIDTH - 100))
        self.rect.top = -1*randint(0,(game_constants.HEIGTH)) 
        self.vel = 3

    def update(self,delta_time, actions):
        
        self.rect.y += 90*delta_time*self.vel

        if self.rect.bottom >= self.screen_rect.bottom:
            self.rect.top = -1*randint(0,(game_constants.HEIGTH/2)) 
            self.rect.centerx = randint(0,(game_constants.WIDTH - 100))



class Omicron(Corona_base):
    def __init__(self, game):
        super().__init__(game)

    def update(self,delta_time, actions):
        
        self.rect.y += 85*delta_time*self.vel

        if self.rect.bottom >= self.screen_rect.bottom:
            self.rect.top = -1*randint(0,(game_constants.HEIGTH/2)) 
            self.rect.centerx = randint(0,(game_constants.WIDTH - 100))
           
         
class Omicron_bulet(Bullet):
    def __init__(self, position_x, position_y, color):
        super().__init__(position_x, position_y, color)

    
    def update(self, delta_time, actions):

        self.rect.y += delta_time*self.vel*5


class Enemies():
    
    def __init__(self):
        pass

    def create_virus(self,game,corona_base_group,number):
           
        corona =  Corona_base(game)
        corona_base_group.add(corona)

        for i in range(0,number):
            new_corona = Corona_base(game)
            corona_base_group.add(new_corona)
