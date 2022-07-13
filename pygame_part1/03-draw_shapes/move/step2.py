from click import Parameter
import pygame 

# Initialize the game engine
pygame.init()
size = width, height = 420, 500 # set  variables for the size of the window
white=255,255,255 
RED=255,0,0 
BLUE= 0,0,255                   # RGB color / red , green , and blue / 0-255
window=pygame.display.set_mode((size)) # we create a graphical window with the call to pygame.display.set_mode()
pygame.display.set_caption('Square!')
# define Parameters as variables
Location_x= 210
Location_y=250
rec_h= 40
rec_w=50
step =0.01

run=True
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False
        
    if Location_x<=0 :
        step =.01
    elif Location_x>=width- rec_w:
        step = -.01
    Location_x += step
   
    
    window.fill(white)
    
    pygame.draw.rect(window,RED, [Location_x, Location_y, rec_w, rec_h])
    pygame.display.update()
