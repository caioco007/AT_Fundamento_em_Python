import pygame, sys, random
from collections import namedtuple

class Jogo:
    # Coordinates
    Coordinate = namedtuple('Coordinate', ['x', 'y'])
    running = True
    preto = (0,0,0)
    azul = (0, 0, 255)
    cinza = (128,128,128)

    lista = []

    def __init__(self):
        # Game init
        pygame.init()
        pygame.font.init()

        self.font = pygame.font.Font(None, 22)
        self.screenSize = self.Coordinate(x=800, y=600)
        self.screen = pygame.display.set_mode(self.screenSize)

        # Change title
        pygame.display.set_caption('Questão 08')

        self.button = pygame.Rect(self.screen.get_width() // 2 - 50, 50, 100, 100)

        # main loop
        self.loop()

    def loop(self):
        # Game loop
        while self.running:
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.sair()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse(event)

            # paint the screen
            self.screen.fill(self.preto)

            self.circulo_botao('Clique')

            for square in self.lista:
                pygame.draw.rect(self.screen, self.azul, square)

            # Update the display
            pygame.display.update()

        pygame.display.quit()

    def sair(self):
        self.running = False
        sys.exit()

    def mouse(self, event):
        if event.button == 1:
            position = pygame.mouse.get_pos()

            if self.button.collidepoint(position):
                rect = self.quadrado()
                self.lista.append(rect)
                self.colisao(rect)

    def circulo_botao(self, text):
        pygame.draw.ellipse(self.screen, self.cinza, self.button)
        button_text = self.font.render(text, False, self.preto)
        button_text_rect = button_text.get_rect(center=self.button.center)

        self.screen.blit(button_text, button_text_rect)

    def quadrado(self):
        x = random.randint(25, self.screen.get_width() - 25)
        y = random.randint(25, self.screen.get_height() - 25)

        return pygame.Rect(x, y, 50, 50)

    def colisao(self, rect):
        for square in self.lista:
            if square is not rect and square.colliderect(rect):
                self.lista.remove(square)
                if rect in self.lista:
                    self.lista.remove(rect)


jogo = Jogo()