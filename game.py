import pygame
import os
import sys


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('fon.jpg'), (500, 500))
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mar.png')

tile_width = tile_height = 50

# основной персонаж
player = None
# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def generate_level(level):
    global player_group
    new_player, x, y = None, None, None
    player_group = pygame.sprite.Group()
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)


def hod(lvl, x, y, l_x, l_y, x1, y1):
    if 0 <= x < l_x and 0 <= y < l_y and lvl[y][x] != "#":
        s = list(lvl[y])
        s[x] = "@"
        lvl[y] = "".join(s)

        s = list(lvl[y1])
        s[x1] = "."
        lvl[y1] = "".join(s)
        return lvl, x, y
    return lvl, x1, y1


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Поле')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    lvl = load_level('map.txt')
    f = False
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            if lvl[i][j] == "@":
                y = i
                x = j
                f = True
                break
        if f:
            break

    player, level_x, level_y = generate_level(lvl)
    running = True
    start_screen()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lvl, x, y = hod(lvl, x - 1, y, level_x, level_y, x, y)
                if event.key == pygame.K_RIGHT:
                    lvl, x, y = hod(lvl, x + 1, y, level_x, level_y, x, y)
                if event.key == pygame.K_UP:
                    lvl, x, y = hod(lvl, x, y - 1, level_x, level_y, x, y)
                if event.key == pygame.K_DOWN:
                    lvl, x, y = hod(lvl, x, y + 1, level_x, level_y, x, y)
                player, level_x, level_y = generate_level(lvl)

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        tiles_group.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
        pygame.display.update()

