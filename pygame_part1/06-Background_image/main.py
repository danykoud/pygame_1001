import sys, pygame
pygame.init()           #

size = width, height = 600, 400 # set a variable for the size of the widow
 
WHITE = (255, 255, 255)                     # RGB color / red , green , and blue

screen = pygame.display.set_mode(size)  # we create a graphical window with the call to pygame.display.set_mode()

spaceship = pygame.image.load("images/spaceship.png") 
background=pygame.image.load("images/background.png")  
background= pygame.transform.scale(background, (width, height))     # we load our images
spaceship= pygame.transform.scale(spaceship,( 50, 50))
pygame.display.set_caption('Star Wars')
shipheight=300
shipwidth=300
shipychange=1.2
shipxchange=1.2
run=True
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False   
    
    shipheight += shipychange
    if shipheight <= 0:
        shipychange = 1.2
    elif shipheight >=300:
        shipychange= -1.2
    shipwidth += shipxchange
    if shipwidth <= 0:
        shipxchange = 1.2
    elif shipwidth >=550:
        shipxchange= -1.2
    screen.fill(WHITE)
    screen.blit(background, (0,0))
    screen.blit(spaceship, (shipwidth,shipheight))
    pygame.display.flip()
pygame.quit()
