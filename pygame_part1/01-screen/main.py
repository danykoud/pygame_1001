import pygame 


# Initialize the game engine
pygame.init()
size = width, height = 420, 500 # set  variables for the size of the window
black=0,0,0  
white=255,255,255  
RED= 255,0,0                   # RGB color / red , green , and blue / 0-255
window=pygame.display.set_mode((size)) # we create a graphical window with the call to pygame.display.set_mode()
pygame.display.set_caption('My first game!')



run=True #Boolean
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False



    window.fill(white)
    



    
    
    pygame.display.update()
