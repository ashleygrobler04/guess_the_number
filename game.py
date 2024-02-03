import pygame
import states
pygame.init()
pygame.display.set_mode((500, 500))


class Game:
    def __init__(self):
        states.main_state_machine.to("main menu")

    def loop(self):
        states.main_state_machine.run()


g = Game()
while 1:
    pygame.display.update()
    g.loop()
