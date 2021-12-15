from states.state import State
from states.play_state import Play
import game_constants
import pygame
import os


class Menu(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self, delta_time, actions):

        pass
    
    
    def render(self, surface):

        pygame.mixer.music.load(os.path.join(self.game.dir_audios,game_constants.MUSIC))
        pygame.mixer.music.play()

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
                
                if event.type == pygame.KEYUP:
                    
                    esperando =False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.game.dir_audios,game_constants.k_START)).play()
            
            pygame.time.delay(100)
            
            new_state = Play(self.game)
            new_state.enter_state()