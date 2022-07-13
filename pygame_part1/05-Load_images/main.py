import  pygame


size = width, height = 600, 400 # set a variable for the size of the widow
 
WHITE = (255, 255, 255)                     # RGB color / red , green , and blue

screen = pygame.display.set_mode(size)  # we create a graphical window with the call to pygame.display.set_mode()

spaceship = pygame.image.load("images/spaceship_red.png")        # we load our ball image
spaceship= pygame.transform.scale(spaceship,( 50, 50))
pygame.display.set_caption('Star Wars')
shipheight=300
shipwidth=300
shipychange=.1
shipxchange=.1
run=True
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False   
    
  
    screen.fill(WHITE)
    screen.blit(spaceship, (shipwidth,shipheight))
    pygame.display.flip()
pygame.quit()
