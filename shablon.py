from pygame import *
import math
import random
init()

# Клас GameSprite представляє гравця або м'яч
class GameSprite(sprite.Sprite):
    def __init__(self, image_path, x, y, speed, width, height):
        super().__init()

        self.image = image.load(image_path)
        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

# Клас Player успадковує від GameSprite та представляє гравця
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed

back = (200, 255, 255)
win_width = 600
win_height = 500
win = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong Game")
win.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

# Створення ракеток та м'яча
racket1 = Player("racket.png", 30, win_height // 2 - 50, 4, 15, 100)
racket2 = Player("racket.png", win_width - 45, win_height // 2 - 50, 4, 15, 100)
ball = GameSprite("ball.png", win_width // 2 - 20, win_height // 2 - 20, 4, 30, 30)
font = font.Font(None, 35)
lose1 = font.render("PLAYER 1 LOSE!", True, (180, 0, 0))
lose2 = font.render("PLAYER 2 LOSE!", True, (180, 0, 0))

# Функція для перевірки, чи мишка над кнопкою "Start"
def is_mouse_over(rect):
    mouse_pos = mouse.get_pos()
    return rect.collidepoint(mouse_pos)

# Функція для малювання кнопки "Start"
def draw_start_button():
    start_button_rect = Rect(win_width // 2 - 50, win_height // 2 - 25, 100, 50)
    start_button_color = (0, 255, 0)
    start_button_text = font.render("Start", True, (0, 0, 0))

    draw.rect(win, start_button_color, start_button_rect)
    text_rect = start_button_text.get_rect(center=start_button_rect.center)
    win.blit(start_button_text, text_rect)
    return start_button_rect

# Функція для малювання кнопки "Retry"
def draw_retry_button():
    retry_button_rect = Rect(win_width // 2 - 50, win_height // 2 + 25, 100, 50)
    retry_button_color = (0, 255, 0)
    retry_button_text = font.render("Retry", True, (0, 0, 0))

    draw.rect(win, retry_button_color, retry_button_rect)
    text_rect = retry_button_text.get_rect(center=retry_button_rect.center)
    win.blit(retry_button_text, text_rect)
    return retry_button_rect

retry_screen = False
speed = 4
speedxy = [0, 0]
ang = random.randint(30, 60)
speedxy[0] = math.cos(math.radians(ang)) * speed
speedxy[1] = math.sin(math.radians(ang)) * speed

# Функція для генерації випадкового кута руху м'яча
def generate_random_angle():
    speed = random.randint(6, 12)
    new_ang = random.randint(30, 60)
    speedxy[0] = math.cos(math.radians(new_ang)) * speed
    speedxy[1] = math.sin(math.radians(new_ang)) * speed

start_screen = True
game_over = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if start_screen:
        win.fill(back)
        start_button_rect = draw_start_button()
        display.update()

        # Перевірка натискання кнопки "Start"
        if mouse.get_pressed()[0] and is_mouse_over(start_button_rect):
            start_screen = False
    else:

        if not finish:
            win.fill(back)
            racket1.update_l()
            racket2.update_r()
            ball.rect.x += speedxy[0]
            ball.rect.y += speedxy[1]

            # Перевірка зіткнення м'яча з ракетками
            if sprite.collide_rect(ball, racket1):
                if ball.rect.y < racket1.rect.y + racket1.rect.height / 2:
                    generate_random_angle()
                    speedxy[0] = abs(speedxy[0])
                    speedxy[1] = -abs(speedxy[1])
                else:
                    generate_random_angle()
                    speedxy[0] = abs(speedxy[0])
                    speedxy[1] = abs(speedxy[1])

            if sprite.collide_rect(ball, racket2):
                if ball.rect.y < racket2.rect.y + racket2.rect.height / 2:
                    generate_random_angle()
                    speedxy[0] = -abs(speedxy[0])
                    speedxy[1] = -abs(speedxy[1])
                else:
                    generate_random_angle()
                    speedxy[0] = -abs(speedxy[0])
                    speedxy[1] = abs(speedxy[1])

            # Перевірка зіткнення м'яча з верхньою або нижньою стінкою
            if ball.rect.y > win_height - ball.rect.height or ball.rect.y < 0:
                speedxy[1] *= -1

            # Перевірка виходу м'яча за ліву стінку
            if ball.rect.x < 0:
                finish = True
                win.blit(lose1, (200, 200))

            # Перевірка виходу м'яча за праву стінку
            if ball.rect.x > win_width:
                finish = True
                win.blit(lose2, (200, 200))

            racket1.reset()
            racket2.reset()
            ball.reset()
        elif game_over:

            retry_button_rect = draw_retry_button()
            display.update()

            # Перевірка натискання кнопки "Retry"
            if mouse.get_pressed()[0] and is_mouse_over(retry_button_rect):
                finish = False
                game_over = False
                ball.rect.x = win_width // 2 - 20
                ball.rect.y = win_height // 2 - 20
                generate_random_angle()
        else:
            display.update()
            game_over = True
    display.update()
    clock.tick(FPS)

quit()
