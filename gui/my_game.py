import pygame

pygame.init()
background = pygame.display.set_mode((400,300))
pygame.display.set_caption('게임만들기')


x_Pos=200
y_pos=150
image_dino= pygame.image.load('dino.png)')
image_dino=pygame.transform.scale(image_dibo,(50,50))
font=ptgame.font.stsfont

play = True
while play:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play=False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('up')
                y_Pos=y_pos-10
            elif event.key == pygame.K_DOWN:
                print('down')
                y_pos=y_pos+10
                x_Pos +=10
            elif event.key == pygame.K_LEFT:
                print('left')
                x_Pos -=10
            elif event.key == pygame.K_RIGHT:
                print('right')    
    background.fill((255,0,0))
    #pygame.draw.circle(background,(0,0,255), (x_Pos,y_Pos),10)
    text=font.render('구암고',True,(0,0,0))
    pygame.display.update()
    
    
pygame.quit()
