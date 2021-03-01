def Dijkstra(matrice,s):
    c=[]
    infini=float('inf')
    nb_sommets=len(matrice)

    s_connus={s:[0,[s]]}
    s_inconnus={k:[infini,''] for k in range(nb_sommets) if k!=s}
    suivant=0
    while suivant< nb_sommets:
        if matrice[s][suivant]:
           s_inconnus[suivant]=[matrice[s][suivant], s]
        suivant+=1
#phase de recherche du plus court chemin:
    while s_inconnus and any(s_inconnus[k][0]<infini for k in s_inconnus):
        u=min(s_inconnus,key=s_inconnus.get)
        longueur_u,predecesseur_u=s_inconnus[u]
        for v in range(nb_sommets):
            if matrice[u][v] and v in s_inconnus:
                d=longueur_u+matrice[u][v]
                if d<s_inconnus[v][0]:
                    s_inconnus[v]=[d,u]
       
        s_connus[u]=[longueur_u,s_connus[predecesseur_u][1]+[u]]
        del s_inconnus[u]
        c=c+[map(str,s_connus[u][1])]
    print('plus court chemin de longueur',longueur_u,':','-->'.join(c[len(c)-1]))

    for k in s_inconnus:
        print("il n'y a pas de chemin de {} à {}".format(s,k))
    return s_connus
matrice=[[0,3,7,0,0,0],
        [3,0,2,4,0,0],
        [7,2,0,1,5,0],
        [0,4,1,0,0,9],
        [0,0,5,0,0,1],
        [0,0,0,9,1,0]]
Dijkstra(matrice,0)
