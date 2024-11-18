import pygame
import random
rows = 20
cols = 16
square_size = 32
screen_len = 640
screen_width = 512


def draw_grid(surf):
    for row in range(rows):
        pygame.draw.line(
            surf,
            'black',
            (row*square_size, 0),
            (row*square_size, screen_width),
            1
        )
    for col in range(cols):
        pygame.draw.line(
            surf,
            'black',
            (0,col * square_size),
            (screen_len,col * square_size),
            1
        )
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_x = 0
        mole_y = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    grid_x = mouse_x // square_size
                    grid_y = mouse_y // square_size
                    if (grid_x, grid_y) == (mole_x // square_size, mole_y // square_size):
                        mole_x = random.randrange(0, screen_len, square_size)
                        mole_y = random.randrange(0, screen_width, square_size)

            screen.fill("light green")
            draw_grid(screen)
            pygame.draw.line(
                screen,
                'black',
                (screen_len,0),
                (screen_len,screen_width),
                1
            )
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x,mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
