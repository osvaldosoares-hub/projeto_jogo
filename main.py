
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
        self.actions = {"left": False, "right": False, "action1" : False,"action2" : False}
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
        self.dir_fonts = os.path.join(os.getcwd(),'fonts')
    
     
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
        hard_click = pygame.mixer.Sound(os.path.join(self.dir_audios,game_constants.TYPEWRITER_01))
        soft_click = pygame.mixer.Sound(os.path.join(self.dir_audios,game_constants.TYPEWRITER_02))
        hit = pygame.mixer.Sound(os.path.join(self.dir_audios,game_constants.TYPEWRITER_03))
        text = ''
        hit.play()

        for i in range(len(string)):
            self.get_events()
          
            self.screen.fill(game_constants.WHITE)
            text += string[i]
            fonte = pygame.font.Font(os.path.join(self.dir_fonts,game_constants.TYPEWRITER_FONT),20)
            text_surface = fonte.render(text, True, color)
            text_rect = text_surface.get_rect()
            text_rect.center = (game_constants.WIDTH/2, game_constants.HEIGTH/2)
            self.screen.blit(text_surface, text_rect)
            
            if string[i] == ' ':
                hard_click.play()
                
            else:
                soft_click.play()
            
            pygame.display.update()
            pygame.time.wait(150)
            
            
        
     

    def presetention(self):
        self.display_text_animation(game_constants.INTRO_PART_01, game_constants.BLACK)
        pygame.time.wait(1000)
        self.display_text_animation(game_constants.INTRO_PART_02, game_constants.BLACK)
        pygame.time.wait(100)
        self.display_text_animation(game_constants.INTRO_PART_03, game_constants.BLACK)
        pygame.time.wait(100)
        self.display_text_animation(game_constants.INTRO_PART_04, game_constants.BLACK)
        pygame.time.wait(100)
        self.display_text_animation(game_constants.INTRO_PART_05, game_constants.RED)
        pygame.time.wait(1000)
        self.display_text_animation(game_constants.INTRO_PART_06, game_constants.BLACK)
        pygame.time.wait(100)

        coordenatex = 200
        coordenatey = 200
        vac = ['Coronavac','Pfizer','Jassen','Oxford']
        self.screen.fill(game_constants.WHITE)


        for i in range(1,5):
        
            if i > 2:
                coordenatey = 400
                
            if i % 2 == 0:
                coordenatex = 600
            else:
                coordenatex = 200

            nav_image = pygame.image.load(os.path.join(game.dir_imagens,game_constants.NAV_IMAGE + str(i) + '.png'))
            nav_image = pygame.transform.scale(nav_image, (40*2, 40*2))
            nav_rect = nav_image.get_rect()
            nav_rect.x = coordenatex
            nav_rect.y = coordenatey
            self.screen.blit(nav_image, nav_rect)

            self.draw_text(vac[i-1],15, game_constants.BLACK, coordenatex + 40,coordenatey + 80)
            
            
            
        pygame.display.update()
        pygame.time.wait(6000)

    
    def end(self):

        self.display_text_animation(game_constants.END_PART_01, game_constants.BLACK)
        pygame.time.wait(1000)
        self.display_text_animation(game_constants.END_PART_02, game_constants.BLACK)
        pygame.time.wait(100)
        self.display_text_animation(game_constants.END_PART_03, game_constants.GREEN)
        pygame.time.wait(300)
        self.display_text_animation(game_constants.END_PART_04, game_constants.BLACK)
        pygame.time.wait(100)
        self.display_text_animation(game_constants.END_PART_05, game_constants.BLACK)
        pygame.time.wait(1000)
        self.display_text_animation(game_constants.END_PART_06, game_constants.BLACK)
        pygame.time.wait(100)
        self.display_text_animation(game_constants.END_PART_07, game_constants.GREEN)
        pygame.time.wait(1000)
        self.display_text_animation(game_constants.END_PART_08, game_constants.YELLOW)
        pygame.time.wait(1000)

        boss_image = pygame.image.load(os.path.join(self.dir_imagens,game_constants.TRUE_BOSS))
        boss_rect = boss_image.get_rect()
        boss_rect.centerx = game_constants.HEIGTH/2
        boss_rect.centery = game_constants.WIDTH/2
        self.screen.fill(game_constants.BLACK)
        self.screen.blit(boss_image, boss_rect)
        pygame.display.flip()
        laugh = pygame.mixer.Sound(os.path.join(self.dir_audios,game_constants.LAUGH))
        laugh.play()
        pygame.time.wait(8000)
        laugh.stop()

        self.screen.fill(game_constants.BLACK)
        self.draw_text('OBRIGADO POR JOGAR =)',60,game_constants.WHITE,game_constants.WIDTH/2,200)
        pygame.display.flip()
        pygame.time.wait(2000)


        
        self.playing = False
        self.runing = False

            

            
            



if __name__ == '__main__':
    game = Game()
    game.presetention()
    game.screen.fill(game_constants.BLACK)
    while game.runing:
        
        if game.playing:
            game.game_loop()
        else:
            while len(game.state_stack) > 1:
                game.state_stack.pop()
            game.playing = True
        
    

