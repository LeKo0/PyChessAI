import pygame
from Vue.image import Image

class Piece(Image):

    def __init__(self, nom, estBlanc, coordonnees):
        self.estVert = False
        self.estBlanc = estBlanc
        self.coordonnees = coordonnees
        super().__init__(nom, [coordonnees[0] * Image.DIMENSION_CASE() + Image.BOTTOM_LEFT()[0], -(self.coordonnees[1] + 1) * Image.DIMENSION_CASE() + Image.BOTTOM_LEFT()[1]])

    def setPosition(self, coordonnees):
        """
        Changer la position (l'index dans lequel il va se trouver) et sa location (position dans l'interface)
        :param coordonnees: Nouvelles coordonnées de la pièce
        """
        self.coordonnees = coordonnees
        self.position = [coordonnees[0] * Image.DIMENSION_CASE() + Image.BOTTOM_LEFT()[0], -(self.coordonnees[1] + 1) * Image.DIMENSION_CASE() + Image.BOTTOM_LEFT()[1]]

    def init_image(self):
        self.image = pygame.image.load("Vue" + self.platform_slash + "images" + self.platform_slash + self.nom + (" blanc" if self.estBlanc else " noir") + ".png")


