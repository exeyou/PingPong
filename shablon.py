from pygame import *
import math
init()

class GameSprite(sprite.Sprite):
    def __init__(self, image1, x, y, speed, width, height):
        super().__init__()

        self.image = ...
        self.speed = ...

        self.rect = ...
        self.rect.x = ...
        self.rect.y = ...

    def reset(self):
        win.blit(..., (..., ...))

class Player(GameSprite):
    def update_r(self):
        keys = ...

        if keys[...] and self.rect.y > 5:
            ...

        if keys[...] and self.rect.y < win_height - 80:
            ...

    def update_l(self):
        keys = ...

        if keys[...] and self.rect.y > 5:
            ...

        if keys[...] and self.rect.y < win_height - 80:
            ...

back = (200, 255, 255)
win_width = 600
win_height = 500
win = display.set_mode((..., ...))
win.fill(back)

game = ...
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player(..., ..., ..., ..., ..., ...)
racket2 = Player(..., ..., ..., ..., ..., ...)

ball = GameSprite(..., ..., ..., ..., ..., ...)

font = font.Font(None, 35)
lose1 = font.render("PLAYER 1 LOSE!", True, (180, 0, 0))
lose2 = font.render("PLAYER 2 LOSE!", True, (180, 0, 0))

speed = 5
speedxy = [0, 0]
ang = 15
speedxy[0] = math.cos(math.radians(ang)) * speed
speedxy[1] = math.sin(math.radians(ang)) * speed


while game:
    for e in ...():
        if e.type == ...:
            game = ...

    if not ...:
        win.fill(back)
        racket1.update_l()
        racket2.update_r()

        ball.rect.x += speedxy[0]
        ball.rect.y += speedxy[1]

        if sprite.collide_rect(..., ...) or sprite.collide_rect(..., ...):
            speedxy[0] *= -1

        if ball.rect.y > win_height - 50 or  ball.rect.y < 0:
            speedxy[1] *= -1

        if ball.rect.x < 0:
            finish = True
            win.blit(..., (200, 200))

        if ball.rect.x > win_width:
            finish = True
            win.blit(..., (200, 200))

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
