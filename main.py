
import pygame
from pygame import constants
from pygame import font
import game_constants
from states.menu_state import Menu
#import sprites
import os
import time

class Game():
    def __init__(self):  
        
        pygame.init()
        self.screen = pygame.display.set_mode((game_constants.WIDTH, game_constants.HEIGTH))
        pygame.display.set_caption(game_constants.TITLE)
        self.runing, self.playing = True, True
        self.rect = self.screen.get_rect()
        self.actions = {"left": False, "right": False, "up" : False, "down" : False, "action1" : False,"action2" : False}
        self.dt,self.prev_time = 0, 0
        self.font = pygame.font.match_font(game_constants.FONT)
        self.state_stack = []
        self.load_assets()
        self.load_states()
      
    
    def get_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    self.runing = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.actions['action1'] = True
                    if event.key == pygame.K_LEFT:
                        self.actions['left'] = True
                    if event.key == pygame.K_RIGHT:
                        self.actions['right'] = True
                    if event.key == pygame.K_UP:
                        self.actions['up'] = True
                    if event.key == pygame.K_DOWN:
                        self.actions['down'] = True
                    if event.key == pygame.K_e:
                        self.actions['action2'] = True
    
    def update(self):
        self.state_stack[-1].update(self.dt,self.actions)

    def render(self):
        self.state_stack[-1].render(self.screen)
        pygame.display.flip()

    def get_dt(self):

        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def load_assets(self):

        self.dir_imagens = os.path.join(os.getcwd(),'imagens')
        self.dir_audios = os.path.join(os.getcwd(),'sons')
    
        '''self.spritesheet = os.path.join(diretorio_imagens,game_constants.SPRITESHEET)
        self.man_start_logo = os.path.join(diretorio_imagens, game_constants.LOGO)
        self.man_start = pygame.image.load(self.man_start_logo).convert()'''

    def load_states(self):
        self.menu_screen = Menu(self)
        self.state_stack.append(self.menu_screen)


    def game_loop(self):
        self.clock = pygame.time.Clock()
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()

    def draw_text(self, texto,tamanho,cor,x,y):

        fonte = pygame.font.Font(self.font,tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop=(x,y)
        self.screen.blit(texto,texto_rect)

    def display_text_animation(self,string,color):
        text = ''
        for i in range(len(string)):
            self.screen.fill(game_constants.WHITE)
            text += string[i]
            fonte = pygame.font.Font(self.font,30)
            text_surface = fonte.render(text, True, color)
            text_rect = text_surface.get_rect()
            text_rect.center = (game_constants.WIDTH/2, game_constants.HEIGTH/2)
            self.screen.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.time.wait(150)



if __name__ == '__main__':
    game = Game()
    while game.runing:
        
        if game.playing:
            game.game_loop()
        else:
            while len(game.state_stack) > 1:
                game.state_stack.pop()
            game.playing = True
        
    

