import pygame


FONT_SIZE = 36
BORDER_COLOR = (63, 27, 14)
BORDER_WIDTH = 10
FPS = 30
CELL = 80
INFO_WINDOW_HEIGHT = 40
WIDTH = 8 * CELL + CELL + FONT_SIZE
HEIGHT = 8 * CELL + CELL + INFO_WINDOW_HEIGHT + FONT_SIZE

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Master')
font = pygame.font.Font(None, FONT_SIZE)
textures = {
    'board': pygame.image.load('./assets/board.jpg')
}
for i in range(1, 9):
    textures[str(i)] = font.render(str(i), True, BORDER_COLOR)
    textures[chr(96 + i)] = font.render(chr(96 + i), True, BORDER_COLOR)

running = True
clock = pygame.time.Clock()


def draw_texture(canvas, x, y, width, height, texture):
    for i in range(x, width, texture.get_width()):
        for j in range(y, height, texture.get_height()):
            canvas.blit(texture, (i, j))


while running:
    clock.tick(FPS)
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # rendering
    screen.fill((0, 0, 0))
    draw_texture(screen, 0, 0, WIDTH, HEIGHT, textures['board'])

    pygame.draw.rect(screen, BORDER_COLOR, (0, 0, WIDTH, BORDER_WIDTH))
    pygame.draw.rect(screen, BORDER_COLOR, (0, HEIGHT - BORDER_WIDTH, WIDTH, BORDER_WIDTH))
    pygame.draw.rect(screen, BORDER_COLOR, (0, 0, BORDER_WIDTH, HEIGHT))
    pygame.draw.rect(screen, BORDER_COLOR, (WIDTH - BORDER_WIDTH, 0, BORDER_WIDTH, HEIGHT))
    for i in range(1, 9):
        x_coord = CELL // 2
        y_coord = CELL * (i - 1) + CELL
        ix = 8 - i + 1

        text_rect = textures[str(ix)].get_rect(center=(x_coord, y_coord))
        screen.blit(textures[str(ix)], text_rect)
    for i in range(8):
        y_coord = CELL // 2 + CELL * 8 + FONT_SIZE
        x_coord = CELL * i + CELL + FONT_SIZE
        ix = chr(97 + i)

        text_rect = textures[ix].get_rect(center=(x_coord, y_coord))
        screen.blit(textures[ix], text_rect)
    for y in range(8):
        for x in range(8):
            x_coord = CELL // 2 + CELL * x + FONT_SIZE
            y_coord = CELL // 2 + CELL * y
            if x % 2 == 0 and y % 2 == 0 or x % 2 != 0 and y % 2 != 0:
                cell_color = (255, 255, 255)
            else:
                cell_color = (0, 0, 0)
            pygame.draw.rect(screen, cell_color, (x_coord, y_coord, CELL, CELL))

    pygame.display.update()
pygame.quit()