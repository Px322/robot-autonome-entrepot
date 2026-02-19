import heapq

def a_star(grille, depart, arrivee):
    a_explorer = []
    preced = {}
    cout = {}
    
    heapq.heappush(a_explorer, (0, depart))
    cout[tuple(depart)] = 0

    while a_explorer:
        f_actuel, case_actuelle = heapq.heappop(a_explorer)
        if case_actuelle == arrivee:
            break

        voisins = [
            [case_actuelle[0]+1, case_actuelle[1]],
            [case_actuelle[0]-1, case_actuelle[1]],
            [case_actuelle[0], case_actuelle[1]+1],
            [case_actuelle[0], case_actuelle[1]-1],
        ]

        for voisin in voisins:
            col, ligne = voisin

            if not (0 <= col < len(grille[0]) and 0 <= ligne < len(grille)):
                continue

            if grille[ligne][col] == 1:
                continue

            nouveau_cout = cout[tuple(case_actuelle)] + 1

            if tuple(voisin) not in cout or nouveau_cout < cout[tuple(voisin)]:
                cout[tuple(voisin)] = nouveau_cout
                f_score = nouveau_cout + heuristique(voisin, arrivee)
                heapq.heappush(a_explorer, (f_score, voisin))
                preced[tuple(voisin)] = case_actuelle

    chemin = []
    case = arrivee
    while case != depart:
        chemin.append(case)
        case = preced[tuple(case)]
    chemin.append(depart)
    chemin.reverse()
    return chemin



def heuristique(a,b):
    distance_man = abs(a[0]-b[0]) + abs(a[1]-b[1])
    return distance_man

