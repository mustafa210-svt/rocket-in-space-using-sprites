import pygame

#screen dimensions and title
WIDTH = 600
HEIGHT = 600
TITLE = "SPACE ROCKET USING SPRITE"

#setting up the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

#image variables
bg = pygame.image.load("space background.png")
rocket = pygame.image.load("rocket.png")
#Variables
run = True
# rocketclass
class Sr(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()#calling constructer of sprite class
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


 #objects
rocket1 = Sr(rocket,300,300)   
#group of sprites 
gs = pygame.sprite.Group()
gs.add(rocket1)
        


#While loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    #drawing the background and sprite
    screen.blit(bg,(0,0))
    gs.draw(screen)
    #event
    key_pressed = pygame.key.get_pressed()
    #W KEY
    if key_pressed[pygame.K_w]:
        rocket1.rect.y = rocket1.rect.y - 5
    #S key
    if key_pressed[pygame.K_s]:
        rocket1.rect.y = rocket1.rect.y + 5
    #A key
    if key_pressed[pygame.K_a]:
        rocket1.rect.x = rocket1.rect.x - 5
    #D key
    if key_pressed[pygame.K_d]:
        rocket1.rect.x = rocket1.rect.x + 5 
    
    #screen border
    #x cord
    if rocket1.rect.right >= 600:
        rocket1.rect.right = 600
    if rocket1.rect.left <= 0:
        rocket1.rect.left = 0
    #y cord
    if rocket1.rect.bottom >= 600:
        rocket1.rect.bottom = 600
    if rocket1.rect.top <= 0:
        rocket1.rect.top = 0





    pygame.display.update()
   
