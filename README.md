# pyprogram
# Импортируем модуль для игр pygame
import pygame
import random
 
# Инициализируем движок pygame
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
 
# размеры окна с анимацией
SIZE = [400, 400]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")
 
# пустой список
snow_list = []
 
# Пройдемся 50 раз циклом и добавьм снежинки в рандомную позицию x,y
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])
 
clock = pygame.time.Clock()
 
# Снег будет идти до тех пор пока не нажмется кнопка стоп
done = False
while not done:
 
    for event in pygame.event.get():   # Пользователь сделал что-то
        if event.type == pygame.QUIT:  # Если нажато стоп
            done = True   # выходим из цикла
 
    # цвет backgrounda
    screen.fill(BLACK)
 
    # обработка каждой снежинки
    for i in range(len(snow_list)):
 
        # нарисовать снежинку
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
 
        # снежинка вниз на 1
        snow_list[i][1] += 1
 
        if snow_list[i][1] > 400:
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            x = random.randrange(0, 400)
            snow_list[i][0] = x
 
    # обновление screen с новыми данными и позициями снежинок
    pygame.display.flip()
    clock.tick(20)
pygame.quit()
