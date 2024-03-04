from pygame import *
from random import *

font.init()
win_width = 2000
win_height = 1000
font1 = font.Font(None, 100)
font2 = font.Font(None, 60)
window = display.set_mode((win_width, win_height))
background = image.load('background.jpg')
background = transform.scale(background,(win_width, win_height))
window.blit(background,(0,0))
game = True
stripe1= True
stripe2= True
FPS = 60
i_ping = 0
i_pong = 0
clock = time.Clock()

class Game_sprite(sprite.Sprite):
    def __init__(self,pic,size_x,size_y,x,y,speed):
        super().__init__()
        self.image = transform.scale(image.load(pic),(size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed 
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(Game_sprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 260:            
            self.rect.y += self.speed

class Player2(Game_sprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 260:            
            self.rect.y += self.speed

class Ball(Game_sprite):
    speed_y = 10
    speed_x = 10
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.y >= 850:
            self.speed_y = -self.speed_y



rocket = Player('rocket1.png', 50, 250, 200, 375, 10)
rocket2 = Player2('rocket2.png', 50, 250, 1750, 375, 10)
ball = Ball('ball.png',150,150,675,425,5)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if stripe1:
        if sprite.collide_rect(ball, rocket):
            if ball.rect.left > rocket.rect.left:
                if ball.speed_x <= 0:
                    ball.speed_x = -ball.speed_x
                    i_pong += 1
            else:
                stripe1 = False
                ball.speed_y = -ball.speed_y  
    if stripe2:    
        if sprite.collide_rect(ball, rocket2):  
            if ball.rect.right < rocket2.rect.right:
                if ball.speed_x >= 0:
                    ball.speed_x = -ball.speed_x
                    i_ping += 1
            else:
                stripe2 = False
                ball.speed_y = -ball.speed_y
    window.blit(background,(0,0))
    if ball.rect.x >= 1950:
        text = font1.render('Blue wins!!!',True,(0,0,255))
        window.blit(text, (850,460))
    if ball.rect.x <= 50:
        text3 = font1.render('Red wins!!!',True,(255,0,0))
        window.blit(text3, (850,460))
    text1 = font2.render('Ping:' + str(i_ping),True,(255,0,0))
    window.blit(text1, (1800,40))
    text2 = font2.render('Pong:' + str(i_pong),True,(0,0,255))
    window.blit(text2, (50,40))
    ball.reset()
    ball.update()
    rocket.update()
    rocket2.update()
    rocket.reset()
    rocket2.reset()
    clock.tick(FPS)
    display.update()    
