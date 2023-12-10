import pygame
import sys


pygame.init()


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 750


WHITE = (255, 255, 255)


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Гача")


background_image = pygame.image.load("Фон.jpg")
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))


button_images = []
button_images.append(pygame.image.load("2и.jpg"))
button_images.append(pygame.image.load("3и.jpg"))
button_images.append(pygame.image.load("4и.jpg"))
button_images.append(pygame.image.load("5и.jpg"))
button_images.append(pygame.image.load("6и.jpg"))

for i in range (5):
    # button_images[i].set_colorkey(WHITE)
    button_images[i] = pygame.transform.scale(button_images[i], (WINDOW_WIDTH//2, WINDOW_HEIGHT // 9))

button_rects = []
for i in range(5):
    button_rects.append(button_images[i].get_rect())
    button_rects[i].center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4 + i * (WINDOW_HEIGHT // 9 + 10))

# button_prod_image = pygame.image.load("Продолжить.jpg")
# button_prod_image = pygame.transform.scale(button_prod_image, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 9))
# button_prod_image = button_prod_image.get_rect()
# button_prod_image.center = (WINDOW_WIDTH // 4, WINDOW_HEIGHT - 300)

FPS = 30
clock = pygame.time.Clock()


def draw_menu():
    window.blit(background_image, (0, 0))
    for i in range(5):
        window.blit(button_images[i], button_rects[i])


    font = pygame.font.SysFont('arial', 71)
    text = font.render("Выберете количество игроков:", True, (166, 100, 232))
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 10))
    window.blit(text, text_rect)
    font = pygame.font.SysFont('arial', 70)
    text = font.render("Выберете количество игроков:", True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 10))
    window.blit(text, text_rect)

    pygame.display.update()

def count(num_players):
    window.blit(background_image, (0, 0))
    font = pygame.font.SysFont('arial', 70)
    text = font.render(f"Количество игроков: {num_players}", True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    window.blit(text, text_rect)
    # window.blit(button_prod_image, button_prod_image.center)
    pygame.display.update()
    # На окне отображения количества игроков, если нажимается ALT - подтверждается выбор
    # При нажатии Backspace возвращение к выбору количества игроков
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    return False
                elif event.key == pygame.K_BACKSPACE:
                    return True
            else:
                continue

# Обработка событий
def handle_events():
    running = True
    num_players = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(5):
                    if button_rects[i].collidepoint(event.pos):
                        num_players = i + 2
                        running = count(num_players)
                        draw_menu()
                        #running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    num_players = 2
                    #running = False
                elif event.key == pygame.K_3:
                    num_players = 3
                    #running = False
                elif event.key == pygame.K_4:
                    num_players = 4
                    #running = False
                elif event.key == pygame.K_5:
                    num_players = 5
                    #running = False
                elif event.key == pygame.K_6:
                    num_players = 6
                    #running = False
                running = count(num_players)
            draw_menu()

    return num_players


def menu():
    draw_menu()
    num_players = handle_events()

    return num_players

num_players = menu()



# Запуск игры
def game():
    if num_players > 0:
        print("Выбрано количество игроков:", num_players)
        if num_players == 6:
            print("Все карты наград")
            print("12 жетонов")
        if num_players == 5:
            print("Карты без обозначений и карты с обозначением 5+")
            print("10 жетонов")
        else:
            print("Карты без обозначений")
            print("2и - 5 жетонов, 3и - 6 жетонов, 4и - 8 жетонов")
        # Здесь можно добавить код для запуска игры с выбранным количеством игроков

    clock.tick(FPS)
    pygame.quit()
    sys.exit()

class Button:
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color

    def draw_button(self, x, y, message, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(window, (166, 100, 232), (x, y, self.width, self.height))

                if click[0] == 1 and action is not None:
                    action()
        else:
            pygame.draw.rect(window, WHITE, (x, y, self.width, self.height))



# Запуск игры
game()