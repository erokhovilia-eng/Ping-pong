from pygame import *

win_width = 600
win_height = 500
win = display.set_mode((win_width, win_height))
display.set_caption('Пинг-понг')
win.fill((200, 255, 255))

font.init()
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

ball = GameSprite('soccer.png2.webp', 300, 0, 3)
speed_x = 3
speed_y = 3
left = Player('palochka.png', 100, 0, 3)
right = Player('palochka.png', 500, 0, 3)

font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (100, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (100, 0, 0))
