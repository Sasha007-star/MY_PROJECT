from pygame import *
from random import randint, choice

path_music = "mp3.ogg"
mixer.init() 
mixer.music.load(path_music)
mixer.music.play()

# Ініціалізація
font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)

# Зображення
img_back = 'background_fish.jpg'
hero_img = 'vudka.png'
enemy_img = 'fish.png'

# Налаштування
clock = time.Clock()
FPS = 30
score = 0
goal = 50
lost = 0
max_lost = 5

win_width = 600
win_height = 700
display.set_caption("Fishermen_simulator")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# Клас спрайта
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Гравець (вудка)
class Player(GameSprite):
    def update(self):
        self.rect.x, self.rect.y = mouse.get_pos()  # Вудка рухається за мишею
        self.rect.y = win_height - 120  # Фіксуємо її по вертикалі

# Вороги (рибки)
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.direction = choice([-1, 1])  # Випадковий напрямок (ліворуч чи праворуч)
    
    def update(self):
        self.rect.x += self.speed * self.direction  # Рух горизонтально

        # Якщо рибка виходить за межі екрану, збільшуємо лічильник втрачених і видаляємо її
        if self.rect.x < 0 or self.rect.x > win_width:
            global lost
            lost += 1
            self.kill()  # Видаляємо рибку з групи

# Створення об'єктів
vudka = Player(hero_img, 250, win_height - 120, 80, 100, 20)
fishes = sprite.Group()
for i in range(5):
    fish = Enemy(enemy_img, randint(80, win_width - 80), randint(100, 500), 80, 50, randint(1, 3))
    fishes.add(fish)

finish = False
run = True

# Головний цикл гри
while run:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == MOUSEBUTTONDOWN:
            for fish in fishes:
                if fish.rect.collidepoint(e.pos):  # Перевіряємо доторк миші
                    fishes.remove(fish)  # Видаляємо рибу
                    score += 1
                    new_fish = Enemy(enemy_img, randint(80, win_width - 80), randint(100, 500), 80, 50, randint(1, 3))
                    fishes.add(new_fish)
    
    if not finish:
        text = font2.render(f"Спіймано: {score} | Втрачено: {lost}", 1, (255, 255, 255))
        window.blit(text, (10, 10))
        
        vudka.update()
        fishes.update()
        vudka.reset()
        fishes.draw(window)

    if score >= goal:
        finish = True
        window.blit(font1.render("Ти переміг!", True, (0, 255, 0)), (200, 300))
    
    if lost == max_lost:
        finish = True
        window.blit(font1.render("Ти програв!", True, (255, 0, 0)), (200, 300))
    
    display.update()
    clock.tick(FPS)     
