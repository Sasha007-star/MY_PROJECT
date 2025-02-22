from pygame import *
from random import randint
from time import pytime

clock = time.Clock()
FPS = 30

score = 0
goal = 50
lost = 0
max_lost = 5

img_back = "background_fish.jpg"
hero_img = "vudka.png"
enemy_img = ("fish.png", (60, 70))

fish_caught = 0
is_fishing = False
time_to_wait = 3
running = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width -80:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1
        
        if is_fishing:
            time.sleep(time_to_wait)
            fish_caught = random.choice(True, False)
    
        

            
win_width = 800
win_height = 800
display.set_caption("Fishermen_simulator")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

vudka = Player(hero_img, 5, win_height - 100, 80, 100, 10)


