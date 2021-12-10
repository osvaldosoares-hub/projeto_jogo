import pygame
from pygame import constants
import cosntantes
#import sprites
import os


class MEN_of_America:
    def __init__(self):
        #criando a tela
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((cosntantes.LARGURA,cosntantes.ALTURA))
        pygame.display.set_caption(cosntantes.TITULO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando=True
        self.fonte = pygame.font.match_font(cosntantes.FONT)
        self.carregar_aqr()
    def novo_jogo(self):
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()
    def rodar(self):
        #loop do jogo
        self.jogando =True
        while self.jogando:
            self.relogio.tick(cosntantes.FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()
    def eventos(self):
        #define eventos 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando =False
                self.esta_rodando=False
    def atualizar_sprites(self):
            self.todas_as_sprites.update

    def desenhar_sprites(self):
        self.tela.fill(cosntantes.BRANCO)
        self.todas_as_sprites.draw(self.tela)
        pygame.display.flip()
    
    def carregar_aqr(self):
        
        diretorio_imagens = os.path.join(os.getcwd(),'imagens')
        self.diretorios_audios = os.path.join(os.getcwd(),'sons')
        self.spritesheet = os.path.join(diretorio_imagens,cosntantes.SPRITESHEET)
        self.man_start_logo = os.path.join(diretorio_imagens, cosntantes.LOGO)
        self.man_start = pygame.image.load(self.man_start_logo).convert()
    
    
    def mostrar_texto(self, texto,tamanho,cor,x,y):
        fonte = pygame.font.Font(self.fonte,tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop=(x,y)
        self.tela.blit(texto,texto_rect)
    
    
    def mostrar_logo(self,x,y):
        start_logo_rect =  self.man_start_logo.get_rect()
        
       
        start_logo_rect.midtop= (x,y)
        self.tela.blit(self.man_start_logo,start_logo_rect)

    def mostrar_tela_start(self):
        self.mostrar_logo(0,20)

        pygame.mixer.music.load(os.path.join(self.diretorios_audios,cosntantes.MUSICA))
        pygame.mixer.music.play()
        self.mostrar_texto(
            '-pressione uma tecla pra jogar',
            62,
            cosntantes.BRANCO,
            cosntantes.LARGURA/2,
            320
        )
        self.mostrar_texto(
            'desenvolvido por Osvaldo, Igor e henrique',
            22,
            cosntantes.BRANCO,
            cosntantes.LARGURA/2,
            520
        )
        pygame.display.flip()
        self.esperar_por_jogador()

    def esperar_por_jogador(self):
        esperando=True
        while esperando:
            self.relogio.tick(cosntantes.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando=False
                    self.esta_rodando=False
                if event.type == pygame.KEYUP:
                    esperando =False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.diretorios_audios,cosntantes.TECLA_START)).play()        
        
    def Game_over(self):
        pass
g= MEN_of_America()
g.mostrar_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.Game_over()
''' pygame.sprite.Sprite.__init__(self)
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




while True:
    
    
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

    pygame.display.flip()       '''