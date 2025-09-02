import pygame
from pygame.locals import *
pygame.display.set_caption("bouncing ball")
pos_x = 350
pos_y = 600
pygame.init()
running = True
vectolity = 35
screen = pygame.display.set_mode((800, 400), pygame.RESIZABLE)
clock = pygame.time.Clock()


image = pygame.image.load('piła.png').convert_alpha()
place = image.get_rect(topleft=((pos_x), (pos_y)))

while running:
    if vectolity <= -30:
        vectolity = 29
    pos_y -= vectolity
    vectolity -= 1
    place = image.get_rect(topleft=((pos_x), (pos_y)))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.VIDEORESIZE:
            width, height = ev.size
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        if ev.type == pygame.QUIT:
            running = False

    clock.tick(60)
    screen.fill((0, 0, 0))
    screen.blit(image, place)
    pygame.display.update()

pygame.quit()