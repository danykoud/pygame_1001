import pygame

pygame.init()          

size = width, height = 600, 400 # set a variable for the size of the widow
 
WHITE = (255, 255, 255)                     # RGB color / red , green , and blue

screen = pygame.display.set_mode(size)  # we create a graphical window with the call to pygame.display.set_mode()


# loading images
spaceship = pygame.image.load("images/spaceship.png") 
background=pygame.image.load("images/background.png")  
bullet=pygame.image.load("images/bullet.png")
bullet=pygame.transform.scale(bullet, (25,15))
ufo= pygame.image.load("images/ufo.png")
ufo= pygame.transform.scale(ufo, (50,50))

background= pygame.transform.scale(background, (width, height))    
spaceship= pygame.transform.scale(spaceship,( 50, 50))
# Game title
pygame.display.set_caption('Star Wars')
# Variables
shipheight=300
shipwidth=300
ufo_posx=300
ufo_posy=20
shipxchange=0
shipychange=0
ufo_move= .6
bulletx=300
bullety=300
bulletstate="ready"
bulletmove=.7

# Game loop

run=True
while run:
      # screen.fill(WHITE)
    screen.blit(background, (0,0)) #display background image
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False  

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                shipxchange= -2
                
            if event.key==pygame.K_RIGHT:
               shipxchange= 2
            if event.key== pygame.K_SPACE:
                bulletstate= "fire"
        if event.type == pygame.KEYUP:
            if event.key== pygame.K_LEFT or event.key== pygame.K_RIGHT :
                shipxchange= 0
                shipychange=0
               
             
    shipwidth += shipxchange
    shipheight += shipychange
    # ufo move
    if ufo_posx >= width-50:
        ufo_posy += 20
        ufo_move= - .6
    if ufo_posx <=0:
        ufo_posy += 20
        ufo_move= .6
    ufo_posx += ufo_move
    # spaceship limits
    if shipwidth >= width -50:
        shipwidth= width -50
    if shipwidth <=0 :
        shipwidth= 0

    # bullet
    # if bulletstate is "fire":
    #     bullety -= bulletmove
    # if bullety < 0 :
    #     bullety= 308
    #     bulletstate= "ready"

#    display surfaces
    screen.blit(bullet,(shipwidth + 13,bullety+ 8))
    screen.blit(spaceship, (shipwidth,shipheight))
    screen.blit(ufo, (ufo_posx,ufo_posy))
    
    pygame.display.flip()
pygame.quit()
