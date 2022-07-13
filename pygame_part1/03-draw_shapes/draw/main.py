import pygame 
# circle  / pygame.draw.circle()
# circle(surface, color, center, radius) -> Rect
# circle(surface, color, center, radius, width=0, draw_top_right=None, 
# draw_top_left=None, draw_bottom_left=None, draw_bottom_right=None)


# pygame.draw.line()
# draw a straight line
# line(surface, color, start_pos, end_pos, width) -> Rect
# line(surface, color, start_pos, end_pos, width=1) -> Rect


# pygame.draw.rect()
# draw a rectangle
# rect(surface, color, rect) -> Rect
# rect(surface, color, rect, width=0, border_radius=0, 
# border_top_left_radius=-1, border_top_right_radius=-1, 
# border_bottom_left_radius=-1, border_bottom_right_radius=-1)


size = width, height = 500, 500
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
screen=pygame.display.set_mode((size))
pygame.display.set_caption('My game!')



run=True
while run:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run=False





            

    screen.fill(WHITE)
    # Draw a rectangle outline
    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
    # Draw a solid rectangle
    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

    # Draw a rectangle with rounded corners
    pygame.draw.rect(screen, GREEN, [115, 210, 70, 40], 10, border_radius=15)
    pygame.draw.rect(screen, RED, [135, 260, 50, 30], 0, border_radius=10, border_top_left_radius=0,
                     border_bottom_right_radius=15)
    # Draw on the screen a GREEN line from (0, 0) to (50, 30) 
    # 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)
 
    # Draw on the screen 3 BLACK lines, each 5 pixels wide.
    # The 'False' means the first and last points are not connected.
    pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
    # Draw a circle
    pygame.draw.circle(screen, BLUE, [60, 250], 40)

     # Draw only one circle quadrant
    pygame.draw.circle(screen, BLUE, [250, 250], 40, 5, draw_top_right=True)
    pygame.draw.circle(screen, RED, [250, 250], 40, 10, draw_top_left=True)
    pygame.draw.circle(screen, GREEN, [250, 250], 40, 5, draw_bottom_left=True)
    pygame.draw.circle(screen, BLACK, [250, 250], 40, 10, draw_bottom_right=True)

    
    pygame.display.update()