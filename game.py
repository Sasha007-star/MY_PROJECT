from pygame import *
from random import randint
import time as pytime


font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)

img_back = 'background_fish.png'
hero_img = 'vudka.png'
enemy_img = 'fish.png'

clock = time.Clock()
FPS = 30

score = 0
goal = 50
lost = 0
max_lost = 5

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
        self.player = Player(self, 150, 250, 30, 40, 1)
         
         
class Enemy(GameSprite):
    enemy_x, enemy_y = 300,300
    enemy_width, enemy_width = 100, 100
    object_visible = True
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1
        
             
win_width = 600
win_height = 700
display.set_caption("Fishermen_simulator")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))


vudka = Player(hero_img, 5, win_height - 100, win_width - 80, 100, 10)

monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy(enemy_img, randint
(80, win_width - 80), -40, 80, 50, randint(1,3))
    monsters.add(monster)


finish = False
run = True

while run:  
    if is_fishing:
        time.sleep(time_to_wait)
        fish_caught = randint.choice(True, False) 
    if fish_caught:
        window.blit(hero_img, (randint(100, 100, 100, 100)))
        text1 = font2.render("Риба спіймана!" + str(score), 1, (0, 255,0))
        window.blit(text, (10,50))
    if not finish:
        text = font2.render("Риба не клюнула!" + str(lost), 1, (0, 255,0))
        window.blit(text, (10,50)) 

        vudka.update()
        monsters.update()

        vudka.reset()
        monsters.draw(window)

    collides = sprite.groupcollide(monsters, MOUSEBUTTONDOWN, True, True)
    for collide in collides:
            score = score + 1
            monster = Enemy(
                enemy_img, randint(80, win_width - 80), -40, 80, 50, randint(1, 5)
            )
            monsters.add(monster)
        
    if sprite.spritecollide(monsters, True):
            lost -= 1
            monster = Enemy(
                enemy_img, randint(80,win_width - 80), -40, 80, 50, randint(1,5)
            )
            monsters.add(monster)
        
    if lost >= max_lost:
            finish = True
            mixer.music.stop()
            window.blit(text, (200, 200))
        
    if score >= goal:
            finish = True
            mixer.music.stop()
            window.blit(text1, (200, 200))  


display.update() 
clock.tick(FPS) 
