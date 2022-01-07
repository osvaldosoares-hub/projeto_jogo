from pygame import color, rect
from states.play_state_two import Play_stage_two
from states.state import State
import pygame, os
import game_constants
from pygame.sprite import Group, Sprite
from random import randint
from states.game_elements.elements import Enemies, Nav_player,Corona_base 

class Play_stage_one(State):
    def __init__(self, game):
        super().__init__(game)

        self.player = Nav_player(game)
        self.bullet_group = Group()
        self.corona_base_group = Group()
        self.enemys = Enemies()
        self.level_finish = 0
        self.create = True
        
            

    def update(self, delta_time, actions):

        self.player.update(delta_time, actions)
        
        if actions['action1']:
            self.bullet_group.add(self.player.create_bullet())
            if self.create:
               
                self.enemys.create_virus(self.game,self.corona_base_group,15)
                self.create = False

            actions['action1'] = False

        if actions['action2']:
            actions['action2'] = False
            self.game.screen.fill(game_constants.BLACK)
            self.game.draw_text('Fase II',60,game_constants.WHITE,game_constants.WIDTH/2,200)
            self.game.draw_text('VARIANTE OMICRON',20,game_constants.WHITE,game_constants.WIDTH/2,320)
            pygame.display.flip()
            pygame.time.wait(3000)

            new_state = Play_stage_two(self.game)
            new_state.enter_state()


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

                        self.game.screen.fill(game_constants.BLACK)
                        self.game.draw_text('Fase II',60,game_constants.WHITE,game_constants.WIDTH/2,200)
                        self.game.draw_text('VARIANTE ÔMICRON',20,game_constants.WHITE,game_constants.WIDTH/2,320)
                        pygame.display.flip()
                        pygame.time.wait(3000)

                        new_state = Play_stage_two(self.game)
                        new_state.enter_state()
    
                    break

        for virus in self.corona_base_group.sprites():
            if self.player.nav_rect.colliderect(virus.rect):
                self.game.playing = False

        self.corona_base_group.update(delta_time, actions)

        if self.game.playing == False:
            self.game.screen.fill(game_constants.BLACK)
            self.game.draw_text('GAME OVER',60,game_constants.WHITE,game_constants.WIDTH/2,200)
            pygame.display.flip()
            pygame.time.wait(2000)

        


    def render(self, surface):

        surface.fill(game_constants.BLACK)
        self.player.render(surface)
        self.bullet_group.draw(surface)
        self.corona_base_group.draw(surface)

       






