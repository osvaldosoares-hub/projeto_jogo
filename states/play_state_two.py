from pygame import rect
from states.state import State
import pygame, os
import game_constants
from pygame.sprite import Group, Sprite
from random import randint
from states.game_elements.elements import Enemies, Omicron,Corona_base, Nav_player, Omicron_bulet


class Play_stage_two(State):
    def __init__(self, game):
        super().__init__(game)

        self.player = Nav_player(game)
        self.bullet_group = Group()
        self.corona_base_group = Group()
        self.omicron_group = Group()
        self.omicron_bullet_group = Group()
        self.enemys = Enemies()
        self.create = True
        self.level_finish = 0
        
            

    def update(self, delta_time, actions):


        self.player.update(delta_time, actions)
        
        if actions['action1']:
            self.bullet_group.add(self.player.create_bullet())
            self.omicron_bullet_group.add(Omicron_bulet(randint(0,(game_constants.WIDTH - 100)),-1*randint(0,(game_constants.HEIGTH/2)) ,game_constants.GREEN))

            if self.create:

                self.enemys.create_virus(self.game,self.corona_base_group,15)
             
                self.create = False

            actions['action1'] = False
        
        if actions['action2']:
            actions['action2'] = False
            self.game.end()

        

        for bullet in self.bullet_group.sprites():
            if bullet.rect.top <= 0:
                self.bullet_group.remove(bullet)
            else:	
                bullet.update(delta_time, actions)
            
        for bullet in self.bullet_group.sprites():
            for virus in self.corona_base_group.sprites():
                if bullet.rect.colliderect(virus.rect):
                    self.bullet_group.remove(bullet)
                    self.corona_base_group.remove(virus)
                    self.level_finish += 1

                    if self.level_finish == 5:
                        self.game.end()
                        

                    break

        for virus in self.corona_base_group.sprites():
            if self.player.nav_rect.colliderect(virus.rect):
                self.game.playing = False
                break

        for omi_bullet in self.omicron_bullet_group.sprites():

            if omi_bullet.rect.colliderect(self.player.nav_rect):
                 self.game.playing = False
                 break

        self.corona_base_group.update(delta_time, actions)
        self.omicron_bullet_group.update(delta_time, actions)

        if self.game.playing == False:
            self.game.screen.fill(game_constants.BLACK)
            self.game.draw_text('GAME OVER',60,game_constants.WHITE,game_constants.WIDTH/2,200)
            pygame.display.flip()
            pygame.time.wait(2000)

        


    def render(self, surface):

        surface.fill(game_constants.BLACK)
        self.player.render(surface)
        self.bullet_group.draw(surface)
        self.omicron_bullet_group.draw(surface)
        self.corona_base_group.draw(surface)
        
    
    