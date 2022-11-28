# John Conway's Game of Life
# Basado en lo escrito por
# https://beltoforion.de/en/recreational_mathematics/game_of_life.php

# A living cell dies if it has fewer than two living neighboring cells.
# A living cell with two or three living neighbors lives on.
# A living cell with more than three living neighboring cells dies in the next time step.
# A dead cell is revived if it has exactly three living neighboring cells.

import pygame
import numpy as np

WIDTH, HEIGHT = 600, 600  # Establecer tamanos predeterminados

# Pixels
LIFE = (34, 139, 34)  # Color de vida
DEATH = (139, 69, 19)  # Color de muerte
ENVMAP = (1, 1, 1)  # Color de fondo
GRID = (1, 1, 0)  # Color de grid
PIXELS = 10  # Tamano de pixeles


# Funcion main
def main():
    pygame.init()
    pygame.display.set_caption("John Conway's Game of Life")  # Caption
    SCREEN = pygame.display.set_mode(
        (WIDTH, HEIGHT))  # Display pantalla, aka surface
    cells = np.zeros((WIDTH//10, HEIGHT//10))  # Matriz
    SCREEN.fill(ENVMAP)
    # Actualizar funcion core
    pixelCharm(screen=SCREEN, pixel=cells, size=PIXELS)
    pygame.display.update()
    isIt = False
    # Array
    pixelArray = [[-11, 10],
                  [1, -10],
                  [11, -10],
                  [-11, 0],
                  [11, 0],
                  [-11, 10],
                  [1, 10],
                  [11, 10],
                  [-21, 20],
                  [1, -20],
                  [21, -20],
                  [-21, 0],
                  [21, 0],
                  [-21, 20],
                  [1, 20],
                  [21, 20],
                  [-31, 30],
                  [1, -30],
                  [31, -30],
                  [-31, 0],
                  [31, 0],
                  [-31, 30],
                  [1, 30],
                  [31, 30], ]

    """
    # https://matgomes.com/conways-game-of-life-python/
    for (x, y) in grid.cells:
        pygame.draw.rect(window,
                        (255, 1, 0),
                        (x * cell_width + border_size, y * cell_height +
                         border_size, cell_width - border_size, cell_height - border_size))
    """
    # For loop basado en https://matgomes.com/conways-game-of-life-python/
    for pixel in pixelArray:
        cells[[pixel[0], pixel[1]]] = 1
        pygame.draw.rect(
            SCREEN, LIFE, (pixel[1]*PIXELS, pixel[0]*PIXELS, 4, 4))
        pixelCharm(SCREEN, cells, PIXELS)

    # Salir de pygame
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            else:
                isIt = not isIt
                pixelCharm(SCREEN, cells, PIXELS)
                pygame.display.update()
        SCREEN.fill(GRID)
        if isIt:
            cells = pixelCharm(SCREEN, cells, PIXELS)
            pygame.display.update()

# Funcion basada en lo escrito por
# https://beltoforion.de/en/recreational_mathematics/game_of_life.php


def pixelCharm(screen, pixel, size, isAlive=False):
    # 2 dimensiones inicializado con 0s
    pixels = np.zeros((pixel.shape[0], pixel.shape[1]))

    for i, j in np.ndindex(pixel.shape):  # Core function

        pixelLife = np.sum(pixel[i-1:i+2, j-1:j+2]) - pixel[i, j]
        pixelColor = ENVMAP if pixel[i, j] == 0 else LIFE

        if pixel[i, j] == 1:
            if pixelLife < 2 or pixelLife > 3:
                if isAlive:
                    pixelColor = DEATH  # Se asigna color segun su estatus
            elif 2 <= pixelLife <= 3:
                pixels[i, j] = 1
                if isAlive:
                    pixelColor = pixelLife  # Se asigna color segun su estatus
        else:
            if pixelLife == 3:
                pixels[i, j] = 1
                if isAlive:
                    pixelColor = pixelLife  # Se asigna color segun su estatus

        pygame.draw.rect(screen, pixelColor, (j*size, i *
                         size, size - 1, size - 1))

    return pixels


if __name__ == "__main__":
    main()
