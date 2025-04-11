import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (251,84,5)
BLACK = (0, 0, 0)
WHITE = (240,240,240)
running = True
speed = 1

puntos_poligono = [
    (300,200),(310,180),(320,200),(385,198),(390,185),(400,200),
    (460,200),(465,187),(480,280),(465,400),(460,380),(390,380),
    (385,400),(378,378),(310,380),(295,405),(280,380),(210,380),
    (200,400),(195,380),(130,380),(125,400),(110,280),(125,185),
    (130,205),(190,200),(200,185),(205,200),(270,200),(280,180),
    (290,200),(300,200)
]

while running:
    screen.fill(RED)

    

    pygame.draw.polygon(screen, BLACK, puntos_poligono)
    pygame.display.flip()
    pygame.time.delay(3) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    puntos_poligono = [(x + speed, y) for x, y in puntos_poligono]


    if all(x > WIDTH for x, y in puntos_poligono):
        puntos_poligono = [(x - WIDTH - 100, y) for x, y in puntos_poligono]



pygame.quit()

