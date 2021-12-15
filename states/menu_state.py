from pygame.mixer import get_busy
from states.state import State
from states.play_state_one import Play_stage_one
import game_constants
import pygame
from time import *
import os


class Menu(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self, delta_time, actions):

        pass
    
    
    def render(self, surface):

        self.game.display_text_animation(game_constants.INTRO_PART_01, game_constants.BLACK)
        pygame.time.wait(1000)
        self.game.display_text_animation(game_constants.INTRO_PART_02, game_constants.BLACK)
        pygame.time.wait(100)
        self.game.display_text_animation(game_constants.INTRO_PART_03, game_constants.BLACK)
        pygame.time.wait(100)
        self.game.display_text_animation(game_constants.INTRO_PART_04, game_constants.BLACK)
        pygame.time.wait(100)
        self.game.display_text_animation(game_constants.INTRO_PART_05, game_constants.RED)
        pygame.time.wait(1000)
        self.game.display_text_animation(game_constants.INTRO_PART_06, game_constants.BLACK)
        pygame.time.wait(100)

        pygame.mixer.music.load(os.path.join(self.game.dir_audios,game_constants.MUSIC))
        pygame.mixer.music.play()

        self.game.screen.fill(game_constants.BLACK)
        self.game.draw_text('CORONIAL WAR',60,game_constants.WHITE,game_constants.WIDTH/2,200)
        self.game.draw_text('-pressione uma tecla pra jogar',15,game_constants.WHITE,game_constants.WIDTH/2,320)
        self.game.draw_text('desenvolvido por Osvaldo, Igor e henrique',22,game_constants.WHITE,game_constants.WIDTH/2,520)
        pygame.display.flip()
        

        esperando=True
        while esperando:
            self.game.clock.tick(game_constants.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando=False
                    self.game.playing = False
                    self.game.runing = False
                
                if event.type == pygame.KEYUP and pygame.mixer.music.get_busy() != True:
                    
                    esperando =False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.game.dir_audios,game_constants.k_START)).play()
         
            
            new_state = Play_stage_one(self.game)
            new_state.enter_state()



