import pygame
from pygame.locals import *
import os 
pygame.init()

diretorio_principal = os.path.dirname(__file__)
diretorio_sprites = os.path.join(diretorio_principal,'sprites')
#diretorio_sons = os.path.join(diretorio_principal,'sons')
largura= 800
altura =600
Branco=(255,255,255)
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('made america')

sprite_sheet = pygame.image.load(os.path.join(diretorio_sprites,'man.png')).convert_alpha()


class MEN_of_America(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagem_man= []
        for i in range(5):
            img=sprite_sheet.subsurface((i*62,0),(62,62))
            img = pygame.transform.scale(img, (48*2, 48*2))
            self.imagem_man.append(img)
        
        self.index_lista = 0    
        self.image=self.imagem_man[self.index_lista]
        self.rect = self.image.get_rect()
        self.pos_y_inicial = 500 - 96//2
        self.rect.center = (100,500)
        self.pula = False
        self.andar = False
    #pular no space
    def pular(self):
        self.pula =True
       #andar com A e D
    def anda(self):
        if event.type== KEYDOWN:
            if event.key == K_d:  
                self.andar = True
                if self.andar ==True:
                    if self.rect.x <=799:
                        self.andar =False
                    self.rect.x += 15
                    if self.index_lista > 1:
                        self.index_lista=0
                    self.index_lista += 0.25
                    self.image = self.imagem_man[int(self.index_lista)]
            if event.key== K_a:
                self.andar = True
                if self.andar ==True:
                    if self.rect.x <=0:
                        self.andar =False
                    self.rect.x -= 15

    def update(self):
        if self.pula == True:
            if self.rect.y <=350:
                self.pula =False
            self.rect.y -= 15
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y +=15
                if self.index_lista > 1 or self.index_lista < 3 :
                        self.index_lista=0
                self.index_lista += 0.50
                self.image = self.imagem_man[int(self.index_lista)]  
            else:
                self.rect.y = self.pos_y_inicial

        MEN_of_America.anda(self)             
               
    


todas_sprites = pygame.sprite.Group()
America = MEN_of_America()
todas_sprites.add(America)



relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    tela.fill(Branco)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if America.rect.y != America.pos_y_inicial:
                    pass
                else:
                 America.pular()
            if event.key == K_d:
                America.anda()
            if event.key == K_a:
                America.anda()
                        
   
    
    todas_sprites.draw(tela)
    todas_sprites.update()

    pygame.display.flip()       