import sys
import pygame

ancho = 640
alto=480

#Color de fondo
color_fondo=(0,0,64)

#Clases para el objeto del juego 
class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #cargar la imagen
        self.image=pygame.image.load('imagenes/bolita.png')
        #optener el rectangulo de la imagen
        self.rect=self.image.get_rect()
        #establecer la posición inicial
        self.rect.centerx= ancho/2
        self.rect.centery= alto/2
        #establecer la velocidad de la bolita
        self.speed=[3,3]
        
    def update(self):
        #evitamos que la bolita salga del cuadro
        if self.rect.bottom >= alto or self.rect.top<=0:
            self.speed[1]=-self.speed[1]
        elif self.rect.right>=ancho or self.rect.left<=0:
            self.speed[0]=-self.speed[0]
            
        self.rect.move_ip(self.speed)
        
class Paleta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #cargar la imagen
        self.image=pygame.image.load('imagenes/paleta.png')
         #optener  la imagen
        self.rect=self.image.get_rect()
        self.rect.midbottom=(ancho/2,alto-20)
        self.speed=[0,0]
        
    def update(self,evento):
         #buscar si se presiono el boton de la derecha
        if evento.key==pygame.K_LEFT and self.rect.left>0:
            self.speed=[-5,0]
        elif evento.key==pygame.K_RIGHT and self.rect.right<ancho:
            self.speed=[5,0]
        else:
            self.speed=[0,0]  
        #mover el base a posición actual
        self.rect.move_ip(self.speed)
         
class Ladrillo(pygame.sprite.Sprite):
    def __init__(self,posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('imagenes/ladrillo.png')
        self.rect=self.image.get_rect()
        self.rect.topleft=posicion
        
class Muro(pygame.sprite.Group):
    def __init__(self,cantidad):
        pygame.sprite.Group.__init__(self)
        pos_x=0
        pos_y=20
        for i in range(cantidad):
            ladrillo=Ladrillo((pos_x,pos_y))
            self.add(ladrillo)
            pos_x += ladrillo.rect.width
            if pos_x >= ancho:
                pos_x=0
                pos_y+=ladrillo.rect.height
        
             
#Creamos un reloj, bolita, pantalla
reloj = pygame.time.Clock()    
pantalla = pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("Mi Primer Video Juego ")

#ajustamos la restricción del evento de tecla preionada
pygame.key.set_repeat(30)

#creamos objetos
bolita = Bolita()
juagador= Paleta()
muro=Muro(50)

while True:
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            sys.exit()
        elif evento.type==pygame.KEYDOWN:
            juagador.update(evento)
            
    #actualizamos la posición de la bolita
    bolita.update()
    
    #*********************colición**************
    #colicion entre bolita y jugador
    if pygame.sprite.collide_rect(bolita,juagador):
        bolita.speed[1]=-bolita.speed[-1]

    
    
    #*******************************************
    
    
    #pintamos el fondo de la pantalla
    pantalla.fill(color_fondo)
    #dibujamos bolita en la pantalla
    pantalla.blit(bolita.image,bolita.rect)
    #dibujamos juagdopr en la pantalla
    pantalla.blit(juagador.image,juagador.rect)
    #dibujamos el muro
    muro.draw(pantalla)
    
    pygame.display.flip()
    