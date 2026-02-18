import heapq

def astar(grille,depart,arrivee):
    a_explorer = []  
    preced = {}     
    cout = {}    
    heapq.heappush(a_explorer, (0, depart))
    cout[tuple(depart)] = 0      
    while a_explorer:
        f_actuel,case_actuelle = heapq.heappop(a_explorer)
        if case_actuelle == arrivee:
            break


def heuristique(a,b):
    distance_man = abs(a[0]-b[0]) + (a[1]-b[1])
    return distance_man

