import pygame
from abc import ABC
import platform

class Image(ABC):

    def __init__(self, nom, position):
        """
        Toute forme d'image utilisée dans le programme
        :param nom: Nom de l'image
        :param position: Position (largeur,hauteur) en pixel
        """
        self.nom = nom
        self.position = position
        self.image = None
        self.dimension = None
        self.platform_slash = '\\' if platform.system() == "Windows" else '/'
        self.init_image()
        self.__init_dimension()


    def blit(self, screen):
        """
        Affiche l'image sur l'écran
        :param screen: Écran sur laquelle afficher
        """
        screen.blit(self.image, self.position)

    def init_image(self):
        """
        Initialise l'image
        Est overide dans toutes les classes filles
        """
        self.image = pygame.image.load("Vue" + self.platform_slash + "images" + self.platform_slash + self.nom + ".png")

    def __init_dimension(self):
        """
        Initialise les dimentions de l'image
        """
        self.dimension = self.image.get_rect().size

    @staticmethod
    def DIMENSION_CASE():
        """
        :return: Valeur de la longeur d'un des côté d'une case
        """
        return 41

    @staticmethod
    def BOTTOM_LEFT():
        """
        :return: Valeur du coin en bas à droite de l'échiquier
        """
        return [24, 350]
