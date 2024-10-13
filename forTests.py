import pygame
import math

# Инициализация Pygame
pygame.init()

# Устанавливаем размеры окна
screen = pygame.display.set_mode((800, 600))

# Загружаем изображение
image = pygame.image.load('image.png')

# Угол в радианах
angle_rad = math.pi / 4  # Пример: 45 градусов в радианах

# Преобразуем радианы в градусы
angle_deg = math.degrees(angle_rad)

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Вращаем изображение
    rotated_image = pygame.transform.rotate(image, angle_deg)

    # Получаем прямоугольник для центрирования изображения
    rect = rotated_image.get_rect(center=(400, 300))

    # Заполняем экран белым цветом
    screen.fill((255, 255, 255))

    # Рисуем вращенное изображение
    screen.blit(rotated_image, rect.topleft)

    # Обновляем экран
    pygame.display.flip()

# Закрываем Pygame
pygame.quit()
