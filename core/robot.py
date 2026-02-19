from core.a_star import a_star

class Robot:
    def __init__(self, pos_actuelle, grille):
        self.pos_actuelle = pos_actuelle
        self.chemin = []
        self.colis = False
        self.file_commandes = []

    def calculer_chemin(self, destination, grille):
        self.chemin = a_star(grille, self.pos_actuelle, destination)

    def avancer(self):
        if not self.chemin:
            return None
        self.pos_actuelle=self.chemin.pop(0)

    def ajouter_commande(self,destination):
        self.file_commandes.append(destination)


