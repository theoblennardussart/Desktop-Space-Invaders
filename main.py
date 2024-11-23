import cv2
import pygame
import os
import time


pygame.init()
ev = pygame.event.poll()

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,0)
img = cv2.imread("venv/include/images/Player.png", cv2.IMREAD_COLOR)
cv2.imshow("I2", img)
cv2.moveWindow("I2", 50, 650)

def main():

    x_coord = 50
    offset = 10
    gameIsRunnig = True
    charachter_speed = 0.05
    while gameIsRunnig:

        key = pygame.key.get_pressed()

        if key[pygame.K_ESCAPE]:
            cv2.destroyAllWindows()
            print("ESCAPE")
            gameIsRunnig = False 

        if key[pygame.K_a]:
            x_coord -= offset
            cv2.moveWindow("I2", x_coord, 650)
            time.sleep(charachter_speed)


        if key[pygame.K_d]:
            x_coord += offset
            cv2.moveWindow("I2", x_coord, 650)
            time.sleep(charachter_speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


if __name__ == "__main__":
    main()