import pygame 


size = width, height = 400, 300
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
screen=pygame.display.set_mode((size))
pygame.display.set_caption('My game!')

location_x=200
location_y=150
square_x=50
step= .01
run=True
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False

    location_x -= step
    if location_x <=0:
        step=-.01
    if location_x>= width - square_x:
        location_x= width - square_x
   

    screen.fill(WHITE)
    # Draw a rectangle outline
    pygame.draw.rect(screen, BLACK, [location_x, location_y, square_x, 50])
    

    
    pygame.display.update()