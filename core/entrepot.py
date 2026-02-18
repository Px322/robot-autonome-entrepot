import json

class Entrepot:
    
    def __init__(self,map_path):
        with open(map_path, 'r') as f:
            data = json.load(f)
        self.largeur,self.hauteur = data["grille"]
        self.etageres = data["etageres"]
        self.point_recup = data["point_recup"]
        self.depart = data["depart"]
        self.arrivee = data["arrivee"]

        self.grille = [[0 for _ in range(self.largeur)] for _ in range(self.hauteur)]
        
        for etagere in self.etageres:
            col, ligne = etagere
            self.grille[ligne][col] = 1