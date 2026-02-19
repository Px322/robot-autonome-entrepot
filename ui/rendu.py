import pygame

class Rendu:
    def __init__(self, entrepot):
        self.entrepot = entrepot
        self.taille_case = 40
        largeur_pixels = entrepot.largeur * self.taille_case
        hauteur_pixels = entrepot.hauteur * self.taille_case
        self.fenetre = pygame.display.set_mode((largeur_pixels, hauteur_pixels))
        pygame.display.set_caption("Robot entrepot")


    # Partie affichage
    def dessiner_grille(self):
        for ligne in range(self.entrepot.hauteur):
            for col in range(self.entrepot.largeur):
                if self.entrepot.grille[ligne][col] == 1:
                    couleur = (50, 50, 50)
                else:
                    couleur = (255, 255, 255)
                pygame.draw.rect(self.fenetre, couleur, (
                    col * self.taille_case,
                    ligne * self.taille_case,
                    self.taille_case - 1,
                    self.taille_case - 1
                ))

    def dessiner_point_recup(self):
        for zone in self.entrepot.point_recup:
            col, ligne = zone["position"]
            pygame.draw.rect(self.fenetre, (0, 100, 255), (
                col * self.taille_case,
                ligne * self.taille_case,
                self.taille_case - 1,
                self.taille_case - 1
            ))

    def dessiner_deposit(self):
        col, ligne = self.entrepot.arrivee
        pygame.draw.rect(self.fenetre, (0, 200, 0), (
            col * self.taille_case,
            ligne * self.taille_case,
            self.taille_case - 1,
            self.taille_case - 1
        ))

    def dessiner_chemin(self, robot):
        for case in robot.chemin:
            col, ligne = case
            pygame.draw.rect(self.fenetre, (255, 255, 0), (
                col * self.taille_case + 10,
                ligne * self.taille_case + 10,
                self.taille_case - 20,
                self.taille_case - 20
            ))

    def dessiner_robot(self, robot):
        col, ligne = robot.pos_actuelle
        pygame.draw.rect(self.fenetre, (255, 0, 0), (
            col * self.taille_case + 5,
            ligne * self.taille_case + 5,
            self.taille_case - 10,
            self.taille_case - 10
        ))

    def mise_a_jour(self):
        pygame.display.flip()