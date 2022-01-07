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
        self.waiting=True

    def update(self, delta_time, actions):

        pass
    
    
    def render(self, surface):

        pygame.mixer.music.load(os.path.join(self.game.dir_audios,game_constants.MUSIC))
        pygame.mixer.music.play()

       
        self.game.draw_text('CORONIAL WAR',60,game_constants.WHITE,game_constants.WIDTH/2,200)
        self.game.draw_text('-pressione espaço e as setas pra jogar',15,game_constants.WHITE,game_constants.WIDTH/2,320)
        self.game.draw_text('desenvolvido por Osvaldo, Igor e henrique',22,game_constants.WHITE,game_constants.WIDTH/2,520)
        pygame.display.flip()
        

        
        while self.waiting:
            self.game.clock.tick(game_constants.FPS)
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    self.waiting=False
                    self.game.playing = False
                    self.game.runing = False
                
                if event.type == pygame.KEYUP and pygame.mixer.music.get_busy() != True:
                    
                    self.waiting =False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.game.dir_audios,game_constants.k_START)).play()
         
            
            new_state = Play_stage_one(self.game)
            new_state.enter_state()



