import pygame
from core.entrepot import Entrepot
from core.robot import Robot
from ui.rendu import Rendu
print("1 - import ok")
# Initialisation
pygame.init()
print("2 - pygame init ok")
import os
entrepot = Entrepot(os.path.join(os.path.dirname(__file__), "data", "entrepot.json"))
print("3 - entrepot ok")
robot = Robot(entrepot.depart, entrepot.grille)
print("4 - robot ok")

rendu = Rendu(entrepot)
print("5 - rendu ok")

robot.ajouter_commande(entrepot.point_recup[0]["position"])  #Point de recup 1
robot.ajouter_commande(entrepot.point_recup[1]["position"])  # -- 2
robot.ajouter_commande(entrepot.point_recup[2]["position"])  # -- 3 
robot.ajouter_commande(entrepot.arrivee)


robot.calculer_chemin(robot.file_commandes.pop(0), entrepot.grille)


clock = pygame.time.Clock()
compteur = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Le robot avance toutes les 10 frames
    compteur += 1
    if compteur >= 30:
        compteur = 0
        if robot.chemin:
            robot.avancer()
        elif robot.file_commandes:
            robot.calculer_chemin(robot.file_commandes.pop(0), entrepot.grille)

    # Dessin
    rendu.fenetre.fill((200, 200, 200))
    rendu.dessiner_grille()
    rendu.dessiner_point_recup()
    rendu.dessiner_deposit()
    rendu.dessiner_chemin(robot)
    rendu.dessiner_robot(robot)
    rendu.mise_a_jour()

    clock.tick(60)