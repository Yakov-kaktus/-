import sys
import random
import pygame
pygame.init()
clock = pygame.time.Clock()
width = 1280 #длина окна
height = 960 #высота окна
g = pygame.image.load(f"gf.png") # загрузка фона
window = pygame.display.set_mode((width, height)) # создание окна
animation_set_left = [pygame.image.load(f"l{i}.png") for i in range(1, 6)]
animation_set_right = [pygame.image.load(f"r{i}.png") for i in range(1, 6)]# загрузка кадров анимации
i = 1
x_player = random.randint(1, width) # игрок по длине
y_player = random.randint(1, height) # игрок по высоте
player_stay = pygame.image.load(f"0.png")
player_stay_sad = pygame.image.load(f"0u20.png")
secnd = 10000 # кадры в секунду
def chih():
    window.blit(g, (0, 0)) #функция отчистки экрана и заполнения фоном
gamer = player_stay_sad # переменная изображения игрока
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                while True:
                    chih()
                    window.blit(animation_set_left[i // 12], (x_player, y_player))
                    if i % 12 == 0:
                        x_player -= 3
                    i += 1
                    if i == 60:
                        i = 0
                        break

                    pygame.display.flip()
                    clock.tick(secnd)
                    gamer = player_stay
            elif event.key == pygame.K_RIGHT:
                while True:
                    chih()
                    window.blit(animation_set_right[i // 12], (x_player, y_player))
                    if i % 12 == 0:
                        x_player += 3
                    i += 1
                    if i == 60:
                        i = 0
                        break
                    pygame.display.flip()
                    clock.tick(secnd)
                    gamer = player_stay
            elif event.key == pygame.K_UP:
                chih()
                y_player -= 15
                gamer = player_stay_sad
            elif event.key == pygame.K_DOWN:
                chih()
                y_player += 15
                gamer = player_stay
        chih()
        window.blit(gamer, (x_player, y_player))
        pygame.display.flip()
