from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    res=0
    cpt=-1
    A=image.binarisation(S)
    b=A.localisation()
    for i in list (liste_modeles):
        c=b.resize(i.H, i.W)
        if c.similitude(i)>res:
            res=c.similitude(i)
            cpt=cpt+1
    return cpt

