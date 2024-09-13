# import pygame
# # import os
# # WIDTH,HEIGHT=900,500
# # WIN=pygame.display.set_mode((WIDTH,HEIGHT))
# # pygame.display.set_caption("first game")
# # WHITE=(255,255,255)
# # FBS=60
# # yellow_spaceship_image=pygame.image.load(os.path.join('assets','spaceship_yellow.png'))
# # yellow_spaceship_image=pygame.image.load(os.path.join('assets','spaceship_red.png'))
# #
# # def draw_widnow():
# #     WIN.fill(WHITE)
# #     WIN.blit(yellow_spaceship_image,(300,100))
# #     pygame.display.update()
# #
# # def main():
# #     Clock=pygame.time.Clock()
# #     run =True
# #     while run:
# #         Clock.tick(FBS)
# #         for event in pygame.event.get():
# #             if event.type==pygame.QUIT:
# #                 run = False
# #         draw_widnow()
# #     pygame.quit()
# #
# #
# # if __name__ =="__main__":
# #     main()
import sys

import pygame
import os
pygame.font.init()
pygame.mixer.init()
HEALTH_FONT=pygame.font.SysFont("comicsans",40)
WIN_FONT=pygame.font.SysFont("comicsans",100)
FPS=60
VEL=5
pygame.init()
WHITE=(255,255,255)
YELLOW=(250,255,0)
RED=(255,0,0)
BULLET_HIT_SOUND=pygame.mixer.Sound(os.path.join("Assets","Grenade+1.mp3"))
BULLET_FIRE_SOUND=pygame.mixer.Sound(os.path.join("Assets","Gun+silencer.mp3"))

WIDTH,HEIGHT=900,500
SPACESHIP_WIDTH=70
SPACESHIP_HEIGHT=50
window=pygame.display.set_mode((WIDTH,HEIGHT))
YELLOW_SPACESHIP=pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
RESIZED_ROTATED_YELLOW=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP=pygame.image.load(os.path.join("Assets","spaceship_red.png"))
SPACE=pygame.transform.scale(pygame.image.load(os.path.join("Assets","space.png")),(WIDTH,HEIGHT))
RESIZED_ROTATED_RED=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
x_position=300
y_position=100
BORDER=pygame.Rect(WIDTH//2 -5,0,10,HEIGHT)
YELLOW_BULLETS=[]
RED_BULLETS=[]
MAX_BULLETS=3
BULLET_VEL=20
YELLOW_HIT=pygame.USEREVENT +1
RED_HIT=pygame.USEREVENT +2


def draw(reds,yellows,red_bullets,yellow_bullets,yellow_health,red_health):
    window.fill(WHITE)

    window.blit(SPACE,(0,0,100,200))
    red_health_text=HEALTH_FONT.render("HEALTH: " + str(red_health),1,WHITE)
    yellow_health_text=HEALTH_FONT.render("HEALTH: " + str(yellow_health),1,WHITE)
    window.blit(red_health_text,(WIDTH - red_health_text.get_width() -10,10))
    window.blit(yellow_health_text,(10,10))
    window.blit(RESIZED_ROTATED_YELLOW, (yellows.x, yellows.y))
    window.blit(RESIZED_ROTATED_RED, (reds.x, reds.y))
    for bullet in red_bullets:
        pygame.draw.rect(window,RED,bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(window, YELLOW,bullet)




    pygame.draw.rect(window,(0,0,0),BORDER)



    pygame.display.update()


def handle_win(text):
    win_text=WIN_FONT.render(text,1,WHITE)
    window.blit(win_text,(WIDTH/2 - win_text.get_width()//2,HEIGHT//2 - win_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)
def yellow_handle_movement(keys_pressed,yellow):

    if keys_pressed[pygame.K_a] and yellow.x - VEL> 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and  yellow.x +VEL + yellow.width < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y >0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow .y < HEIGHT -SPACESHIP_HEIGHT:
        yellow.y += VEL

def red_handle_movement(keys_pressed,red):


    if keys_pressed[pygame.K_LEFT] and red.x > WIDTH/2 + SPACESHIP_WIDTH/8:
         red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x < WIDTH - SPACESHIP_WIDTH :
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y < HEIGHT - SPACESHIP_HEIGHT:
        red.y += VEL

def handle_bullets(yellow_bullets,red_bullets,yellow,red):
    for bullet in yellow_bullets:
        bullet.x +=BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)


    for bullet in red_bullets:
        bullet.x -=BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        if bullet.x <0 :
            red_bullets.remove(bullet)







def main():
    red_health = 10
    yelllow_health = 10
    red=pygame.Rect(700,HEIGHT/2,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow=pygame.Rect(100,HEIGHT/2,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    run=True
    Clock=pygame.time.Clock()
    while run:
        Clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False
                pygame.quit()


            key_pressed=pygame.key.get_pressed()


            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RCTRL and len(RED_BULLETS) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x , red.y + red.height // 2 - 2, 10, 5)
                    RED_BULLETS.append(bullet)
                    BULLET_FIRE_SOUND.play()


                if event.key==pygame.K_SPACE and len(YELLOW_BULLETS) < MAX_BULLETS:
                    bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                    YELLOW_BULLETS.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type==RED_HIT:
                red_health -=1
                BULLET_HIT_SOUND.play()
            if event.type==YELLOW_HIT:
                yelllow_health-=1
                BULLET_HIT_SOUND.play()

        win_statment=""
        if yelllow_health<=0:
            win_statment="RED WINS !"

        if red_health <=0:
            win_statment="YELLOW  WINS !"

        if win_statment !="":
            handle_win(win_statment)
            break











        keys_pressed=pygame.key.get_pressed()

        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        handle_bullets(YELLOW_BULLETS,RED_BULLETS,yellow,red)




        draw(red,yellow,RED_BULLETS,YELLOW_BULLETS,yelllow_health,red_health)




    main()





if __name__=="__main__":
    main()