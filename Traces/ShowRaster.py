import pygame

screen_height = 400
screen_width = 714

screen = pygame.display.set_mode((screen_width,screen_height))


done = False
# Add a title to window
pygame.display.set_caption("A beautiful sunset")

# load background image
background = pygame.image.load('sunset.jpg')
sprite = pygame.image.load('charasprite.png')


while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            done = True
    screen.blit(background,(0,0))
    screen.blit(sprite,(100,100))
    pygame.display.update()
pygame.quit()
